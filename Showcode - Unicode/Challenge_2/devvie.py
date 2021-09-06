class Solution:

    def devvie(self, input):
        coordinate = (0,0)
        direction = "N"
        output = 0
        for character in input:
            if character == "F":
                if direction == "N":
                    coordinate = (coordinate[0],coordinate[1]+1)
                elif direction == "E":
                    coordinate = (coordinate[0]+1,coordinate[1])
                elif direction == "S":
                    coordinate = (coordinate[0],coordinate[1]-1)
                else:
                    coordinate = (coordinate[0]-1,coordinate[1])
            elif character == "L":
                if direction == "N":
                    direction = "W"
                elif direction == "E":
                    direction = "N"
                elif direction == "S":
                    directrion = "E"
                else:
                    direction = "S"
            elif character == "R":
                if direction =="N":
                    direction = "E"
                elif direction == "E":
                    direction = "S"
                elif direction == "S":
                    direction = "W"
                else:
                    direction = "N"
            else:
                pass
    
        if coordinate == (0,0):
            output = 0
        elif coordinate[0] == 0 and coordinate[1] < 0:
            if direction == "N":
                output = -coordinate[1]
            elif direction in ("E","W"):
                output = 1 - coordinate[1]
            else:
                output = 2 - coordinate[1]
        elif coordinate[0] == 0 and coordinate[1] > 0:
            if direction == "N":
                output = 2 + coordinate[1]
            elif direction in ("E","W"):
                output = 1 + coordinate[1]
            else:
                output = coordinate[1]
        elif coordinate[0] < 0 and coordinate[1] == 0:
            if direction in ("N","S"):
                output = 1 - coordinate[0]
            elif direction == "E":
                output = -coordinate[0]
            else:
                output = 2 -coordinate[0]
        elif coordinate[0] > 0 and coordinate[1] == 0:
            if direction in ("N","S"):
                output = 1 + coordinate[0]
            elif direction == "E":
                output = 2 + coordinate[0]
            else:
                output = coordinate[0]
        elif coordinate[0] < 0 and coordinate[1] < 0:
            if direction in ("N","E"):
                output = 1 - coordinate[0] - coordinate[1]
            else:
                output = 2 - coordinate[0] - coordinate[1]
        elif coordinate[0] > 0 and coordinate[1] < 0:
            if direction in ("N","W"):
                output = 1 + coordinate[0] - coordinate[1]
            else:
                output = 2 + coordinate[0] - coordinate[1]
        elif coordinate[0] < 0 and coordinate[1] > 0:
            if direction in ("S","E"):
                output = 1 - coordinate[0] + coordinate[1]
            else:
                output = 2 - coordinate[0] + coordinate[1]
        elif coordinate[0] > 0 and coordinate[1] > 0:
            if direction in ("S","W"):
                output = 1 + coordinate[0] + coordinate[1]
            else:
                output = 2 + coordinate[0] + coordinate[1]
    
        return(output)
