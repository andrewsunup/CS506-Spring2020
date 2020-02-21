

def draw_mall(height=2, width=3):
    """
    draw a mall with height and width.
    :param: height is the height of mall, 2  means it is a 2 storey mall
    :param: width is the width. 2 means, 2 unit within same storey
    """
    if height <= 0 or width <= 0:
       raise ValueError("Please input valid height and width")

    print()
    draw_mall_roof(width)

    for _ in range(height):
        print()
        draw_mall_floor(width)
        print()
        draw_mall_wall(width)
    print()
    draw_mall_base(width)

    print()

    return

def draw_mall_floor(width=3):
    if width <= 0:
       raise ValueError("Please input valid  width")
    for _ in range(width):
        print("|=|", "|=|", sep="---", end="")

def draw_mall_wall(width=3):
    if width <= 0:
       raise ValueError("Please input valid  width")
    for _ in range(width):
        print("|=|", "|=|", sep="   ", end="")

def draw_mall_roof(width=3):

    if width <= 0:
       raise ValueError("Please input valid  width")

    for _ in range(width):
        print("   ", "   ", sep=" = ", end="")
    print()
    for _ in range(width):
        print("   ", "   ", sep="===", end="")


def draw_mall_base(width = 3):
    if width <= 0:
       raise ValueError("Please input valid  width")
    for _ in range(width):
       print("|=|", "|=|", sep="===", end="")
    print()

