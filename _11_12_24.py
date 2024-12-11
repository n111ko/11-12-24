##### Ülesanne 2 #####
while True:
    try:
        A = int(input("Sisesta A: "))
        break
    except:
        print("On vaja naturaalne arv")
summa = 0
if A > 0:
    for i in range(1, A+1, 1):
        summa += i #summa = summma + i
        print(f"{i}. samm summa = {summa}")
    print(f"Vastus {summa}")
######################

##### Ülesanne 3 #####
p = 1
for j in range(8):
    while True:
        try:
            arv = float(input(f"Sisesta {j+1} arv: "))
            break
        except:
            print("On vaja reaalne arv")
    if arv > 0: p *= arv
    print(f"{j+1}. samm korrutis = {p}")
print(f"Lõpputulemus on {p}")
######################