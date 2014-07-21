p1 = [1,7,7,3]
p2 = [-18,12,2,5]
p3 = [1,1,2,2]
p4 = [3,3,4,4]
def is_intersect(P1, P2):
    x1, y1, x2, y2 = P1
    a1, b1, a2, b2 = P2
    if a1<=x1<=a2 or x1<=a2<=x2 and b1<=y1<=b2 or y1<=b1<=y2:
        return True
    else:
        return False
