"""

Write a procedure that curates a new list of individuals that like to hike or ride motorcycles. The structure of a user profile is this:
User:
  - Name [STRING]
  - Age [INTEGER > 0] 
  - eMail  [STRING]
  - interests  [LIST]
       - Interests contains strings that describe the users interests, ranging from volleyball to wakeboarding.

Use this test data to verify your procedure works

"""
users = [
  {
    "name": "Shirley Hickman",
    "age": 43,
    "email": "shickman123@email.com",
    "interests": [
      "biking",
      "computers",
      "security"
    ]
  },
  {
    "name": "Arthur McInnis",
    "age": 23,
    "email": "amdub12@mail.com",
    "interests": [
      "whiskey",
      "motorcycles",
      "hiking",
      "fireworks"
    ]
  },
  {
    "name": "Leticia Green",
    "age": 36,
    "email": "greenthumbl.36@corpo.org",
    "interests": [
      "motorbikes",
      "books"
    ]
  }
]

# HINT: Your procedure should select both "Arthur McInnis" and "Leticia Green", but not "Shirley Hickman"

#for user in users: print(user)

#users [1]
#print(users)
#print (users["interests"]) 
#for interests in users.interests():
    #print(interests)
#for item in users.item():
 #   value = item[1]
#    key = item[0]


found = []
to_check = [
"backpacking",
"hiking",
"camping",
"motorcycles",
"motorbikes"
]

for user in users:
    interest_match = False
    for interest in user["interests"]:
        if interest in to_check:
            interest_match = True
    if interest_match:
        found.append(user)
    print(found)        

