
def distance(p1, p2):
    return ((p1[0] - p2[0])** 2 + (p1[1] - p2[1])** 2) ** 0.5
def brute_force(points):
    min_distance = float('inf')
    min_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_distance:
                min_distance = d
                min_pair = (points[i], points[j])
    return min_distance, min_pair

def closet_pair_recursive(points_x, points_y):

    if len(points_x) <= 3:
        return brute_force(points_x)
    
    # Compute separation line L
    mid = len(points_x) // 2
    L = points_x[mid][0]

    # Get the left and right subset
    left_points_x = points_x[:mid]
    right_points_x = points_x[mid:]

    left_points_y = [p for p in points_y if p[0] <= L]
    right_points_y = [p for p in points_y if p[0] > L]
    
    # Recursively find the closest pair of points on the left and right sides of L.
    delta1, pair1 = closet_pair_recursive(left_points_x, left_points_y)
    delta2, pair2 = closet_pair_recursive(right_points_x, right_points_y)

    # Get the minimum distance
    delta = min(delta1, delta2)
    min_pair = pair1 if delta1 < delta2 else pair2

    # Delete all points further than delta from line L.
    strip = [p for p in points_y if abs(p[0] - L) < delta]

    # Scan points in y-order and compare distance between each point and next 11 neighbors.
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 12, len(strip))):
            d = distance(strip[i], strip[j])
            if d < delta:
                delta = d
                min_pair = (strip[i], strip[j])
    return delta, min_pair

def closet_pair(points):
    #### Sort the points by x and y first, Avoid the repeatedly sort in the recursion.####
    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])
    return closet_pair_recursive(points_x, points_y)

if __name__ == '__main__':
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    distance, pair = closet_pair(points)
    print(f"The closest pair of points is {pair} with distance {distance}")


