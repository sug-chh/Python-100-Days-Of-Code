class User:
    def __init__(self, user_id, username):
        print("new user created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User('001', 'Sugam')
print(user1.id, user1.username)

user2 = User('002', "Jacob")
print(user2.id, user2.username)

user1.follow(user2)

print(user1.followers, user2.followers, user1.following, user2.following)
