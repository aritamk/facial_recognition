# author: Mark Arita

import os

def get_all_sub_directories(root_path):
    if root_path is None or not os.path.exists(root_path):
        return None

    print("Searching from ", root_path)

    directories = []
    os.walk(root_path)

    dirs = next(os.walk(root_path))[1]
    for sub_dir in dirs:
        directories.append(root_path + "/" + sub_dir + "/")

    return directories


def get_all_child_files(dirs):
    if dirs is None:
        return None

    image_files = []
    metadata_files = []
    names = []

    for sub_dir in dirs:
        files, metadata = get_all_files(sub_dir)
        image_files.extend(files)
        metadata_files.extend(metadata)
        names.append(os.path.basename(os.path.dirname(sub_dir)))

    return image_files, metadata_files, names


def get_all_files(path, exts=[]):
    if path is None:
        return None

    files = []

    # get all child files in all subdirectories
    dirs = [path]
    while not dirs is None and not len(dirs) == 0:
        # get all files in current directory
        for item in os.listdir(dirs[0]):
            object_path = os.path.join(dirs[0], item)

            # check file of acceptable type
            if os.path.isfile(object_path):
                name, extension = os.path.splitext(object_path)
                if extension in exts:
                    files.append(os.path.join(dirs[0], item))
            elif os.path.isdir(object_path):
                dirs.append(object_path)

        dirs.remove(dirs[0])  # remove first dir

    return files