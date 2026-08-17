class RepetitionCounter:

    def __init__(
        self,
        down_angle,
        up_angle,
        start_state="DOWN"
    ):

        self.down_angle = down_angle
        self.up_angle = up_angle

        self.state = start_state
        self.previous_state = start_state

        self.reps = 0

    def update(self, angle):

        if angle is None:

            return self.reps, self.state

        self.previous_state = self.state

        # ---------------------------------------
        # Determine current exercise state
        # ---------------------------------------

        if angle >= self.down_angle:

            self.state = "DOWN"

        elif angle <= self.up_angle:

            self.state = "UP"

        # ---------------------------------------
        # Count repetition
        # ---------------------------------------

        # A complete repetition occurs when
        # the user moves from UP back to DOWN.

        if (
            self.previous_state == "UP"
            and self.state == "DOWN"
        ):

            self.reps += 1

        return self.reps, self.state

    def get_repetitions(self):

        return self.reps

    def get_state(self):

        return self.state

    def reset(self):

        self.reps = 0

        self.state = "DOWN"

        self.previous_state = "DOWN"
