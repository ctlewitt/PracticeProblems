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


# mat = []
# for _ in range(5):
#     mat .append([None]*5)
#
# print(mat)
#
# print(get_adjacent_neighbors(mat, [2,4]))
# print(get_adjacent_neighbors(mat, [0,0]))
# print(get_adjacent_neighbors(mat, [2,2]))
#
# print(get_neighbors(mat, [[2,3],[2,1],[3,2],[1,2],[2,2]]))
# print(get_neighbors(mat, [[2,3],[2,1],[3,2],[2,2]]))
# print(get_neighbors(mat, [[3,2],[1,2],[2,2]]))
# print(get_neighbors(mat, [[2,2]]))
#
#
# mat1 = []
# for _ in range(4):
#     mat1.append([None]*3)
#
# print(get_adjacent_neighbors(mat1, [2,2]))
# print(get_adjacent_neighbors(mat1, [0,0]))
# print(get_adjacent_neighbors(mat1, [2,1]))
#
# print(get_neighbors(mat1, [[2,1],[3,2],[1,2],[2,2]]))
# print(get_neighbors(mat1, [[2,1],[3,2],[2,2]]))
# print(get_neighbors(mat1, [[3,2],[1,2],[2,2]]))
# print(get_neighbors(mat1, [[2,2]]))
#


mat2 = []
for _ in range(3):
    mat2 .append([None]*3)

print(mat2)

print(all_paths(mat2, [0,0]))

mat3 = []
for _ in range(2):
    mat3.append([None] * 2)

print(mat3)

print(all_paths(mat3, [0, 0]))


mat4 = []
for _ in range(6):
    mat4.append([None] * 1)

print(mat4)

print(all_paths(mat4, [2, 0]))
print(all_paths(mat4, [0, 0]))


    # print([[0,0]append([2,2]]))