def mysplit(strng):
    if strng.isspace() or strng == '':
        return list()
    lst = []
    new_strng = ''
    inword = not strng[0].isspace()
    for i in strng:
        if inword:
            if not i.isspace():
                new_strng += i
            else:
                lst.append(new_strng)
                inword = False
        else:
            if not i.isspace():
                inword = True

                new_strng = i
            else:
                pass
    if inword:
        lst.append(new_strng)
    return lst
    print(new_strng)

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
