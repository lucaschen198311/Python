##1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
##Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]= 15
print(x)
##Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)
##In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
##Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

##2.Iterate Through a List of Dictionaries
def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name - {students[i]['first_name']} , last_name - {students[i]['last_name']}\n")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

##3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, arr):
    for i in range(len(arr)):
        print(arr[i][key_name])
iterateDictionary2('first_name', students)

##4.Iterate Through a Dictionary with List Values
def printInfo(dict_name):
    for key in dict_name.keys():
        print(f"{len(dict_name[key])} {key.upper()}")
        for i in range(len(dict_name[key])):
            print(dict_name[key][i])
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
