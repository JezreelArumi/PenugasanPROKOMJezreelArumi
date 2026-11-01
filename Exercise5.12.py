# 5.12 Styling if Statements
# Review of this chapter's programs: every comparison operator has one
# space on each side (age < 4, not age<4), like the examples below.
age = 12

if age < 4:
    print("Free admission.")
elif age >= 4 and age < 18:
    print("Admission is $25.")
else:
    print("Admission is $40.")