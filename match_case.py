liczba = int(input("podaj liczbe: "))

if liczba == 0:
    print("jestes zerem")
elif liczba < 0:
    print("jestes liczbą ujemną")
elif liczba > 0:
    print("jestes liczba dodatnia")
else:
    print("what are you?")

zawod = int(input("podaj zawod: "))

match zawod:
    case "zolnierz":
        print("jestes zolnierzem")
    case "policjant":
        print("jestes policjantem")
    case "nauczyciel":
        print("jestes nauczyciel")
