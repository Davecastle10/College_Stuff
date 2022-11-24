def intersects(a_sphere , array_of_spheres):
    """Returns the index of the first sphere in the array that intersects
    in 3-dimensional space, or -1. Note objects of class Sphere have 	attributes
    radius, x, y, z """
    base_x = a_sphere.x
    base_y = a_sphere.y
    base_z = a_sphere.z
    rad = a_sphere.radius 
    intersect = 0
    yes = False
    index_of_sphere = 0
    for i in range(len(array_of_spheres)):
        arr_x = array_of_spheres[i].x
        arr_y = array_of_spheres[i].y
        arr_z = array_of_spheres[i].z
        arr_rad = array_of_spheres[i].radius
        if base_x - rad <= arr_x + arr_rad <= base_x + rad or base_x - rad <= arr_x - arr_rad <= base_x + rad:
            intersect += 1
        elif base_y - rad <= arr_y + arr_rad <= base_y + rad or base_y - rad <= arr_y - arr_rad <= base_y + rad:
            intersect += 1
        elif base_Z - rad <= arr_Z + arr_rad <= base_Z + rad or base_Z - rad <= arr_Z - arr_rad <= base_Z + rad:
            intersect += 1
        elif intersect == 3:
            yes = True
            index_of_sphere = i
            break
    if yes == True:
        return index_of_sphere
    else:
        return -1

    
    
