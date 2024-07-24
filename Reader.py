import os
Path = os.path.dirname(os.path.abspath(__file__))+"/"

f = open(os.path.join(Path,"Code.txt"), "r")
key = input("Key >> ")
lines = f.readlines()
for line in lines:
    line = int(line.strip())
    print(chr(int(line)-int(key)), end="")
print("\n해독 완료")
f.close()
a = input("\n엔터로 작업 완료...")
while a != "":
    a = input("...")