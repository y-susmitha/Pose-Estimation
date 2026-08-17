import cv2


class SessionEngine:

    def __init__(self, camera, pose_detector):

        self.camera = camera
        self.pose_detector = pose_detector

        self.running = False
        self.reps = 0
        self.state = "START"

    def start(self):

        self.running = True

        print("======================================")
        print("      RehabRanger Session")
        print("======================================")
        print("Live pose estimation started.")
        print("Press Q to stop.")
        print("--------------------------------------")

        while self.running:

            # Get frame from camera
            frame = self.camera.read()

            if frame is None:

                print("ERROR: Could not read camera frame.")
                break

            # Detect human pose
            results = self.pose_detector.detect(frame)

            # Draw MediaPipe landmarks
            frame = self.pose_detector.draw_landmarks(
                frame,
                results
            )

            # Get landmarks
            landmarks = self.pose_detector.get_landmarks(
                results
            )

            # Check whether a person is detected
            if landmarks:

                cv2.putText(
                    frame,
                    "POSE DETECTED",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    "NO POSE DETECTED",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

            # Display repetitions
            cv2.putText(
                frame,
                "Reps: {}".format(self.reps),
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            # Display current state
            cv2.putText(
                frame,
                "State: {}".format(self.state),
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            # Display camera
            cv2.imshow(
                "RehabRanger",
                frame
            )

            # Press Q to quit
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                self.stop()

        self.cleanup()

    def stop(self):

        self.running = False

        print("Stopping session...")

    def cleanup(self):

        self.camera.release()

        self.pose_detector.close()

        cv2.destroyAllWindows()

        print("RehabRanger session ended.")
