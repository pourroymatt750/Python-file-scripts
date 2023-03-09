
Matthew Pourroy
4:38 PM (0 minutes ago)
to me

# import OS module

import os

import string

import re

 

# Get the list of all files and directories

path = "C:\\xampp\downloads\\htdocs\\bayview-condo-json\\drawings\\structural"

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

    old_file = f"C:\\xampp\\downloads\\htdocs\\bayview-condo-json\\drawings\\structural\\{old}"

    new_file = f"C:\\xampp\\downloads\\htdocs\\bayview-condo-json\\drawings\\structural\\{new}"

    os.rename(old_file, new_file)
