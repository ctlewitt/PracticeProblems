# recursively find all paths in a matrix starting at a point

Y = 0
X = 1


def all_paths(mat, start):
    paths = []
    path_so_far = [start]
    for neighbor in get_neighbors(mat, path_so_far):
        paths.append(all_paths_aux(mat, [start, neighbor]))
    return paths


def get_neighbors(mat, path_so_far):
    neighbors = []
    for possible_neighbor in get_adjacent_neighbors(mat, path_so_far[-1]):
        if possible_neighbor not in path_so_far:
            neighbors.append(possible_neighbor)
    return neighbors


def get_adjacent_neighbors(mat, pos):
    height = len(mat)
    width = len(mat[0])
    adjacent_positions = [[pos[Y]-1, pos[X]],
                           [pos[Y]+1, pos[X]],
                           [pos[Y], pos[X]-1],
                           [pos[Y], pos[X]+1]]
    viable_adjacent_positions = [[y, x] for [y,x] in adjacent_positions if x >= 0 and x < width and y >= 0 and y < height]
    return viable_adjacent_positions


def all_paths_aux(mat, path_so_far):
    neighbors = get_neighbors(mat, path_so_far)
    if len(neighbors) == 0:
        return path_so_far
    paths = []
    for neighbor in neighbors:
        new_path_so_far = path_so_far
        new_path_so_far.append(neighbor)
        paths.extend(all_paths_aux(mat, new_path_so_far))
    # print("psf")
    # print(path_so_far)
    # print(paths)
    return paths


def create_matrix(height, width):
    mat = []
    for _ in range(height):
        mat.append([None]*width)
    return mat

# test get adjacent neighbors and get neighbors with square matrix
mat = create_matrix(5,5)
print(get_adjacent_neighbors(mat, [2,4]))
print(get_adjacent_neighbors(mat, [0,0]))
print(get_adjacent_neighbors(mat, [2,2]))

print(get_neighbors(mat, [[2,3],[2,1],[3,2],[1,2],[2,2]]))
print(get_neighbors(mat, [[2,3],[2,1],[3,2],[2,2]]))
print(get_neighbors(mat, [[3,2],[1,2],[2,2]]))
print(get_neighbors(mat, [[2,2]]))

# test get adjacent neighbors and get neighbors with rectangular matrix
mat1 = create_matrix(4,3)
print(get_adjacent_neighbors(mat1, [2,2]))
print(get_adjacent_neighbors(mat1, [0,0]))
print(get_adjacent_neighbors(mat1, [2,1]))

print(get_neighbors(mat1, [[2,1],[3,2],[1,2],[2,2]]))
print(get_neighbors(mat1, [[2,1],[3,2],[2,2]]))
print(get_neighbors(mat1, [[3,2],[1,2],[2,2]]))
print(get_neighbors(mat1, [[2,2]]))

# test all_paths for square matrix
mat2 = create_matrix(3,3)
print(all_paths(mat2, [0,0]))

# test all_paths for smaller, square matrix
mat3 = create_matrix(2,2)
print(all_paths(mat3, [0, 0]))

# test all_paths for rectangular matrix (where paths are cut off)
mat4 = create_matrix(6,1)
print(all_paths(mat4, [2, 0]))
print(all_paths(mat4, [0, 0]))
