import re
from datetime import datetime
from pathlib import Path

today = [datetime(2022, 2, 19)]


# print(pattern)

def main(today):
    path_to_file1 = '/home/ubuntu/Downloads/mailog2022-02-17 - 2022-02-24'
    pattern = re.findall(r'\d{4}-\d{2}-\d{2}\s-\s\d{4}-\d{2}-\d{2}', path_to_file1)
    print(pattern)
    listToStr = ''.join(map(str, pattern))
    result = listToStr.split()
    print(result)
    path_to_file = '/home/ubuntu/Downloads/' + str(listToStr)
    print("the original result:" + str(result))
    date_start = result[0]
    date_end = result[2]
    for today in result:
        if today >= date_start and today <= date_end:
            path_to_file = '/home/ubuntu/Downloads/' + str(listToStr)
        else:
            print('the file is not in path')
        path = Path(path_to_file)
        if path.is_file():
            fpath = Path


print(main(today))

