def num_of_feet(chicken, cow):
    return ((chicken * 2) + (cow * 4))

chicken = float(input("How many chicken are there in the farm?"))
cow = float(input("How many cows are there in the farm?"))

feet = num_of_feet(chicken, cow)

print(f"The number of feet is {feet}")