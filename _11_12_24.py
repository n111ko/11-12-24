# ##### Ülesanne 2 #####
# while True:
#     try:
#         A = int(input("Sisesta A: "))
#         break
#     except:
#         print("On vaja naturaalne arv")
# summa = 0
# if A > 0:
#     for i in range(1, A+1, 1):
#         summa += i #summa = summma + i
#         print(f"{i}. samm summa = {summa}")
#     print(f"Vastus {summa}")
# ######################

# ##### Ülesanne 3 #####
# p = 1
# for j in range(8):
#     while True:
#         try:
#             arv = float(input(f"Sisesta {j+1} arv: "))
#             break
#         except:
#             print("On vaja reaalne arv")
#     if arv > 0:
#         p *= arv
#     else:
#         print("Korrutame arvud ainult rohkem kui 0")
#     print(f"{j+1}. samm korrutis = {p}")
# print(f"Lõpputulemus on {p}")
# ######################

# ##### Ülesanne 4 #####
# for i in range(10, 21, 1):
#     print(i**2, end="; ")
# ######################

# ##### Ülesanne 16 #####
# for j in range(1, 10):
#     for i in range(1, 10):
#         if i == j:
#             print(j, end=" ")
#         else:
#             print("0", end=" ")
#     print()

# print()
# #######################

# ##### Ülesanne 15 #####
# for read in range(10):
#     for veerg in range(10):
#         print(read, end=" ")
#     print()
# print()
# #######################

# ##### Ülesanne 1 #####
# for j in range(16):
#     while True:
#         try:
#             arv = int(input(f"Sisesta {j+1} arv: "))
#             break
#         except:
#             print("On vaja naturaalne arv")
# print()
# print("Kõik arvud on naturaalsed.")
# ######################

##### Ülesanne 18 #####
#Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.
for i in range (20, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
#######################
