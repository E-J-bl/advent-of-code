#codes is a little sh*t but at least i used functions 
data='''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split(',')
boxes=[[] for i in range(256)]
print(boxes)
def convert(data):
  sum=0
  for i in data:
    sum+=int(ord(i))
    sum*=17
    sum=sum%256
  return sum
total=0
def add(data):
    box=convert(data[0:data.index('=')])
    inside=False
    placeinside=0
    for lens in boxes[box]:
      if lens[0]==data[0:data.index('=')]:
        inside=True
        placeinside=boxes[box].index(lens)
    if inside:
      boxes[box][placeinside]=[data[0:data.index('=')],data[-1]]
    else:
      boxes[box].append([data[0:data.index('=')],data[-1]])

def sub(data):
  box = convert(data[0:data.index('-')])
  ind=[]
  for da in boxes[box]:
    if da[0]==data[0:data.index("-")]:
      ind.append(da)
  print('ind:',ind)
  if len(ind)!=0:
    boxes[box].remove(ind[0])
for section in data:
  total+=convert(section)
  if section[-2]=='=':
    add(section)
    print('add',boxes)
  if section[-1]=='-':
    sub(section)
    print('sub:',boxes)
score=0
for index,bos in enumerate(boxes):
  for ind,lens in enumerate(bos):
    score+=int(lens[1])*(index+1)*(ind+1)
    print(score)
print(boxes)
print(total)
print(score)
