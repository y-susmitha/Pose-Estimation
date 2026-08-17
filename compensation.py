class CompensationDetector:

    def __init__(self):

        self.issues = []

    def check_angle(
        self,
        angle,
        minimum=None,
        maximum=None,
        message="Incorrect angle"
    ):

        if angle is None:

            return False

        if minimum is not None and angle < minimum:

            self.add_issue(message)

            return True

        if maximum is not None and angle > maximum:

            self.add_issue(message)

            return True

        return False

    def check_vertical_alignment(
        self,
        shoulder_x,
        hip_x,
        tolerance=50,
        message="Keep your trunk straight"
    ):

        if shoulder_x is None or hip_x is None:

            return False

        difference = abs(shoulder_x - hip_x)

        if difference > tolerance:

            self.add_issue(message)

            return True

        return False

    def check_knee_position(
        self,
        knee_x,
        ankle_x,
        tolerance=40,
        message="Keep your knee aligned with your ankle"
    ):

        if knee_x is None or ankle_x is None:

            return False

        difference = abs(knee_x - ankle_x)

        if difference > tolerance:

            self.add_issue(message)

            return True

        return False

    def add_issue(self, message):

        if message not in self.issues:

            self.issues.append(message)

    def get_feedback(self):

        if len(self.issues) == 0:

            return "Good Form"

        return " | ".join(self.issues)

    def has_compensation(self):

        return len(self.issues) > 0

    def reset(self):

        self.issues = []
