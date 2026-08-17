from feedback import FeedbackEngine


feedback = FeedbackEngine()


print("================================")
print(" RehabRanger Feedback Test")
print("================================")


print("\nDOWN:")
print(feedback.get_feedback("DOWN"))


print("\nUP:")
print(feedback.get_feedback("UP"))


print("\nTOO_FAST:")
print(feedback.get_feedback("TOO_FAST"))


print("\nTOO_SLOW:")
print(feedback.get_feedback("TOO_SLOW"))


print("\nINCORRECT:")
print(feedback.get_feedback("INCORRECT"))


print("\nNO_POSE:")
print(feedback.get_feedback("NO_POSE"))


print("\nGOOD_FORM:")
print(feedback.get_feedback("GOOD_FORM"))


print("\nUNKNOWN:")
print(feedback.get_feedback("UNKNOWN"))
