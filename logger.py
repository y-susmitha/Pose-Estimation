import os
import json
from datetime import datetime


class RehabLogger:

    def __init__(self, output_directory="output"):

        self.output_directory = output_directory

        # Create output directory if it does not exist
        if not os.path.exists(self.output_directory):

            os.makedirs(self.output_directory)

        self.events_file = os.path.join(
            self.output_directory,
            "events.json"
        )

        self.keypoints_file = os.path.join(
            self.output_directory,
            "keypoints.json"
        )

        self.events = []
        self.keypoints = []

    # --------------------------------------------------
    # Get current timestamp
    # --------------------------------------------------

    def timestamp(self):

        return datetime.now().isoformat()

    # --------------------------------------------------
    # Log a general event
    # --------------------------------------------------

    def log_event(
        self,
        event_type,
        message="",
        exercise=None,
        state=None,
        reps=None
    ):

        event = {
            "timestamp": self.timestamp(),
            "event_type": event_type,
            "message": message,
            "exercise": exercise,
            "state": state,
            "repetitions": reps
        }

        self.events.append(event)

        self.save_events()

    # --------------------------------------------------
    # Log joint angle
    # --------------------------------------------------

    def log_angle(
        self,
        joint,
        angle,
        exercise=None
    ):

        event = {
            "timestamp": self.timestamp(),
            "joint": joint,
            "angle": angle,
            "exercise": exercise
        }

        self.events.append(event)

        self.save_events()

    # --------------------------------------------------
    # Log MediaPipe landmarks
    # --------------------------------------------------

    def log_keypoints(
        self,
        landmarks,
        frame_number=None
    ):

        data = {
            "timestamp": self.timestamp(),
            "frame_number": frame_number,
            "landmarks": landmarks
        }

        self.keypoints.append(data)

        self.save_keypoints()

    # --------------------------------------------------
    # Save events to JSON
    # --------------------------------------------------

    def save_events(self):

        with open(
            self.events_file,
            "w"
        ) as file:

            json.dump(
                self.events,
                file,
                indent=4
            )

    # --------------------------------------------------
    # Save keypoints to JSON
    # --------------------------------------------------

    def save_keypoints(self):

        with open(
            self.keypoints_file,
            "w"
        ) as file:

            json.dump(
                self.keypoints,
                file,
                indent=4
            )

    # --------------------------------------------------
    # Log session start
    # --------------------------------------------------

    def session_start(
        self,
        exercise=None
    ):

        self.log_event(
            event_type="SESSION_START",
            message="Exercise session started",
            exercise=exercise
        )

    # --------------------------------------------------
    # Log session end
    # --------------------------------------------------

    def session_end(
        self,
        exercise=None,
        reps=None
    ):

        self.log_event(
            event_type="SESSION_END",
            message="Exercise session ended",
            exercise=exercise,
            reps=reps
        )

    # --------------------------------------------------
    # Log repetition
    # --------------------------------------------------

    def log_repetition(
        self,
        exercise,
        reps
    ):

        self.log_event(
            event_type="REPETITION",
            message="Repetition completed",
            exercise=exercise,
            reps=reps
        )

    # --------------------------------------------------
    # Log feedback
    # --------------------------------------------------

    def log_feedback(
        self,
        exercise,
        message
    ):

        self.log_event(
            event_type="FEEDBACK",
            message=message,
            exercise=exercise
        )

    # --------------------------------------------------
    # Log compensation
    # --------------------------------------------------

    def log_compensation(
        self,
        exercise,
        message
    ):

        self.log_event(
            event_type="COMPENSATION",
            message=message,
            exercise=exercise
        )

    # --------------------------------------------------
    # Clear all logs
    # --------------------------------------------------

    def clear(self):

        self.events = []
        self.keypoints = []

        self.save_events()
        self.save_keypoints()
