import random as rand
from Rectangles import Rectangle
import matplotlib.patches as pat

def generate_rect(coverage_x, coverage_y):
    """Returns a rectangle with a random height, width and lower_left coordinate within the given parameters
    Args:
        coverage_x: Width of coverage area
        coverage_y: Height of the coverage area
    """
    assert isinstance(coverage_x,int)
    assert coverage_x > 0
    assert isinstance(coverage_y,int)
    assert coverage_y > 0
    width = rand.randint(1, coverage_x)
    height = rand.randint(1, coverage_y)
    left = rand.randint(0, coverage_x - width)
    right = rand.randint(0, coverage_y - height)
    lower_left = (left, right)
    return Rectangle(lower_left, width, height)

def trim_fit(before_rect, after):
    """Returns a rectangle after trimming it to fit into the grid along with the other rectangles.  if it can't fit
    return None.
    Args:
        before_rect: Rectangle to be trimmed and fit into the grid.
        after: List of rectangles already trimmed and fitted into grid.
    """
    assert isinstance(before_rect, Rectangle)
    assert isinstance(after, list)

    rects = [before_rect]
    for a in after:
        if a is not None:
            assert isinstance(a, Rectangle)
            holder = []
            for r in rects:
                if r.overlap(a):
                    temp = []
                    if r < a:
                        temp.append(Rectangle(r.lower_left, a.lower_left[0]-r.lower_left[0], r.height))
                    if r > a:
                        new_coord = (a.lower_left[0]+a.width, r.lower_left[1])
                        temp.append(Rectangle(new_coord, (r.lower_left[0]+r.width)-(a.lower_left[0]+a.width), r.height))
                    if r <= a:
                        temp.append(Rectangle(r.lower_left, r.width, a.lower_left[1]-r.lower_left[1]))
                    if r >= a:
                        new_coord = (r.lower_left[0], a.lower_left[1]+a.height)
                        temp.append(Rectangle(new_coord, r.width, (r.lower_left[1]+r.height)-(a.lower_left[1]+a.height)))
                    holder += temp
                else:
                    holder += [r]
            if not holder:
                return None
        rects = holder
    largest_area = 0
    largest_rect = None
    for r in rects:
        assert isinstance(r, Rectangle)
        if largest_area <= r.width*r.height:
            largest_area = r.width*r.height
            largest_rect = r
    return largest_rect

def give_rects(coverage_x, coverage_y, num_rects):
    """Returns a given number of rectangles
    Args:
        coverage_x: Width of the grid
        coverage_y: Height of the grid
        num_Rectangles: Number of rectangles to produce
    """
    assert isinstance(coverage_x,int)
    assert coverage_x > 0
    assert isinstance(coverage_y,int)
    assert coverage_y > 0
    assert isinstance(num_rects, int)
    assert num_rects > 0

    after = []
    original = []
    rect = generate_rect(coverage_x, coverage_y)
    original.append(rect)
    after.append(rect)
    counter = 1
    while counter < num_rects:
        total = 0
        for a in after:
            if a != None:
                total += a.height*a.width
        if total == coverage_y*coverage_x:
            break
        rect = generate_rect(coverage_x, coverage_y)
        end_rect = trim_fit(rect, after)
        if end_rect != None:
            original.append(rect)
            after.append(end_rect)
            counter += 1
    return (original, after)

def rect_grid(rects):
    """Returns a list of rectangles for matlib
    Args:
        rects: List of rectangles 
    """
    assert isinstance(rects, list)
    c = [(0,0,1,0.5), (0,0.5,0,0.5), (1,0,0,0.5)]
    e = [(0,0,1,1), (0,0.5,0,1), (1,0,0,1)]
    a = 0
    l = []
    a = 0
    for r in rects:
        if r != None:
            r = pat.Rectangle(r.lower_left,r.width,r.height, fc=c[a%len(c)] ,ec=e[a%len(e)])
            l.append(r)
        else:
            l.append(None)
        a += 1
    return l

def num_cover_all(coverage_x,coverage_y):
    """Returns number of rectangles needed to fill up all of the area
    Args:
        coverage_x: Width of coverage area
        coverage_y: Height of the coverage area
    """
    assert isinstance(coverage_x,int)
    assert coverage_x > 0
    assert isinstance(coverage_y,int)
    assert coverage_y > 0

    before = []
    before_rect = generate_rect(coverage_x, coverage_y)
    after = []
    before.append(before_rect)
    after.append(before_rect)
    count = 1
    while True:
        total = 0
        for a in after:
            if a != None:
                total += a.height*a.width
        if total == coverage_y*coverage_x:
            break
        before_rect = generate_rect(coverage_x, coverage_y)
        after_rect = trim_fit(before_rect, after)
        if after_rect != None:
            before.append(before_rect)
            after.append(after_rect)
            count = count + 1
    return count