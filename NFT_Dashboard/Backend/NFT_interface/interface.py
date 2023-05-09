'''
Created by 唐溢知 on 4/18/23.
'''

import requests
from web3 import Web3

'''
Documentation:
1. https://docs.alchemy.com/docs/nft-project-code-templates
2. https://docs.alchemy.com/reference/nft-api-quickstart
3. https://dashboard.alchemy.com/
4. https://docs.alchemy.com/reference/sdk-getnftsales
5. https://docs.alchemy.com/reference/ethereum-api-quickstart
'''

API_key = 'PlIE5PSJaLBOTy67DORlQwY3MchgQxfP'
API_url = "https://eth-mainnet.g.alchemy.com/v2/PlIE5PSJaLBOTy67DORlQwY3MchgQxfP"
API_nft_url = 'https://eth-mainnet.g.alchemy.com/nft/v2/PlIE5PSJaLBOTy67DORlQwY3MchgQxfP'

def getNFTsForCollection(contractAddress, withMetadata, startToken):
	url = API_url + '/getNFTsForCollection?contractAddress=' + contractAddress + '&withMetadata=' + str(withMetadata) + '&startToken=' + str(startToken)
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

# def getNFTsForCollection(contractAddress, withMetadata):
# 	url = API_url + '/getNFTsForCollection?contractAddress=' + contractAddress + '&withMetadata=' + str(withMetadata) + '&limit=500'
# 	r = requests.get(url, headers={"accept": "application/json"})
# 	return r.json()

def getOwnersForCollection(contractAddress):
	url = API_url + '/getOwnersForCollection/?contractAddress=' + contractAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def getOwnersByAddress(walletAddress):
	url = API_url + '/getNFTs/?owner=' + walletAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def getOwnerOfNTF(contractAddress, tokenid):
	url = API_url + '/getOwnersForToken?contractAddress=' + contractAddress + '&tokenId=' + str(tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def computeRarity(contractAddress, tokenid):
	url = API_nft_url + '/computeRarity/?contractAddress=' + contractAddress + '&tokenId=' + str(tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def getNFTSales(contractAddress, tokenid):
	# from block 0 to latest block, with ascending order
	url = API_url + '/getNFTSales?fromBlock=0&toBlock=latest&order=desc&contractAddress=' + contractAddress + '&tokenId=' + str(tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def getFloorPrice(contractAddress):
	url = API_nft_url + "/getFloorPrice?contractAddress=" + contractAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def getMetaData(contractAddress, tokenid):
	url = API_nft_url + '/getNFTMetadata?contractAddress=' + contractAddress + '&tokenId=' + str(tokenid) + '&refreshCache=false'
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()

def getNFTAttributes(contractAddress):
	url = API_nft_url + '/summarizeNFTAttributes?contractAddress=' + contractAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r.json()
