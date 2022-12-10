import json


class Settings:

    def __init__(self, json_path):
        try:
            with open(json_path, "r") as f:
                data = json.loads(f.read())
        except FileNotFoundError:
            raise ValueError("JSON not found")

        self.infura_api = data.get('infura_api')
        self.infura_link = data.get('infura_link')

    def update_json(self, json_path="PriceTrackerSettings.json"):
        data = {"infura_api": self.infura_api, "infura_link": self.infura_link}

        with open(json_path, "w") as f:
            data = json.dumps(data, indent=1)
            f.write(data)

class Variables:

    def __init__(self, contract_address="0x4bfa950992e1dc32b622414e30886082c2bbea95", abi='[{"inputs":[],'
                '"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"TotalMarketCapUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatest1inchEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatest1inchUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAaveUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAdaUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAlcxEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAlcxUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAtomEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAtomUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAudUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestAvaxUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBadgerEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBadgerUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBalEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBalUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBandEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBnbEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBnbUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBtcEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestBtcUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestCadUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestCakeUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestCrvEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestCrvUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestDotUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestEnjEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestEnjUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestEthUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestEurUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestFilUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestGbpUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestGldUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestInrUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestJpyUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestKsmUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestLinkEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestLinkUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestLtcUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestMakerEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestMakerUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestManaEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestManaUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestMaticUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestOilUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestPerpEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestPerpUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestRuneEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestSilUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestSolUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestSushiEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestSushiUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestUniEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestUniUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestXmrUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestXrpUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestYfiEth",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLatestYfiUsd",'
                '"outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"",'
                '"type":"uint256"}],"stateMutability":"view","type":"function"}]',
                 contract="", data_prices=None, keys=None, widget_keys=None, run_time=True, updated_timestamp=""):

        if widget_keys is None:
            widget_keys = []
        if data_prices is None:
            data_prices = {}
        if keys is None:
            keys = []

        self.contract_address = contract_address
        self.abi = abi
        self.contract = contract
        self.data_prices = data_prices
        self.keys = keys
        self.widget_keys = widget_keys
        self.run_time = run_time
        self.updated_timestamp = updated_timestamp

settings_price_tracker = Settings("PriceTrackerSettings.json")
variables_tracker = Variables()