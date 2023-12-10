from typing import List
from termcolor import colored
from colorama import Fore, Back, Style


class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)




mazes = open("maze.txt", "r")
out=open("out.txt","w")
maze = mazes.readlines()
direction = {"|": [(-1, 0), (1, 0)], "-": [(0, 1), (0, -1)], "L": [(-1, 0), (0, 1)], "J": [(-1, 0), (0, -1)],
             "7": [(1, 0), (0, -1)], "F": [(1, 0), (0, 1)],".":[(0,0),(0,0)],"S":[(0,0),(0,0)]}
card = {(1, 0): "down", (-1, 0): "up", (0, 1): "right", (0, -1): "left",(0,0):"stay"}
arrder = [(1, 0), (-1, 0), (0, 1), (0, -1)]
unlooped=True
start=[]
for i in range(len(maze) - 1):
    maze[i] = maze[i][0:-1]
maze = [list(y) for y in maze]
for y in maze:
    if "S" in y:
        start: list[int] = (maze.index(y), y.index("S"))
#print("start",start)
defspot=[start]
counter=0

pospoits=[]
polet=[]
letlink=[]
for direc in arrder:
    pospoits.append((defspot[-1][0]+direc[0],defspot[-1][1]+direc[1]))
for point in pospoits:
    polet.append(maze[point[0]][point[1]])
for letter in range(len(polet)):
    temp=(pospoits[letter][0]+direction[polet[letter]][0][0],pospoits[letter][1]+direction[polet[letter]][0][1])
    temp2=(pospoits[letter][0]+direction[polet[letter]][1][0],pospoits[letter][1]+direction[polet[letter]][1][1])
    if 0 <= temp[0] < len(maze) and 0 <= temp[1] < len(maze[0]):
        letlink.append(temp)
    else:
        letlink.append(None)

    if 0 <= temp2[0] < len(maze) and 0 <= temp2[1] < len(maze[0]) :
        letlink.append(temp2)
    else:
        letlink.append(None)
#print("definiate",defspot)
#print("possible",pospoits)
#print("possible lettet",polet)
#print("possible checkers",letlink)

for pos in range(len(letlink)):
    if letlink[pos]==defspot[-1] and pospoits[pos%len(pospoits)] not in defspot:
        defspot.append(pospoits[pos//2])
counter=0
while defspot[-1]!= defspot[0]:
    for pos in range(len(direction[maze[defspot[-1][0]][defspot[-1][1]]])):
        #print("now",defspot[-1])
        #print("nowletter",maze[defspot[-1][0]][defspot[-1][1]])
        #print("moves",direction[maze[defspot[-1][0]][defspot[-1][1]]])
        #print("chosen",direction[maze[defspot[-1][0]][defspot[-1][1]]][pos])
        temp=(defspot[-1][0]+direction[maze[defspot[-1][0]][defspot[-1][1]]][pos][0],defspot[-1][1]+direction[maze[defspot[-1][0]][defspot[-1][1]]][pos][1])
        #print("next",temp)
        if temp not in defspot:
            defspot.append(temp)
            #print("shift",direction[maze[defspot[-1][0]][defspot[-1][1]]][pos])
        if temp==defspot[0] and len(defspot)>2:
            defspot.append(temp)
            #print(pos)
    counter+=1
    if counter>10000:
        break
#print(counter)
#print(defspot)
#print("middle",len(defspot)//2)
#print("spot",defspot[(len(defspot)//2)-1])

for line in range(len(maze)):
    lenw = []
    for letter in range(len(maze[0])):

        if (line,letter) in defspot:
            temp= maze[line][letter]
            lenw.append(temp)

        else:
            lenw.append(".")

    for letter in lenw:

        out.write(letter)
    out.write("\n")
print("chain len",len(defspot))
print("start",defspot[0])
print("end",defspot[-1])
mazes.close()



#this is part 1
