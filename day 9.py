data=open("input.txt","r")
data=data.readlines()


for i in range(len(data)-1):
    data[i]=data[i][0:-1]
data=[y.split(" ") for y in data]

longstor=[]
dif=[]
for level in data:
    dif=[]
    dif.append(level)
    while len(set(dif[-1])) > 1:
        temp=[]
        for i in range(len(dif[-1])-1):
            temp.append(int(dif[-1][i+1])-int(dif[-1][i]))
        dif.append(temp)


    longstor.append(dif)

#print(longstor)
hold=[]
for level in longstor:
    temp=[int(level[0][0])]
  #for part a change it to a version where it just takes the last value of every elements in level 
    for step in range(len(level[1:])):
        temp.append(level[step+1][0])
    #print(temp)
    sume=0
    beg = temp[0]
  # and remove this to get to A
    for et in range(len(temp[1:])):
        print(temp[-(et+1)])
        temp[-(et+2)]-=temp[-(et+1)]
    #print(temp)

    hold.append(temp[0])

print(hold)
print(sum(hold))
