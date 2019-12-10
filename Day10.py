import math

input = """#..#.#.###.#...##.##....
.#.#####.#.#.##.....##.#
##..#.###..###..#####..#
####.#.#..#....#..##.##.
.#######.#####...#.###..
.##...#.#.###..###.#.#.#
.######.....#.###..#....
.##..##.#..#####...###.#
#######.#..#####..#.#.#.
.###.###...##.##....##.#
##.###.##.#.#..####.....
#.#..##..#..#.#..#####.#
#####.##.#.#.#.#.#.#..##
#...##.##.###.##.#.###..
####.##.#.#.####.#####.#
.#..##...##..##..#.#.##.
###...####.###.#.###.#.#
..####.#####..#####.#.##
..###..###..#..##...#.#.
##.####...##....####.##.
####..#..##.#.#....#..#.
.#..........#..#.#.####.
###..###.###.#.#.#....##
########.#######.#.##.##"""

def getAngle(y2, y1, x2, x1) :
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def getDistance(y2, y1, x2, x1) :
    return abs(y2 - y1) + abs(x2 - x1)

def getAsteroids(x, y) :
    asteroids = {} # create a dictionary of 'angles' to other asteroids from this location
    for ii in range(height) : # for each x,y location
        for jj in range(width) :
            if (ii != x or jj != y) and aMap[ii][jj] == '#' : # if we are not on the same square and theres an asteroid
                angle = getAngle(jj, y, ii, x) # calc the angle to the asteroid
                dist = getDistance(jj, y, ii, x) # get the distance to the asteroid

                if angle not in asteroids :
                    asteroids[angle] = (ii,jj) # add it as we cant see another asteroid on this angle
                elif getDistance(asteroids[angle][1], y, asteroids[angle][0], x)  > dist : # if we already 'see' and asteroid but its further away then add the new one
                    asteroids[angle] = (ii, jj)
    return asteroids


lines = input.split('\n')
width = len(lines[0])
height = len(lines)

aMap = [['.' for i in range(width)] for j in range(height)] # create empty 2d array
locs = {} # will contain every x,y point and a dictionary of all visible asteroids by angle

# fill the 2d array
for i in range(height) :
    for j in range(width) :
        aMap[i][j] = lines[i][j]

for i in range(height) : # for each x,y location
    for j in range(width) :        
        locs[(i,j)] = getAsteroids(i,j) ## set the dictionary for this x,y location

highestKey = list(locs.keys())[0]

# find the location with the most visible asteroids
for k, val in locs.items() :    
    if len(locs[highestKey]) < len(val) :        
        highestKey = k

print(highestKey)
print(len(locs[highestKey]))
