def newF(limit):
    for i in range(0, limit+1):
        if i % 2 == 0 :
            print(f"{str(i)}: even")
        else:
            print(f"{str(i)}: odd")

newF(5)