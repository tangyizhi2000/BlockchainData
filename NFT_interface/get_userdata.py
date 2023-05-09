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

all_user_address = {}

def xactionHistory(walletAddress):
	pass

def xactionUsers(contractAddress, tokenid):
	time.sleep(0.1)
	r = interface.getNFTSales(contractAddress, tokenid).text
	xaction = json.loads(r)
	for history in xaction['nftSales']:
		#print(history['buyerAddress'], history['sellerAddress'])
		all_user_address[history['buyerAddress']] = 1
		all_user_address[history['sellerAddress']] = 1


def parseNFTCollectionData(contractAddress):
	r = interface.getNFTsForCollection(contractAddress, False).text
	allNFTs = json.loads(r)
	print("Total", len(allNFTs['nfts']), " NTFs")
	for item in allNFTs['nfts']:
		tokenid = int(item['id']['tokenId'], 16) # convert hex string to int
		xactionUsers(contractAddress, tokenid)
	print(all_user_address.keys())

def getUsers():
	#parseNFTCollectionData('0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D')
	print(interface.getContractsForOwner('0x610bBb9119B3Ec49ba3d12F9ABE5D561EAF25A82').text)

#getUsers()
interface.getTransfersForOwner('0x610bBb9119B3Ec49ba3d12F9ABE5D561EAF25A82')
