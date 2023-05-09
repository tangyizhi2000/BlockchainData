from flask import Flask, jsonify, request, render_template
from NFT_interface.data_processing import fetch_and_store_nft_data, categorize_nfts
import json

app = Flask(__name__)


@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    contract_address = "0x60E4d786628Fea6478F785A6d7e704777c86a7c6"
    filename = f"{contract_address}.json"
    with open(filename, "r") as f:
        results = json.load(f)
    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    contract_address = "0x60E4d786628Fea6478F785A6d7e704777c86a7c6"
    nft_data = fetch_and_store_nft_data(contract_address)
    with open("nft_data.json", "r") as f:
        nft_data = json.load(f)
    categorize_nfts(nft_data, contract_address)
    app.run(debug=True)
