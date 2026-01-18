import re

num=list(range(1,11))
num_str=str(num)

extract=re.findall(r'[1-5]',num_str)[0:5]
extract=list(map(int,extract))
print(f"Original list: {num_str}")
print(f"Extracted first five element:{extract}")
extract.reverse()
print(f"Reversed extracted elements:{extract}")