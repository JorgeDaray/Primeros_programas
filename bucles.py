s = input("Introduce una cadena en minusculas: :")
palabras = 0
for i in range(len(s)):
    if i < len(s)-2:
        if s[i] == "b" and s[i + 1] == "o" and s[i + 2] == "b":
            palabras += 1
print("tu palabra tiene",palabras, "bob")