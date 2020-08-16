import re


def read(file):
    with open(file, "r") as template:
        return template.readlines()



x = read("index.html")

for index, line  in enumerate(x):
    if re.search("<!-- content insertion -->", line):
        content_type = re.search(r"type==[1-zA-Z-]*", x[index+1]).group()
        content_type = content_type.replace("type==", "")
        print(content_type)
        x.pop(index)
        x.pop(index)
        x.insert(index+1, "I inserted this \n")



with open("newhtml.html", "w")as f:
    f.writelines(x)


