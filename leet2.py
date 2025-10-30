# palindrom?

x = "11233211"
i=0
palindrom = False
for j in range(len(x)-1,-1,-1):
    if x[i] == x[j]:
        i +=1
        palindrom = True
    else:
        palindrom = False
        break


if palindrom:
    print("palindrom")
else:
    print("not palindrom")