import os
import shutil
import sys
from functions import generate_pages_recursive
from copystatic import copy_files_recursive


# def delete_folder(path):
#     if not os.path.exists(path):
#         raise ValueError(f"Path `{path}` does not exist")

#     if os.path.isfile(path):
#         raise ValueError(f"Path `{path}` is file instead of a folder")

#     for file_or_folder in os.listdir(path):
#         cur_path = os.path.join(path, file_or_folder)
#         if os.path.isfile(cur_path):
#             os.remove(cur_path)
#         else:
#             delete_folder(cur_path)
#     os.rmdir(path)


# def overwrite_folder(source, target):

#     if not os.path.exists(source):
#         raise Exception("No static folder")

#     if os.path.exists(target):
#         delete_folder(target)

#     os.makedirs(target)

#     for file_or_folder in os.listdir(source):
#         cur_path = os.path.join(source, file_or_folder)
#         dest_path = os.path.join(target, file_or_folder)

#         if os.path.isfile(cur_path):
#             shutil.copy(cur_path, dest_path)

#         else:
#             overwrite_folder(cur_path, dest_path)


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_public)


main()
