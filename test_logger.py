from logger import RehabLogger


# Create logger
logger = RehabLogger("output")


print("================================")
print(" RehabRanger Logger Test")
print("================================")


# -----------------------------------------
# Session started
# -----------------------------------------

logger.session_start(
    exercise="Side Arm Raise"
)

print("Session started")


# -----------------------------------------
# Log joint angle
# -----------------------------------------

logger.log_angle(
    joint="shoulder",
    angle=85.5,
    exercise="Side Arm Raise"
)

print("Shoulder angle logged")


# -----------------------------------------
# Log repetition
# -----------------------------------------

logger.log_repetition(
    exercise="Side Arm Raise",
    reps=1
)

print("Repetition logged")


# -----------------------------------------
# Log feedback
# -----------------------------------------

logger.log_feedback(
    exercise="Side Arm Raise",
    message="Excellent"
)

print("Feedback logged")


# -----------------------------------------
# Log compensation
# -----------------------------------------

logger.log_compensation(
    exercise="Side Arm Raise",
    message="Avoid leaning your trunk"
)

print("Compensation logged")


# -----------------------------------------
# Log MediaPipe landmarks
# -----------------------------------------

landmarks = [
    {
        "id": 11,
        "x": 0.45,
        "y": 0.32,
        "z": -0.10
    },
    {
        "id": 13,
        "x": 0.50,
        "y": 0.48,
        "z": -0.08
    },
    {
        "id": 15,
        "x": 0.55,
        "y": 0.62,
        "z": -0.05
    }
]


logger.log_keypoints(
    landmarks,
    frame_number=1
)

print("Keypoints logged")


# -----------------------------------------
# Session ended
# -----------------------------------------

logger.session_end(
    exercise="Side Arm Raise",
    reps=1
)

print("Session ended")

print("\nLogging completed.")
