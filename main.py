import cv2
import yaml
import os

from camera import Camera
from pose_detector import PoseDetector
from exercise_loader import ExerciseLoader
from session_engine import SessionEngine
from logger import Logger

from utils.geometry import landmarks_reliable


def calculate_exercise_angle(
        exercise,
        landmarks):

    from utils.geometry import (
        get_landmark_point,
        calculate_angle
    )

    name = exercise["name"]

    if name == "Side Arm Raise":

        hip = get_landmark_point(
            landmarks,
            exercise["landmarks"]["hip"]
        )

        shoulder = get_landmark_point(
            landmarks,
            exercise["landmarks"]["shoulder"]
        )

        elbow = get_landmark_point(
            landmarks,
            exercise["landmarks"]["elbow"]
        )

        return calculate_angle(
            hip,
            shoulder,
            elbow
        )

    if name == "Lunges":

        hip = get_landmark_point(
            landmarks,
            exercise["landmarks"]["hip"]
        )

        knee = get_landmark_point(
            landmarks,
            exercise["landmarks"]["knee"]
        )

        ankle = get_landmark_point(
            landmarks,
            exercise["landmarks"]["ankle"]
        )

        return calculate_angle(
            hip,
            knee,
            ankle
        )

    if name == "Seated Dorsiflexion":

        knee = get_landmark_point(
            landmarks,
            exercise["landmarks"]["knee"]
        )

        ankle = get_landmark_point(
            landmarks,
            exercise["landmarks"]["ankle"]
        )

        foot = get_landmark_point(
            landmarks,
            exercise["landmarks"]["foot"]
        )

        return calculate_angle(
            knee,
            ankle,
            foot
        )

    return None


def main():

    # -------------------------------------------------
    # LOAD CONFIGURATION
    # -------------------------------------------------

    with open(
            "config.yaml",
            "r") as file:

        config = yaml.safe_load(file)

    # -------------------------------------------------
    # CAMERA
    # -------------------------------------------------

    camera_config = config["camera"]

    camera = Camera(

        camera_id=camera_config["id"],

        width=camera_config["width"],

        height=camera_config["height"]
    )

    if not camera.is_opened():

        print("ERROR: Camera could not be opened.")

        return

    # -------------------------------------------------
    # POSE DETECTOR
    # -------------------------------------------------

    pose_config = config["pose"]

    detector = PoseDetector(

        min_detection_confidence=
            pose_config["detection_confidence"],

        min_tracking_confidence=
            pose_config["tracking_confidence"]
    )

    # -------------------------------------------------
    # EXERCISES
    # -------------------------------------------------

    loader = ExerciseLoader(
        "exercises"
    )

    exercise_files = (
        config["session"]["exercises"]
    )

    exercises = loader.load_all(
        exercise_files
    )

    exercise_list = []

    for filename in exercise_files:

        with open(
                os.path.join(
                    "exercises",
                    filename
                ),
                "r") as file:

            exercise_list.append(
                yaml.safe_load(file)
            )

    # -------------------------------------------------
    # SESSION
    # -------------------------------------------------

    session = SessionEngine(
        exercise_list
    )

    # -------------------------------------------------
    # LOGGER
    # -------------------------------------------------

    logger = Logger(
        config["output"]["directory"]
    )

    print()
    print(
        "================================="
    )
    print(
        "       RehabRanger"
    )
    print(
        "================================="
    )
    print(
        "Starting guided rehabilitation session"
    )
    print(
        "Press Q to quit."
    )
    print()

    # -------------------------------------------------
    # MAIN LOOP
    # -------------------------------------------------

    while True:

        frame = camera.read()

        if frame is None:

            print(
                "Camera frame unavailable."
            )

            break

        results = detector.process(
            frame
        )

        landmarks = (
            detector.get_landmarks(
                results
            )
        )

        # ---------------------------------------------
        # POSE AVAILABLE
        # ---------------------------------------------

        if landmarks is not None:

            logger.log_keypoints(
                landmarks
            )

            current_exercise = (
                session.current_exercise
            )

            required_indices = []

            for value in (
                current_exercise[
                    "landmarks"
                ].values()
            ):

                required_indices.append(
                    value
                )

            reliability_threshold = (
                current_exercise[
                    "reliability"
                ]["threshold"]
            )

            reliable = landmarks_reliable(

                landmarks,

                required_indices,

                reliability_threshold
            )

            if reliable:

                angle = (
                    calculate_exercise_angle(
                        current_exercise,
                        landmarks
                    )
                )

            else:

                angle = None

            # -----------------------------------------
            # SESSION PROCESSING
            # -----------------------------------------

            result = session.process(

                landmarks,

                angle,

                reliable
            )

            # -----------------------------------------
            # LOG EVENTS
            # -----------------------------------------

            if result:

                if angle is not None:

                    logger.log_event(

                        result["exercise"],

                        "angle",

                        angle
                    )

                logger.log_event(

                    result["exercise"],

                    "state",

                    result["stage"]
                )

            # -----------------------------------------
            # DRAW POSE
            # -----------------------------------------

            frame = detector.draw(
                frame,
                results
            )

            # -----------------------------------------
            # DISPLAY
            # -----------------------------------------

            if result:

                cv2.putText(

                    frame,

                    "Exercise: {}".format(
                        result["exercise"]
                    ),

                    (20, 35),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (0, 255, 0),

                    2
                )

                angle_text = "Angle: --"

                if result["angle"] is not None:

                    angle_text = (
                        "Angle: {:.1f}".format(
                            result["angle"]
                        )
                    )

                cv2.putText(

                    frame,

                    angle_text,

                    (20, 70),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (255, 255, 255),

                    2
                )

                cv2.putText(

                    frame,

                    "Reps: {}/{}".format(

                        result["reps"],

                        result["target"]
                    ),

                    (20, 105),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (0, 255, 255),

                    2
                )

                cv2.putText(

                    frame,

                    "Stage: {}".format(
                        result["stage"]
                    ),

                    (20, 140),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (255, 255, 0),

                    2
                )

                cv2.putText(

                    frame,

                    result["feedback"],

                    (20, 180),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.65,

                    (0, 255, 0),

                    2
                )

        else:

            cv2.putText(

                frame,

                "No pose detected",

                (20, 40),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.8,

                (0, 0, 255),

                2
            )

        # ---------------------------------------------
        # SESSION COMPLETE
        # ---------------------------------------------

        if session.is_complete():

            cv2.putText(

                frame,

                "SESSION COMPLETE",

                (250, 300),

                cv2.FONT_HERSHEY_SIMPLEX,

                1.2,

                (0, 255, 0),

                3
            )

        cv2.imshow(
            "RehabRanger",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):

            break

    # -------------------------------------------------
    # CLEANUP
    # -------------------------------------------------

    camera.release()

    detector.close()

    logger.save()

    cv2.destroyAllWindows()

    print()
    print(
        "Session data saved to output/"
    )


if __name__ == "__main__":

    main()
