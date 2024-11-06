import os

os.chmod("F:/IMS/Python/python/boto3.md", 0o777)

print(os.access("F:/IMS/Python/python/boto3.md", os.W_OK))

myContent = """
<html>
<body>
<center>
<h1> "Welcome to Sathiyan Cinemas" </h1>
</center>
</body>
</html>
"""


with open("F:/IMS/Python/python/boto3.md", "w") as var1:
    var1.write(myContent)

with open("kannan.html", "r") as f:
    read = f.readlines()
    print(type(read))

read.insert(-3, "<h2>i'm new to programming</h2>\n")

print(read)

with open("kannan.html", "w") as w:
    w.writelines(read)