# parse transaction history of a user
import requests
import time
import json

# read in file
sellfile = './0x194cc2541ea8696957acdcf1dc3dd5a687bb5ca5sell.txt'
buyfile = './0x194cc2541ea8696957acdcf1dc3dd5a687bb5ca5buy.txt'
wallet_address = '0x194cc2541ea8696957acdcf1dc3dd5a687bb5ca5'
sell = 0
buy = 0
API_url = "https://eth-mainnet.g.alchemy.com/v2/PlIE5PSJaLBOTy67DORlQwY3MchgQxfP"

# store all transaction history into a data structure
all_nfts = {}

def parse_json(filepath):
	global sell
	global buy
	with open(filepath) as f:
		data = json.load(f)
		for transaction in data:
			address = transaction['contract']['address']
			tokenid = transaction['tokenId']
			# initialize data structure
			if address not in all_nfts.keys():
				all_nfts[address] = {}
			if tokenid not in all_nfts[address].keys():
				all_nfts[address][tokenid] = []
			# fill in data
			if [transaction['timeLastUpdated'], transaction['from'], transaction['to'], transaction['blockNumber']] not in all_nfts[address][tokenid]:
				all_nfts[address][tokenid].append([transaction['timeLastUpdated'], transaction['from'], transaction['to'], transaction['blockNumber']]);
			if transaction['from'].lower() == wallet_address:
				sell += 1
			else:
				buy += 1

parse_json(sellfile)
parse_json(buyfile)

def getNFTSales(blockNumber, From, To, contractAddress, Tokenid):
	time.sleep(0.1)
	#url = API_url + '/getNFTSales?fromBlock=' + str(blockNumber) + '&toBlock=' + str(blockNumber) + '&contractAddress=' + str(contractAddress) + '&buyerAddress=' + str(To) + '&sellerAddress=' + str(From) + '&tokenId=' + str(Tokenid)
	url = API_url + '/getNFTSales?fromBlock=0&toBlock=latest&contractAddress=' + str(contractAddress) + '&buyerAddress=' + str(To) + '&sellerAddress=' + str(From) + '&tokenId=' + str(Tokenid)
	r = requests.get(url, headers={"accept": "application/json"})
	return r

print(getNFTSales('0xc8229d', '0x7b34c08ce9eef94e3ca2e0137d0e5d36e8c79799', '0x194cc2541ea8696957acdcf1dc3dd5a687bb5ca5', '0x995020804986274763df9deb0296b754f2659ca1', 6177).text)
# parse the data structure to calculate details
# sort according to time
for collection in all_nfts.keys():
	for tokenid in all_nfts[collection].keys():
		all_nfts[collection][tokenid].sort(key = lambda x: x[0], reverse=False)
#print(all_nfts)
#print(sell, buy)
def calculate_netincome(profit):
	netincome = 0
	for collection in all_nfts.keys():
		for tokenid in all_nfts[collection].keys():
			for i in range(len(all_nfts[collection][tokenid])):
				# check what's the price
				r = json.loads(getNFTSales(all_nfts[collection][tokenid][i][3], all_nfts[collection][tokenid][i][2], all_nfts[collection][tokenid][i][1], collection, tokenid).text)
				if len(r['nftSales']) == 0:
					r = json.loads(getNFTSales(all_nfts[collection][tokenid][i][3], all_nfts[collection][tokenid][i][1], all_nfts[collection][tokenid][i][2], collection, tokenid).text)
				if len(r['nftSales']) == 0:
					continue
				# whether calculate profit only
				if profit:
					if i == 0 and str(r['nftSales'][0]['sellerAddress']).lower() == wallet_address:
						continue
					if i == len(all_nfts[collection][tokenid])-1 and str(r['nftSales'][0]['buyerAddress']).lower() == wallet_address:
						continue
				if str(r['nftSales'][0]['buyerAddress']).lower() == wallet_address:
					netincome -= int(r['nftSales'][0]['sellerFee']['amount']) / 1000000000
				else:
					netincome += int(r['nftSales'][0]['sellerFee']['amount']) / 1000000000
	return netincome

def most_attention():
	all_purchase = []
	for collection in all_nfts.keys():
		for tokenid in all_nfts[collection].keys():
			all_purchase.append([collection, Tokenid, len(all_nfts[collection][Tokenid])])
	all_purchase.sort(key = lambda x: x[2], reverse=False)

def userStats():
	calculate_netincome(True)
	most_attention()

print(calculate_netincome(True))
userStats()
