#

for i in range(1,11):
    for j in range(2, i):
        if i % j == 0:
            # print(f"{i} is not prime")
            pass
            break
    else:
        print(i)