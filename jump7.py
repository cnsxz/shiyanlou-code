a = 0
while a < 100:
    a += 1
    if a % 7 == 0: ##a?7??????
        continue
    if a-a//10*10 == 7: ##?7???
        continue
    if a >= 70 and a <80: ##70~79
        continue
    print(a)


