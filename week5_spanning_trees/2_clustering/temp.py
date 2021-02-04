ans=[]
i=1
f = open("ans.txt", "w")
f.write("[")
while True:
    if i**2<10**9:
        f.write(str(i**2)+",")
    else:
        break
    i+=1
f.write("]")
