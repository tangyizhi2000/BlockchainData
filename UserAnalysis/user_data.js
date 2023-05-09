// Imports the Alchemy SDK
const { Alchemy, Network } = require("alchemy-sdk");

// Configures the Alchemy SDK
const config = {
  apiKey: "PlIE5PSJaLBOTy67DORlQwY3MchgQxfP", // Replace with your API key
  network: Network.ETH_MAINNET, // Replace with your network
};

// Creates an Alchemy object instance with the config to use for making requests
const alchemy = new Alchemy(config);

// Example of using the new getTransfersForOwner method
const getprofit = async (walletaddress) => {

  // Calling the getTransfersForOwner method
  let category = "FROM";
  let transfers = await alchemy.nft.getTransfersForOwner(
    walletaddress,
    category,
  );

  let all_history = [];
  let i = 1;
  while (true){
  	console.log(i); i += 1;
  	all_history.push(...transfers['nfts'])
  	if ('pageKey' in transfers && transfers['pageKey'] !== undefined){
  		console.log(transfers['pageKey'])
		let options = {
		    pageKey: transfers['pageKey']
		};
		transfers = await alchemy.nft.getTransfersForOwner(
		    walletaddress,
		    category,
		    options,
		);
  	} else {
  		break;
  	}
  }


  var fs = require('fs');
  fs.writeFile("./"+walletaddress.toString()+'.txt', JSON.stringify(all_history), function(err) {if (err) {console.log(err);}});
};

const readUsers = () => {
	const fs = require('fs')
	var mydata;
    fs.readFile('./all_wallet_address.json', (err, inputD) => {
	   if (err) throw err;
	      //console.log(inputD.toString());
	      mydata = JSON.parse(inputD);
	      for (var key in mydata) {
		    if (mydata.hasOwnProperty(key)) {
		        console.log(key + " -> " + mydata[key]);
		        getprofit(key);
		        break;
		    }
		}
	})
}

readUsers();