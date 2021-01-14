#Tuples
#note:Immutable ordered collection (sequence)

my_tuple = (1,2,3)
this_is_valid = 4, 5, 6
single_item = (True,)

coordinates = (12, -99, 8)
x = coordinates[0]
y = coordinates[1]
z = coordinates[5]

#Tuple unpacking
x, *y = coordinates
print(x)
print(y)

#Sets 
#Mutable, unordered, unique, item collection 
computers = {"Macintosh", "Dell", "Lenovo", "Asus"}
ages = {12,22,12}
print(ages)

tea_types= {"green", "masala chai"}
tea_types.add("oolong")
tea_types.add("black")
tea_types.add("jasmine")
tea_types.add("matcha")
tea_types.add("green")

#list
#ordered, mutable, collection (sequence)

my_list = []

cars = ["Volkswagen", "Ferrari", "Ford", "Tesla"]

some_data = [12, "abc123", True, [],("windows", "linux")]

some_data[2]
#List methods

some_list = [99,33,66,33]
some_list.append(123) #add one item to the end 
some_list.extend([88, 74]) #Add items from another list to the end 
some_list.insert(2,"a thing") # Add an item at a specific index
some_list.remove(33) # Remove the first instance of a given item
some_list.pop() # Remove and return the item at given index (end default)
some_list.clear() # Removes all from list 
some_list.index("a thing") # Index of the first instance of the item 
#count
#sort
#reverse
#copy

purchases = [
    33.78,
    5.99,
    533.32,
    3.50,
    1300.00,
    19.98,
    44.44,
    66.00,
    17.38,
]

last_five = [purchases[5], 
    purchases[6], 
    purchases[7],
    purchases[8],
    purchases[9]

]
                    #[start: stop: step]
last_five = purchases[5:8:2]
purchases[-1]

#Dictionaries(an objec literal),mutable

person= { 
    "name": "Guido van Rossum",
    "age": 64,
    "accomplishments":[
        "invented Python",
        "Awarded for the Advancement of Free Software"
    ],
    (0,2): "what"

}

print (person["age"])
print (person[(0,2)])


}
user = {
    "name": {
        "first": "Grace",
        "last": "Hopppppper"
    },

  "rank": "Rear Admiral (lower half)",
    "service_year":79,
    "cool_factor": 9001
}
user ["rank"]
user["name"]["last"]

user["cool_factor"] = 1000000

#Goal:Quote a fact about her
quote = "The most important thing I've done other than building the compiler, is training young people"
user["quote"]= quote
print(user)