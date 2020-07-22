import numpy as np



def get_intersections(person,q):
    x,y,d = person
    if (d == "S"):
        return [(xx, yy) for yy in range(0,y) for xx in range(0, x)]
    if (d == "N"):
        return [(xx, yy) for yy in range(y+1,q+1) for xx in range(0, x)]
    if (d == "W"):
        return [(xx, yy) for xx in range(0,x) for yy in range(0, y)]
    if (d == "E"):
        return [(xx, yy) for xx in range(x+1,q+1) for yy in range(0, y)]


    
    

def find_crepes(people, q):
    intersections = np.zeros((q+1,q+1))
    print ("here")

    for person in people:
        for (x,y) in get_intersections(person,q):
            if not intersections[x][y]:
                intersections[x][y] = intersections[x][y] + 1

    max_headings = np.amax(intersections)
    where = np.where(intersections == max_headings)
    zipped = np.dstack(where)[0]

    

    most_sw = None

    for inters in zipped:
        if most_sw is None:
            most_sw = inters
        elif inters[0] < most_sw[0]:
            most_sw = inters
        elif inters[0] == most_sw[0] and inters[1] < most_sw[1]:
            most_sw = inters


    return most_sw
    




# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    
    
    p, q  = [int(s) for s in input().split(" ")]
    people = []

    for k in range(p):
        (x,y,d) = input().split(" ")
        person = (int(x), int(y), d)
        people.append(person)

    crepe = find_crepes(people, q)

    

    print("Case #{}: {} {}".format(i, crepe[0], crepe[1]))
    # check out .format's specification for more formatting options
