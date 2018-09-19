dict = {"María": 21, "Dani": 21, "Mike": 23}
name = input("Dime un nombre:")
print(dict[name] if name in dict.keys() else "No tienes amigos :(")
