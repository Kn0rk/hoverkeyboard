
def simple_staggered_grid():
    points = []
    index_one = 0.1
    index_two = 0.1
    offset = False
    while index_one < 0.95:
        while index_two < 0.85:
            offset = not offset
            if offset:
                points.append(index_one + 0.05)
            else:
                points.append(index_one)
            points.append(index_two)
            index_two += 0.1
        index_one += 0.1
        index_two = 0.1

    # Include Points outside of the boundary box
    points.extend([-5,-5, 5,-5, 5,5, -5,5])
    return points