'''
Created by 唐溢知 on 4/18/23.
'''
import sys
import sys
sys.path.append('../..')
from BlockchainData.NFT_interface import interface
from BlockchainData.IPFS_interface import IPFS
import json

def parseNFTMetaData(contractAddress, tokenid):
	# Documentation: https://docs.alchemy.com/docs/how-to-fetch-complete-nft-metadata
	r = interface.getMetaData(contractAddress, tokenid).text
	metadata = json.loads(r)
	ipfs_address = metadata['metadata']['image']
	print(ipfs_address)
	IPFS.download_img(ipfs_address)


def testParsing():
	parseNFTMetaData('0x5180db8F5c931aaE63c74266b211F580155ecac8', 1590) # Fail, not a IPFS file
	parseNFTMetaData('0x4Ad3785EC7EED7589FA86538244a4530f962434F', 7931) # Succeed, download image file
	parseNFTMetaData('0x60E4d786628Fea6478F785A6d7e704777c86a7c6', 19788)

testParsing()