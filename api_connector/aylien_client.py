import json
from aylienapiclient import textapi


class AylienClient:

    config_path = "resources/aylien_config.json"

    def __init__(self, path=config_path):
        self.config_path = path

    def connect(self):
        config = json.load(open(self.config_path, 'r'))
        return textapi.Client(config["api_id"], config["key"])
