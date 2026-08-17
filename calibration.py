import statistics


class Calibration:

    def __init__(self, sample_count=30):

        self.sample_count = sample_count
        self.samples = []
        self.calibrated = False

        self.mean = None
        self.std = None

    def add_sample(self, angle):

        if angle is None:
            return False

        self.samples.append(float(angle))

        if len(self.samples) >= self.sample_count:

            self.calculate_baseline()

            return True

        return False

    def calculate_baseline(self):

        if len(self.samples) == 0:
            return False

        self.mean = statistics.mean(self.samples)

        if len(self.samples) > 1:
            self.std = statistics.stdev(self.samples)
        else:
            self.std = 0.0

        self.calibrated = True

        return True

    def is_calibrated(self):

        return self.calibrated

    def get_baseline(self):

        if not self.calibrated:
            return None

        return {
            "mean": self.mean,
            "std": self.std
        }

    def reset(self):

        self.samples = []
        self.calibrated = False

        self.mean = None
        self.std = None

    def remaining_samples(self):

        remaining = self.sample_count - len(self.samples)

        if remaining < 0:
            remaining = 0

        return remaining
