from repetition_counter import RepetitionCounter


counter = RepetitionCounter(
    down_angle=165,
    up_angle=45
)


angles = [
    170,
    160,
    140,
    120,
    90,
    60,
    45,
    60,
    90,
    120,
    150,
    165,

    160,
    130,
    90,
    60,
    45,
    60,
    100,
    140,
    165
]


print("================================")
print(" RehabRanger Repetition Test")
print("================================")


for angle in angles:

    reps, state = counter.update(angle)

    print(
        "Angle: {:>3}° | State: {:>4} | Reps: {}".format(
            angle,
            state,
            reps
        )
    )


print("--------------------------------")
print("Final repetitions:", counter.get_repetitions())
print("Final state:", counter.get_state())
