import random
X = 0

def function(speed):
    global X
    if speed > 70:
        X += 1
    if X == 12:
        print("Licence cancelled")
        return False

x = []
for i in range (0,50):
    x.append(random.randint(20,100))


for i in x:
    d = function(i)
    if d == False:
        break