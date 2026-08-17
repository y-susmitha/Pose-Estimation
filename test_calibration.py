from calibration import Calibration


calibrator = Calibration(sample_count=10)


angles = [
    170,
    171,
    169,
    170,
    170,
    171,
    169,
    170,
    170,
    171
]


print("================================")
print(" RehabRanger Calibration Test")
print("================================")


for angle in angles:

    completed = calibrator.add_sample(angle)

    print(
        "Angle: {}  Remaining samples: {}".format(
            angle,
            calibrator.remaining_samples()
        )
    )

    if completed:

        print("\nCalibration completed.")

        print(
            "Mean:",
            calibrator.mean
        )

        print(
            "Standard deviation:",
            calibrator.std
        )


print("\nCalibration status:")

print(
    calibrator.is_calibrated()
)


print("\nBaseline:")

print(
    calibrator.get_baseline()
)
