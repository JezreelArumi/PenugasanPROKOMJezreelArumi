# 5.8 Hello Admin
usernames = ['natha', 'naila', 'queena', 'al', 'jeva']

for username in usernames:
    if username == 'jeva':
        print("Hello jeva, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")