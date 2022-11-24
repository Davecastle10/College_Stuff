def find_surface_area(cuboid_tuple):
    # calculates area of a cuboid with ide lengths from a tuple
    sides_a = cuboid_tuple[0] * cuboid_tuple[1] * 2
    sides_b = cuboid_tuple[1] * cuboid_tuple[2] * 2
    sides_c = cuboid_tuple[2] * cuboid_tuple[0] * 2
    total_area = sides_a + sides_b + sides_c
    return total_area
