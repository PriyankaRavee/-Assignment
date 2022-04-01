def function(x):
    if x == 2:
        return [2]
    elif x == 3:
        return [2,3]
    else:
        d = [2,3]
        for i in range(2, x):
            for k in range(2, i-1):
                if i%k==0:
                    break

                else:
                    d.append(i)
                    break

        return d

def returnage(x):
    return True if x >= 21 else False


print(function(2))
print(returnage(20))
