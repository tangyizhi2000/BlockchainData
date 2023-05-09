from NFT_interface import interface
import json

# contract_address = "0x60E4d786628Fea6478F785A6d7e704777c86a7c6"


def fetch_and_store_nft_data(contract_address):
    global nft_data

    nft_data = []
    start_token = 0

    while True:
        nfts = interface.getNFTsForCollection(contract_address, True, start_token)
        if not nfts or len(nfts) == 0 or start_token > 5000:
            break
        start_token += 100

        for nft in nfts["nfts"]:
            token_id = int(nft["id"]["tokenId"], 16)

            print("token_id: ", token_id)
            raw = nft["media"][0]["raw"]

            sales = interface.getNFTSales(contract_address, token_id)
            if not sales["nftSales"] or not sales["nftSales"][0]["sellerFee"] or not sales["nftSales"][0]["protocolFee"] \
                    or not sales["nftSales"][0]["royaltyFee"]:
                continue  # Skip this NFT if there are no sales
            last_sale = sales["nftSales"][0]
            last_price = int(last_sale["sellerFee"]["amount"]) + int(last_sale["protocolFee"]["amount"]) + int(
                last_sale["royaltyFee"]["amount"])
            last_price = last_price / (10 ** 18)

            buyer = last_sale["buyerAddress"]
            seller = last_sale["sellerAddress"]

            if len(sales["nftSales"]) > 1:
                if not sales["nftSales"][1]["sellerFee"] or not sales["nftSales"][1]["protocolFee"] or not \
                sales["nftSales"][1]["royaltyFee"]:
                    continue  # Skip this NFT if there are no sales
                previous_sale = sales["nftSales"][1]
                prev_price = int(previous_sale["sellerFee"]["amount"]) + int(previous_sale["protocolFee"]["amount"]) + int(
                    previous_sale["royaltyFee"]["amount"])
                prev_price = prev_price / (10 ** 18)
                trend = (last_price - prev_price) / prev_price
            else:
                trend = 0

            rarity_data = interface.computeRarity(contract_address, token_id)
            cumulative_rarity = sum(r["prevalence"] for r in rarity_data) / len(rarity_data)

            attribute_dict = {attr["trait_type"]: {"value": attr["value"], "prevalence": attr["prevalence"]} for attr in
                              rarity_data}

            nft_data.append({
                "token_id": token_id,
                "raw": raw,
                "last_price": last_price,
                "cumulative_rarity": cumulative_rarity,
                "buyer": buyer,
                "seller": seller,
                "trend": trend,
                "attribute": attribute_dict
            })

    with open("nft_data.json", "w") as f:
        json.dump(nft_data, f)

    return nft_data


def categorize_nfts(nft_data, contract_address):
    if nft_data is None or len(nft_data) == 0:
        return {}
    categories = {}

    for nft in nft_data:
        attributes = nft["attribute"]
        for trait_type, trait_info in attributes.items():
            if trait_type not in categories:
                categories[trait_type] = {}

            value = trait_info["value"]
            prevalence = trait_info["prevalence"]

            if value not in categories[trait_type]:
                categories[trait_type][value] = {
                    "num": 1,
                    "prevalence": prevalence,
                    "floor_price": nft["last_price"],
                    "item_on_floor": nft["token_id"],
                    "total_price": nft["last_price"],
                    "total_trend": nft["trend"],
                    "nfts": [nft]
                }
            else:
                categories[trait_type][value]["num"] += 1
                categories[trait_type][value]["nfts"].append(nft)
                categories[trait_type][value]["total_price"] += nft["last_price"]
                categories[trait_type][value]["total_trend"] += nft["trend"]

                if nft["last_price"] < categories[trait_type][value]["floor_price"]:
                    categories[trait_type][value]["floor_price"] = nft["last_price"]
                    categories[trait_type][value]["item_on_floor"] = nft["token_id"]

    # Calculate average price and trend
    for trait_type, values in categories.items():
        for value, data in values.items():
            print("values.items()", values.items())
            data["average_price"] = data["total_price"] / data["num"]
            data["average_trend"] = data["total_trend"] / data["num"]
            del data["total_price"], data["total_trend"]

    filename = f"{contract_address}.json"
    with open(filename, "w") as f:
        json.dump(categories, f)

    return categories
