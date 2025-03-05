import map_data as m
tiles=[]
data = m.data()
for line in data:
    row=[]
    for tile_number in line:
        row.append(int(tile_number))
    tiles.append(row)
y2=[]
x2=[]
n1=0
n2=0
for y1 in tiles:
    for x1 in y1:
        if x1==4:
            y2.append(n2*64)
        if x1 ==3:
            x2.append(n1*64)
        n1 = n1 + 1
    n1=0
    n2 = n2 + 1
def list_y():
    return y2
def list_x():
    return x2
def allow_x(x):
    if x in range(384,448-52) or x in range(3008,3008+448-384-52):
        return False
    else:
        return True
def allow_not_y(y):
    for i in range(len(y2)):
        if y in range((y2[i])-57,(y2[i])+14):
            return True
def allow_not_x(x):
    for i in range(len(x2)):
        if x in range(x2[i]+54,x2[i]):
            return True
def allow_x_y(x,y):
    for i in range(len(x2)):
        if x not in range(384,448-52) and y in range((y2[i])-57,(y2[i])+64):
            return True
