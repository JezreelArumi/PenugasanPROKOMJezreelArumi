# 5.9 No Users (b): all usernames removed, so the list is empty
usernames = []

if usernames:
    for username in usernames:
        if username == 'natha':
            print("Hello natha, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")