import os
import shutil
import sys
from functions import generate_pages_recursive


def delete_folder(path):
    if not os.path.exists(path):
        raise ValueError(f"Path `{path}` does not exist")

    if os.path.isfile(path):
        raise ValueError(f"Path `{path}` is file instead of a folder")

    for file_or_folder in os.listdir(path):
        cur_path = os.path.join(path, file_or_folder)
        if os.path.isfile(cur_path):
            os.remove(cur_path)
        else:
            delete_folder(cur_path)
    os.rmdir(path)


def overwrite_folder(source, target):

    if not os.path.exists(source):
        raise Exception("No static folder")

    if os.path.exists(target):
        delete_folder(target)

    os.makedirs(target)

    for file_or_folder in os.listdir(source):
        cur_path = os.path.join(source, file_or_folder)
        dest_path = os.path.join(target, file_or_folder)

        if os.path.isfile(cur_path):
            shutil.copy(cur_path, dest_path)

        else:
            overwrite_folder(cur_path, dest_path)


def main():
    basepath = "/"

    args = sys.argv

    if len(args) > 1:
        basepath = sys.argv[1]

    dir_path_content = os.path.join(os.getcwd(), "content")
    template_path = os.path.join(os.getcwd(), "template.html")
    dest_dir_path = os.path.join(os.getcwd(), "docs")

    generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path)


main()
