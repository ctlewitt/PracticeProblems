# simplifies file paths with extra /'s .'s and ..'s
def path_simplifier(path):
    path_arr = path.split("/")
    new_path = []
    while len(path_arr) > 0:
        next = path_arr.pop()
        if next == "..":
            if len(path_arr) > 0:
                path_arr.pop()
        elif next != "" and next != ".":
            new_path.append(next)
    if len(new_path) == 0:
        return "/"
    else:
        return "/" + "/".join(new_path)


print path_simplifier("/foo/bar////")
print path_simplifier("/foo/./bar/./hi")
print path_simplifier("/foo/../bar")
print path_simplifier("/foo///bar")

# could do by filtering