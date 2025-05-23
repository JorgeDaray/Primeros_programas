abecedario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
              "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
              "n": 14, "ñ": 15, "o": 16, "p": 17, "q": 18, "r": 19, "s": 20,
              "t": 21, "u": 22, "v": 23, "w": 24, "x": 25, "y": 26, "z": 27}

s = input(str("introduce una cadena en minuscuclas :"))
inicio =0
final =0
inicio_abecedario = 0
final_abecedario = 0
for i in range(len(s)):
    if i == 27 or abecedario[str(s[i])] >= abecedario[str(s[i - 1])]:
        final = i
    elif s:
        inicio = i
        final = i
    else:
        if s.isspace():
            print("no se valen espacios.")
    if (final - inicio) > (final_abecedario - inicio_abecedario):
        inicio_abecedario, final_abecedario = inicio, final
print("la subcadena mas larga es:", s[inicio_abecedario:final_abecedario + 1])

