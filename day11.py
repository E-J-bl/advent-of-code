space='''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

space=space.split('\n')
for index,layer in enumerate(space):
    space[index]=list(layer)
print("pass1")
print(space)
apendset=[]
for index,layer in enumerate(space):
    if set(list(layer))=={'.'}:
        print(index)
        apendset.append(index+len(apendset))
for dup in apendset:
    #for part b just add a for loop here to 1000
    space.insert(dup,list('.'*len(space[0])))
colm=[]
for col in range(len(space[0])):
    temp=[]
    for layer in space:
        row=layer
        temp.append(row[col])
    colm.append(temp)
hold=[str(counter) for counter in range(len(space[0]))]
print(' ',hold)
for index,row in enumerate(space):
    print(index,row,1)
print(colm,'!')
counter=0
for col,content in enumerate(colm):
    if set(content)=={'.'}:
        print('passA',col,col+counter)
        for index,row in enumerate(space):
           #add a for loop here for part b as well
            row.insert(col+counter,'.')
        
            space[index]=row
        counter+=1

starpoint=[]
posmove=[(0,1),(0,-1),(1,0),(-1,0)]
for row,content in enumerate(space):
    for col,point in enumerate(content):
        if point=='#':
            starpoint.append([row,col])   
print(starpoint)       
sum=0
for i in range(len(starpoint)):
    for r in range(i+1,len(starpoint)):
        sum+=abs(starpoint[i][0]-starpoint[r][0])+abs(starpoint[i][1]-starpoint[r][1])
        print(sum)
            
            
        
print("pass3")
for layer in space:
    print(layer)
    
print('part1',sum)
