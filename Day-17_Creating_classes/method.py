class User_Add:
    def __init__(self ,id ,username):
        print("This is the constructor method")
        self.id = id
        self.username = username
        self.followers = 0

    def follow(self, user): #this is a method
        user.followers += 1
        user.following = self.followers

user_a = User_Add(1,"John")
user_b = User_Add(2,"Levis")
print(user_a.id)
print(user_b.username)
user_b.follow(user_a)#here we're using the method
print(user_a.followers)
print(user_b.followers)
