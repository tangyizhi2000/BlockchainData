'''
Created by 唐溢知 on 4/18/23.
'''

import requests
import shutil
import os

url = 'https://gateway.ipfs.io/ipfs/'
file_path = '../../BlockchainData/IPFS_interface/Samples/'

def test_downloads():
	# Download images from a list of IPFS hash
	hash_list = ['Qmd9HaQdMSyAReLM6KGNmdRSVhCkuTTNgC5R3LE41kMqSs/3149.png', 'QmQHVxjj8KDVBmXMzv242AFyXP32ytGZqxEAnLmLkjVHd6/1784.png', 'QmYDvPAXtiJg7s8JdRBSLWdgSphQdac8j1YuQNNxcGE1hg/1865.png']

	for h in hash_list:
		r = requests.get(url+h, stream=True, verify=False, headers={"Accept-Encoding": "identity"})
		print(r, r.headers, r.raw)
		filename = file_path+h.replace('/', '_')
		with open(filename, 'wb') as out_file:
			shutil.copyfileobj(r.raw, out_file)

#test_downloads()

def download_img(ipfs_address):	
	if ipfs_address.startswith('ipfs://'):
		# i.e. ipfs://Qmd9HaQdMSyAReLM6KGNmdRSVhCkuTTNgC5R3LE41kMqSs/7931.png
		target_file = ipfs_address[7:]
		print("downloading from", url+target_file)
		# https request
		r = requests.get(url+target_file, stream=True, verify=False, headers={"Accept-Encoding": "identity"})
		# filename processing
		filename = file_path + target_file.replace('/', '_')
		if not filename.endswith('.png'):
			filename += '.png'
		# save image file
		with open(filename, 'wb') as out_file:
			shutil.copyfileobj(r.raw, out_file)
	else:
		print("Not IPFS File")