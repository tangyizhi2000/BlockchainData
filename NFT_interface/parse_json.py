'''
Created by 唐溢知 on 4/18/23.
'''
import json
import time
import sys
import os
sys.path.append('../..')
from BlockchainData.NFT_interface import interface
from BlockchainData.IPFS_interface import IPFS


file_path = '../../BlockchainData/Data/'
if not os.path.exists(file_path):
	os.makedirs(file_path)

def parseNFTMetaData(contractAddress, tokenid):
	# Documentation: https://docs.alchemy.com/docs/how-to-fetch-complete-nft-metadata
	time.sleep(0.1) # avoid calling interface too many times got throttle
	r = interface.getMetaData(contractAddress, tokenid).text
	# load json and save json
	metadata = json.loads(r)
	metadata_fp = file_path+contractAddress+"_"+str(tokenid)+'.json'
	with open(metadata_fp, "w") as outfile:
		outfile.write(json.dumps(metadata))
	ipfs_address = metadata['metadata']['image']
	# save images
	IPFS.download_img(ipfs_address, file_path)

def parseNFTCollectionData(contractAddress):
	r = interface.getNFTsForCollection(contractAddress, False).text
	allNFTs = json.loads(r)
	print("Total", len(allNFTs['nfts']), " NTFs")
	for item in allNFTs['nfts']:
		tokenid = int(item['id']['tokenId'], 16) # convert hex string to int
		parseNFTMetaData(contractAddress, tokenid)

def testParsing():
	#parseNFTMetaData('0x5180db8F5c931aaE63c74266b211F580155ecac8', 1590) # Fail, not a IPFS file
	#parseNFTMetaData('0x4Ad3785EC7EED7589FA86538244a4530f962434F', 7931) # Succeed, download image file
	#parseNFTMetaData('0x60E4d786628Fea6478F785A6d7e704777c86a7c6', 19788)
	parseNFTCollectionData('0x306b1ea3ecdf94aB739F1910bbda052Ed4A9f949')

testParsing()
