end = 0
ok = False
lst = []
while end < 9:

    i = list(input("Enter {} line of sudoku: ".format(end+1)))
    end += 1
    lst.append(i)
check_list = [chr(x + ord('0')) for x in range(1, 10)]
trans_lst = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
for rows in lst:
    if sorted(rows) == check_list:
        ok = True
    else:
        ok = False
        break
if ok:
    for cols in trans_lst:
        if sorted(cols) == check_list:
            ok = True
        else:
            ok = False
            break
if ok:
    for
if ok:
    print("ok")
else:
    print("not ok")