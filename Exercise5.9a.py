# 5.9 No Users (a): hello_admin.py with a check, list has users
usernames = ['natha', 'naila', 'queena', 'al', 'jeva']

if usernames:
    for username in usernames:
        if username == 'jeva':
            print("Hello jeva, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")