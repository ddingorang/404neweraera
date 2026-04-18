a = int(input(""))
bagnum = 0

while True :
    if a % 5 == 0 :
        bagnum += a/5
        break
    else : 
        bagnum += 1
        a -= 3
        if a < 0 : 
            bagnum = -1
            break

print("{:g}".format(bagnum))