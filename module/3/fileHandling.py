import os

name = open("kannan.txt")
print(name.read())

os.chmod("F:/IMS/CyberSecurity/cybersec-python/file_handling/index.html", 0o777)
accessability = os.access("F:/IMS/CyberSecurity/cybersec-python/file_handling/index.html", os.W_OK)
read_accessability = os.access("F:/IMS/CyberSecurity/cybersec-python/file_handling/index.html", os.R_OK)
print("file access is",accessability)
print("file access read is",read_accessability)

file_report = os.stat("F:/IMS/CyberSecurity/cybersec-python/file_handling/index.html")
print(file_report)