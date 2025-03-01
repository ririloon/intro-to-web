class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user1 = User("john_doe", "john@example.com")
print(user1.email)

del user1.email
del user1

# print(user1.username)