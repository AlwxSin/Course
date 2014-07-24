P1 = [int(input('Please, input coordinates of first rectangle\nx1 coordinate\n')), int(input('y1 coordinate\n')), int(input('x2 coordinate\n')), int(input('y2 coordinate\n'))] # First rectangle coordinates
P2 = [int(input('Please, input coordinates of second rectangle\nx1 coordinate\n')), int(input('y1 coordinate\n')), int(input('x2 coordinate\n')), int(input('y2 coordinate\n'))] # Second rectangle coordinates
def is_intersect(P1, P2):
    inter = 0 # По этой переменной определим, пересекутся ли прямоугольники
    for x in range(P1[0], P1[2]+1):
        for y in range(P1[1], P1[3]+1):
            if x in range(P2[0], P2[2]+1) and y in range(P2[1], P2[3]+1):
                inter = 1
                break
    if inter == 1:
        print("Yep, they're intersecting")
        return True
    else:
        print("Fail =(")
        return False
