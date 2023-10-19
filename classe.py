#How to create your own Class in Python
"""Class is a Blueprint (from arquicteture)
Classes uses PascalCase.
camelCase
snake_case - for variables and functions in Python
"""

class CarCamshaftPulley:
  pass
  

class User:
  pass
  

user_1 = User()


#Working with Attributes, Class Constructor and the __init__() Function
#Use of the constructor to initialize
class User:
  pass
  

user_1 = User()
user_1.id = "234"
user_1.username = "angela"

print(user_1.username)

user_2 = User()
#attribute id
user_2.id = "333"
#attribute username
user_2.username = "Jack"

"""
class Car:
    def __init__(self):
      #initialise attributes
"""

class User:

  def __init__(self, user_id, username):
    #attributes in constructor for 
    self.id = user_id
    self.username = username
    self.followers = 0
    print("user created")

user_1 = User("001", "Angela")

print(user_1.username)
print(user_1.followers)


#Adding Methods to a Class
"""
class Car:
    def __init__(self):
      #initialise attributes
"""

class User:

  def __init__(self, user_id, username):
    #attributes in constructor for 
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0
    print("user created")

    
  def follow(self, user):
    user.followers += 1
    self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(user_1.username)
print(user_1.following)
print(user_1.followers)
print(user_1.username)
print(user_2.following)
print(user_2.followers)

