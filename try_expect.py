def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: wrong input")
        if ok:
            ok = min <= value <= max
        if not ok:
            print("Error: the value in not within perimitted range ({} ... {})".format(min, max))
    return value


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
