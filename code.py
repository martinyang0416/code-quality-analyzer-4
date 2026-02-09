import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def polygon_area(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[i][1] * points[j][0]
    return abs(area) / 2.0

def sutherland_hodgman(subject_polygon, clip_edge):
    def inside(p):
        a, b, c = clip_edge
        return a * p[0] + b * p[1] + c >= 0

    def compute_intersection(s, e):
        a, b, c = clip_ed