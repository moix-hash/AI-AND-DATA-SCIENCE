def check_score(score):
    if score >= 60:
        return "You have passed the exam."
    else:
        return "You have failed the exam."

print(check_score(75))   # Passed
print(check_score(45))   # Failed
