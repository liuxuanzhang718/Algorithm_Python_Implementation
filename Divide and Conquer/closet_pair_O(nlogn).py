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
    return min_distance, min_pair, sorted(points, key=lambda p: p[1])

def closet_pair_recursive(points_x, points_y):

    if len(points_x) <= 3:
        return brute_force(points_x)
    
    # Compute separation line L
    mid = len(points_x) // 2
    L = points_x[mid][0]

    # Get the left and right subset
    left_points_x = points_x[:mid]
    right_points_x = points_x[mid:]

    delta1, pair1, y_sorted_1 = closet_pair_recursive(left_points_x, [p for p in points_y if p[0] <= L])
    delta2, pair2, y_sorted_2 = closet_pair_recursive(right_points_x, [p for p in points_y if p[0] > L])

    y_sorted = merge_sorted_lists(y_sorted_1, y_sorted_2)

    # Get the minimum distance
    delta = min(delta1, delta2)
    min_pair = pair1 if delta1 < delta2 else pair2

    # Delete all points further than delta from line L.
    strip = [p for p in y_sorted if abs(p[0] - L) < delta]

    # Scan points in y-order and compare distance between each point and next 11 neighbors.
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 12, len(strip))):
            d = distance(strip[i], strip[j])
            if d < delta:
                delta = d
                min_pair = (strip[i], strip[j])

    return delta, min_pair, y_sorted 

def closet_pair(points):
    #### Sort the points by x and y first, Avoid the repeatedly sort in the recursion.####
    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])
    return closet_pair_recursive(points_x, points_y)[:2]  

def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i][1] < list2[j][1]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

if __name__ == '__main__':
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    distance, pair = closet_pair(points)
    print(f"The closest pair of points is {pair} with distance {distance}")
