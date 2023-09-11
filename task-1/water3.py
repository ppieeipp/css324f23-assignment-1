def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4 

def successors(s):
    x, y, z = s
    
    # Pour from the 8-liter bottle to the 5-liter bottle
    t = min(x, 5 - y)
    if t > 0:
        yield ((x - t, y + t, z), t)

    # Pour from the 8-liter bottle to the 3-liter bottle
    t = min(x, 3 - z)
    if t > 0:
        yield ((x - t, y, z + t), t)

    # Pour from the 5-liter bottle to the 8-liter bottle
    t = min(y, 8 - x)
    if t > 0:
        yield ((x + t, y - t, z), t)

    # Pour from the 5-liter bottle to the 3-liter bottle
    t = min(y, 3 - z)
    if t > 0:
        yield ((x, y - t, z + t), t)

    # Pour from the 3-liter bottle to the 8-liter bottle
    t = min(z, 8 - x)
    if t > 0:
        yield ((x + t, y, z - t), t)

    # Pour from the 3-liter bottle to the 5-liter bottle
    t = min(z, 5 - y)
    if t > 0:
        yield ((x, y + t, z - t), t)

# Test the code
initial = initial_state()
goal = (4, 4, 0)



