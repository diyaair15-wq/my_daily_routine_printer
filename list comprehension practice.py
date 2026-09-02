subjects = ["Math", "Physics", "Chemistry", "Biology", "History"]
grades = [85, 92, 78, 65, 95]

short_subjects = [sub for sub in subjects if len(sub) <= 5]
upper_subjects = [sub.upper() for sub in subjects]
passed_subjects = [sub for sub, grade in zip(subjects, grades) if grade >= 75]
subject_status = ["Pass" if grade >= 75 else "Fail" for grade in grades]

print(f"Original: {subjects}")
print(f"Short names: {short_subjects}")
print(f"Uppercase: {upper_subjects}")
print(f"Passed: {passed_subjects}")
print(f"Status: {subject_status}")
