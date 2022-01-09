#Create a list of colors from comma-seperated color names entered by user.Display first and last color

colours = input("enter the colours:")
print(colours.split(","))
print("first colour:", colours.split(",")[0])
print("last colour:", colours.split(",")[-1])