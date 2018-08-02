#! python3

# mapTest

# a = room number
# b = choice number

locations = [
    ["Room 1",["Room 2","Room 3"]],
    ["Room 2",["Room 3","Room 1"]],
    ["Room 3",["Room 1","Room 2"]]
    ]

location = locations[0][0]

while True:

    print("You are in " + location)

    for i in range(len(locations)):
        if location in locations[i]:
            print("Yes")
            a = locations[i].index(location) # this is only returning 0 for some reason
            print(a)

    print("You can go:")
    for i in range(len(locations[a][1])):
        print("[" + str(i+1) + "] " + locations[a][1][i])
    b = int(input())-1
    choice = locations[a][1][b]


    for i in range(len(locations)):
        if choice in locations[i][a]:
            c = locations[i][a].index(choice)
            location = locations[a][1][c]
    startLocation = location

            
