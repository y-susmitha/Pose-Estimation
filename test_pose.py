from camera import Camera
from pose_detector import PoseDetector
import cv2


# ------------------------------------------------
# Initialize camera
# ------------------------------------------------
camera = Camera()

# ------------------------------------------------
# Initialize MediaPipe pose detector
# ------------------------------------------------
detector = PoseDetector()


# ------------------------------------------------
# Check camera
# ------------------------------------------------
if not camera.is_opened():

    print("ERROR: Camera could not be opened.")

    exit()


print("======================================")
print(" RehabRanger Live Pose Detection")
print("======================================")
print("Camera started successfully.")
print("MediaPipe pose detection started.")
print("Press Q to quit.")


# ------------------------------------------------
# Main loop
# ------------------------------------------------
while True:

    # Get frame from camera
    frame = camera.read()

    if frame is None:

        print("ERROR: Could not read camera frame.")

        break


    # Detect pose
    results = detector.detect(frame)


    # Draw MediaPipe landmarks
    frame = detector.draw_landmarks(
        frame,
        results
    )


    # Display camera image
    cv2.imshow(
        "RehabRanger - Live Pose Detection",
        frame
    )


    # Press Q to exit
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):

        break


# ------------------------------------------------
# Release resources
# ------------------------------------------------
detector.close()

camera.release()

cv2.destroyAllWindows()


print("Pose detection stopped.")
print("Camera released.")
