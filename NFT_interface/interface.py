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

def test_connection():
	w3 = Web3(Web3.HTTPProvider(alchemy_url))
	latest_block = w3.eth.get_block("latest")
	print(latest_block)

def getNFTsForCollection(contractAddress, withMetadata):
	url = API_url + '/getNFTsForCollection?contractAddress=' + contractAddress + '&withMetadata=' + str(withMetadata)
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getOwnersForCollection(contractAddress):
	url = API_url + '/getOwnersForCollection/?contractAddress=' + contractAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getOwnersByAddress(walletAddress):
	url = API_url + '/getNFTs/?owner=' + walletAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getOwnerOfNTF(contractAddress, tokenid):
	url = API_url + '/getOwnersForToken?contractAddress=' + contractAddress + '&tokenId=' + str(tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def computeRarity(contractAddress, tokenid):
	url = API_nft_url + '/computeRarity/?contractAddress=' + contractAddress + '&tokenId=' + str(tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getNFTSales(contractAddress, tokenid):
	# from block 0 to latest block, with ascending order
	url = API_url + '/getNFTSales?fromBlock=0&toBlock=latest&order=asc&contractAddress=' + contractAddress + '&tokenId=' + str(tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getFloorPrice(contractAddress):
	url = API_nft_url + "/getFloorPrice?contractAddress=" + contractAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getMetaData(contractAddress, tokenid):
	url = API_nft_url + '/getNFTMetadata?contractAddress=' + contractAddress + '&tokenId=' + str(tokenid) + '&refreshCache=false'
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def getNFTAttributes(contractAddress):
	url = API_nft_url + '/summarizeNFTAttributes?contractAddress=' + contractAddress
	r = requests.get(url, headers={"accept": "application/json"})
	return r

def testInterface():
	#getNFTsForCollection('0x394E3d3044fC89fCDd966D3cb35Ac0B32B0Cda91', True)
	#getOwnersForCollection('0x394E3d3044fC89fCDd966D3cb35Ac0B32B0Cda91')
	#getOwnersByAddress('elanhalpern.eth')
	#getOwnerOfNTF('0xDd69da9a83ceDc730bc4d3C56E96D29Acc05eCDE', 4254)
	#computeRarity('0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D', 7090)
	#getNFTSales('0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D', 7090)
	#getFloorPrice('0xe785E82358879F061BC3dcAC6f0444462D4b5330')
	#getMetaData('0x5180db8F5c931aaE63c74266b211F580155ecac8', 1590)
	#getNFTAttributes('0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D')
	example = getNFTsForCollection('0x394E3d3044fC89fCDd966D3cb35Ac0B32B0Cda91', True)
	print(example.text)

def unimplemented():
	# https://docs.alchemy.com/docs/how-to-get-nft-owners-at-a-specific-block-height
	# https://docs.alchemy.com/docs/how-to-filter-out-spam-nfts
	# https://docs.alchemy.com/docs/how-to-get-minters-of-an-nft-collection
	# https://docs.alchemy.com/reference/getcontractmetadata
	# https://docs.alchemy.com/reference/getnftmetadatabatch
	# https://docs.alchemy.com/reference/searchcontractmetadata
	pass

testInterface()
