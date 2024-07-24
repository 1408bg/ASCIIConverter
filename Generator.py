import random
import os
Path = os.path.dirname(os.path.abspath(__file__))+"/"

s = open(os.path.join(Path+"setting.txt"),"r")
rd = s.readlines()
k1 = int(rd[0].strip())
k2 = int(rd[1].strip())
newL = True if rd[2] == 'true' else False
s.close()

key = random.randint(k1,k2)
f = open(Path+"Code.txt","w")
while True:
    main = input(">> ")
    if main == "-1":
        break
    for i in main:
        f.write(str(ord(i)+key)+"\n")
    print("입력 성공")
    if newL:
        f.write(str(10+key)+"\n")
print("종료\n\n")
f.close()
print("Key : "+str(key))
a = input("\n엔터로 작업 완료...")
while a != "":
    a = input("...")