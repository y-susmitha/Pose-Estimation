from compensation import CompensationDetector


detector = CompensationDetector()


print("================================")
print(" RehabRanger Compensation Test")
print("================================")


# --------------------------------
# Test 1: Correct angle
# --------------------------------

detector.reset()

result = detector.check_angle(
    angle=45,
    minimum=40,
    maximum=50,
    message="Keep your elbow position correct"
)

print("\nTest 1")
print("Compensation:", result)
print("Feedback:", detector.get_feedback())


# --------------------------------
# Test 2: Incorrect angle
# --------------------------------

detector.reset()

result = detector.check_angle(
    angle=70,
    minimum=40,
    maximum=50,
    message="Correct your elbow angle"
)

print("\nTest 2")
print("Compensation:", result)
print("Feedback:", detector.get_feedback())


# --------------------------------
# Test 3: Trunk alignment
# --------------------------------

detector.reset()

result = detector.check_vertical_alignment(
    shoulder_x=300,
    hip_x=380,
    tolerance=50
)

print("\nTest 3")
print("Compensation:", result)
print("Feedback:", detector.get_feedback())


# --------------------------------
# Test 4: Correct trunk alignment
# --------------------------------

detector.reset()

result = detector.check_vertical_alignment(
    shoulder_x=300,
    hip_x=320,
    tolerance=50
)

print("\nTest 4")
print("Compensation:", result)
print("Feedback:", detector.get_feedback())


# --------------------------------
# Test 5: Knee alignment
# --------------------------------

detector.reset()

result = detector.check_knee_position(
    knee_x=400,
    ankle_x=470,
    tolerance=40
)

print("\nTest 5")
print("Compensation:", result)
print("Feedback:", detector.get_feedback())
