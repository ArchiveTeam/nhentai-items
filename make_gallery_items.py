import re
import sys

import requests


def main(start_num: int):
    response = requests.get('https://nhentai.net/')
    max_num = 0
    for s in re.findall(b'/g/([0-9]+)/', response.content):
        num = int(s)
        if num > max_num:
            max_num = num
    assert max_num > start_num, 'Maximum found ID is higher than the start ID.'
    with open('gallery_{}-{}.txt'.format(start_num, max_num), 'w') as f:
        for i in range(start_num, max_num+1):
            f.write('gallery:'+str(i)+'\n')

if __name__ == '__main__':
    main(int(sys.argv[1]))

