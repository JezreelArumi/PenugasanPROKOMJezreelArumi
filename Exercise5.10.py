# 5.10 Checking Usernames
current_users = ['natha', 'naila', 'queena', 'al', 'jeva']
new_users = ['james', 'juhoon', 'martin', 'sean', 'keonho']

# Lowercase copy, so the comparison ignores capitalization.
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user}, that username is taken. "
              "Please enter a new username.")
    else:
        print(f"Good news, {new_user}, that username is available.")