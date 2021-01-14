#For Loops
students = ["Jane", "John", "Kenn", "Sophia"]

#for variabel in the list
for student in students: 
    print(student)

state = {
    "name": 'Wyoming',
    "capital": "Cheyenne",
    "bird":"Western meadwlark",
    "highest-point": 13804
}


#dict.values() -> each value associated to a key in a list
#dict.items() -> Tuple represenation of each key and value pair
#dict.keys() -> gives just the keys 

for item in state :
    #print(item)
    print(state[item])

for item in state.values():
    print(item)

for item in state.items():
    value = item [1]
    key = item[0]         
     #OR
for key, value in state.items(): 
    print(key, value)

stations = ["Zarya", "Skylab", "Mir"]

for index, value in enumerate(stations):
    print(f"The {value} station resides at position {index}") 

#While Loop

x = 0
while x < 10 :
    print("The loop is still going")
    x +=1

print("The loop is done!")

#Menu
# while True:
#     choice = input("Choose one:1) Keep going. 0) Exit" )
#     if choice == "1":
#         print("The program will continue")
#     elif choice == "0":
#         print("Goodbye, Dave")
#         break
#     else:
#         print("I'm sorry, I cannot do that Dave")

# Loop Control 

options = ["up", "down", "left", "right"]

for selection in options:
    if selection == "lefty":
        print("Nope")
        break
else:
    print("When does this fire?")

for selection in options:
    if selection == "down":
        print("The air gets thicker")
        continue
    print("You have moved in the dungeon")