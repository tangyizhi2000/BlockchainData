'''
Created by 唐溢知 on 4/18/23.
'''

import requests
import shutil

# Download images from a list of IPFS hash
file_path = './Samples/'
hash_list = ['Qmd9HaQdMSyAReLM6KGNmdRSVhCkuTTNgC5R3LE41kMqSs/4227.png', 'Qmd9HaQdMSyAReLM6KGNmdRSVhCkuTTNgC5R3LE41kMqSs/3149.png', 'QmQHVxjj8KDVBmXMzv242AFyXP32ytGZqxEAnLmLkjVHd6/1784.png', 'QmYDvPAXtiJg7s8JdRBSLWdgSphQdac8j1YuQNNxcGE1hg/1865.png']
url = 'https://gateway.ipfs.io/ipfs/'

for h in hash_list:
    r = requests.get(url+h, stream=True, verify=False, headers={"Accept-Encoding": "identity"})
    print(r, r.headers, r.raw)
    filename = file_path+h.replace('/', '_')
    with open(filename, 'wb') as out_file:
    	shutil.copyfileobj(r.raw, out_file)
