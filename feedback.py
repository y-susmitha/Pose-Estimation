class FeedbackEngine:

    def __init__(self):

        self.feedback_messages = {
            "DOWN": "Lower Completely",
            "UP": "Excellent",
            "TOO_FAST": "Slow Down",
            "TOO_SLOW": "Lift Smoothly",
            "INCORRECT": "Correct Your Form",
            "NO_POSE": "Move Into Camera View",
            "GOOD_FORM": "Good Form"
        }

        self.current_feedback = "Ready"

    def get_feedback(self, state):

        if state in self.feedback_messages:

            self.current_feedback = \
                self.feedback_messages[state]

        else:

            self.current_feedback = "Keep Going"

        return self.current_feedback

    def update(self, state):

        return self.get_feedback(state)

    def reset(self):

        self.current_feedback = "Ready"

        return self.current_feedback
