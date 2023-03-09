# import OS module
import os
import string
import re

 

# Get the list of all files and directories. Exact file path removed for security purposes.
path = "C:\\xampp\downloads\\htdocs\\..."

dir_list = os.listdir(path)

 

i = 1

for x in dir_list:

    splitX = os.path.splitext(x)

    title = re.sub('[-]', ' ', splitX[0])

    print("{")

    print(f"title: 'P&F {i}', ")

    print(f"title: '{title}', ")

    print(f"link: 'archives/structural/{x}' ")

    print("},")

    i+=1

 

for old in dir_list:

    new = re.sub('[" "]', '-', old)

    # Exact file path removed for security purposes.
    old_file = f"C:\\xampp\\downloads\\htdocs\\...{old}"

    new_file = f"C:\\xampp\\downloads\\htdocs\\..{new}"

    os.rename(old_file, new_file)
