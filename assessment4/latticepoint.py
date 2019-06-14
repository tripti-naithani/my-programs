def N(point):
    point[1] += 1
    return point

def S(point):
    point[1] -= 1
    return point
    
def E(point):
    point[0] += 1
    return point

def W(point):
    point[0] -= 1
    return point

def NE(point):
    point[0] += 1
    point[1] += 1
    return point

def NW(point):
    point[0] -= 1
    point[1] += 1
    return point
    
def SE(point):
    point[0] += 1
    point[1] -= 1
    return point

def SW(point):
    point[0] -= 1
    point[1] -= 1
    return point


def NESW(point, step):
    for i in range(0, step[0]):
        point = step[1] + (point)  #example: N(point) or S(point), calling to a function will occur

def terminus(point, steps):
    for step in steps:
        if (len(step) ==  2):
            point = NESW(point, step)
        else:
            point = NESW(point, step)
            
            
            
        





x = int(input("x:"))
y = int(input("y:"))
steps = list(map(str, input("steps:").split()))
print(terminus([x, y], steps))






