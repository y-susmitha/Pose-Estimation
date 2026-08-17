import os
import yaml


class ExerciseLoader:

    def __init__(self, exercise_directory="exercises"):

        self.exercise_directory = exercise_directory

    def load(self, exercise_name):

        file_path = os.path.join(
            self.exercise_directory,
            exercise_name
        )

        if not file_path.endswith(".yaml"):
            file_path += ".yaml"

        if not os.path.exists(file_path):

            raise FileNotFoundError(
                "Exercise file not found: {}".format(file_path)
            )

        with open(
            file_path,
            "r"
        ) as file:

            config = yaml.safe_load(file)

        if config is None:

            raise ValueError(
                "Exercise configuration is empty: {}".format(file_path)
            )

        return config

    def list_exercises(self):

        if not os.path.exists(
            self.exercise_directory
        ):

            return []

        exercises = []

        for filename in os.listdir(
            self.exercise_directory
        ):

            if filename.endswith(".yaml"):

                exercises.append(
                    filename
                )

        return exercises
