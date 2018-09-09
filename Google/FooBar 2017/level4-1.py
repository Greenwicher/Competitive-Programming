def cal_distance(x1, x2):
    """
    calculate the Euclidean distance between point x1 and x2
    :param x1: Tuple(int, int), the coordinates of the first point
    :param x2: Tuple(int, int), the coordinates of the second points
    :return: double, the Euclidean distance
    """
    return ((x2[0]-x1[0])**2 + (x2[1]-x1[1])**2) ** 0.5

def cal_direction(x1, x2):
    """
    calculate the direction vector between point x1 and x2
    :param x1: Tuple(int, int), the coordinates of the first point
    :param x2: Tuple(int, int), the coordinates of the second points
    :return: Tuple(double, double), the direction vector between point x1 and x2
    """
    x, y = x2[0]-x1[0], x2[1]-x1[1]
    gcd = cal_gcd(x, y)
    if gcd == 0:
        return None, None
    ans = x // gcd, y // gcd
    return ans

def cal_gcd(a, b):
    """
    calculate the greatest common divisor given a, b
    :param a: int,
    :param b: int,
    :return: int, the greatest common divisor given a, b
    """
    while b:
        a, b = b, a % b
    return abs(a)

def generate_image(x, dimensions):
    """
    generate the reflection point of x along the four borders of the house
    :param x: Tuple(int, int), the coordinates of the point x
    :param dimensions: List[int, int], the width and height of the house
    :return: double, the four reflection/image points of x
    """
    w, h = dimensions
    image = [(-x[0], x[1]), (x[0], -x[1]), (2*w-x[0], x[1]),(x[0], 2*h-x[1])]
    return image

def sucide(captain_position, captain_images, v):
    """
    check whether the beam will shoot captain first
    :param captain_position: List[int, int], the coordinate of captain's position
    :param captain_images: Set(int, int), the coordinates of captain's image points so far
    :param v: Tuple(int, int), the coordinate of bad guy's image point
    :return: Bool, whether the beam will shoot captain first
    """
    # calculate the unit move distance
    direction = cal_direction(captain_position, v)
    x, y = captain_position
    # calculate the maximum integer points between captain and v
    step = abs(v[0] - captain_position[0]) // abs(direction[0])
    i = 0
    while i < step:
        x += direction[0]
        y += direction[1]
        i += 1
        # if any image of captain is between captain and v, then it will shoot captain first
        if (x, y) in captain_images:
            return True
    return False


def answer(dimensions, captain_position, badguy_position, distance):
    """
    calculate the number of feasible distinct directions that captain can shoot the bad guy
    :param dimensions: List[int, int], the width and height of the house
    :param captain_position: List[int, int], the coordinate of captain
    :param badguy_position: List[int, int], the coordinate of bad guy
    :param distance: int, the maximum distance that the bullet can travel
    :return: int, the number of feasible distinct directions
    """
    # exit if the distance between captain_position and badguy_position is larger than the maximum distance
    if cal_distance(captain_position, badguy_position) <= distance:
        queue = [(tuple(captain_position), tuple(badguy_position))] # store all the feasible image points
    else:
        return 0
    visited = set() # store the visited image points
    feasible = set() # store the feasible directions
    captain_images = set([tuple(captain_position)]) # store the image points of captain
    while queue:
        u, v = queue.pop(0) # u, v is the image points of captain and bad guy, respectively
        if v not in visited:
            visited.add(v)
            # check whether the beams hit captain first
            if not sucide(captain_position, captain_images, v):
                feasible.add(cal_direction(captain_position, v))
            # generate images based on current u (captain) and v (bad guy)
            imageu = generate_image(u, dimensions)
            imagev = generate_image(v, dimensions)
            for _u, _v in zip(imageu, imagev):
                # if the distance is larger than maximum distance, it can be proven that the distance between all its
                # image unvisited points and captain_position is larger than maximum distance
                if cal_distance(captain_position, _v) <= distance:
                    queue.append((_u, _v))
            # update image points of captain
            for _u in imageu:
                captain_images.add(_u)
    ans = len(feasible)
    return ans

print(answer([3,2],[1,1],[2,1],4), 7)
print(answer([300,275],[150,150],[185,100],500),9)
print(answer([10,10],[5,5],[6,6],5))
print(answer([4,4],[2,2],[3,4],5))