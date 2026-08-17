class StateMachine:

    def __init__(self, initial_state="START"):

        self.current_state = initial_state
        self.previous_state = initial_state

    def update(self, new_state):

        self.previous_state = self.current_state
        self.current_state = new_state

        return self.current_state

    def get_state(self):

        return self.current_state

    def get_previous_state(self):

        return self.previous_state

    def state_changed(self):

        return self.current_state != self.previous_state

    def reset(self, state="START"):

        self.current_state = state
        self.previous_state = state

    def transition(self, new_state):

        old_state = self.current_state

        self.previous_state = old_state
        self.current_state = new_state

        return old_state, new_state
