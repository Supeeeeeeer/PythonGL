width = 8
height = 5
cw = 1
ch = 1
n = ""

sqr = 0

NAME = "PythonGL"

def area(w: int, h: int):
    sqr = w*h
    return sqr

area(width, height)

sqr = area(width, height)


for i in range(sqr):
    n+="x"
    if cw  == width:
        n+="\n"
        cw = 1
    else:
        cw += 1
        
print(n)