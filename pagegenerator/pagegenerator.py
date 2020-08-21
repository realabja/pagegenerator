import re
import os
# print(os.getcwd())
# print(os.listdir(f"{ os.getcwd()}"))


def read(file):
    with open(file, "r") as f:
        return f.readlines()


def folder_name(title_name):
    title_to_list = title_name.split()
    name_tuple = tuple(title_to_list)
    return "-".join(name_tuple)


rawtext = read("example.txt")
title = rawtext[0]
date_and_writer = rawtext[1]
text = "\n".join(rawtext[2:])
post_template = read("blog-post-template.html")
post_preview = read("post-preview-template.html")
# content_holders=[]


def process(raw_template):
    for index, line in enumerate(raw_template):
        raw_template[index] = line.replace("{folder_name(title)}", folder_name(title))
        if re.search("<!-- content insertion -->", line):
            content_type = re.search(r"type==[1-zA-Z-]*", raw_template[index + 1]).group()
            content_type = content_type.replace("type==", "")

            raw_template.insert(index, globals()[content_type])

    return raw_template

# content_holder = (index, content_type)
# content_holders.append(content_holder)


try:
    os.makedirs(f"{folder_name(title)}/")
except:
    print("error while creating directory")


with open(f"{folder_name(title)}/index.html", "w")as processed_page:
    processed_page.writelines(process(post_template))


with open(f"{folder_name(title)}/post-preview.html", "w")as processed_page:
    processed_page.writelines(process(post_preview))
