from markdown_blocks import markdown_to_html_node, extract_title
import os


def generate_page(basepath, from_path, template_path, dest_path):
    # print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = None
    with open(from_path) as f:
        from_file = f.read()

    if from_file is None:
        raise ValueError(f"from_path `{from_path}` is empty or does not exist")

    temp_file = None
    with open(template_path) as f:
        temp_file = f.read()

    if temp_file is None:
        raise ValueError(f"template_path `{template_path}` is empty or does not exist")

    html_node = markdown_to_html_node(from_file)
    html_string = html_node.to_html()
    title = extract_title(from_file)

    if title is None:
        raise ValueError(f"Title is None for ```\n{html_string}\n```")

    result = (
        temp_file.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_string)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', 'src="' + basepath)
    )

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Overwrite the file
    with open(dest_path, "w") as f:
        f.write(result)


def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):

    for file_or_folder in os.listdir(dir_path_content):
        file_or_folder_path = os.path.join(dir_path_content, file_or_folder)

        if os.path.isfile(file_or_folder_path):
            split_tup = os.path.splitext(file_or_folder)

            if split_tup[1] == ".md":
                generate_page(
                    basepath,
                    os.path.join(dir_path_content, file_or_folder),
                    template_path,
                    dest_path=os.path.join(dest_dir_path, f"{split_tup[0]}.html"),
                )
        else:

            generate_pages_recursive(
                basepath,
                os.path.join(dir_path_content, file_or_folder),
                template_path,
                os.path.join(dest_dir_path, file_or_folder),
            )
