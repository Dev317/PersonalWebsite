import os
import yaml
from typing import Dict


def get_config() -> Dict:
    config_file_path = f"{os.getcwd()}/config.yaml"
    with open(file=config_file_path,
              mode="r") as config_file:
        config = yaml.load(stream=config_file,
                           Loader=yaml.FullLoader)
    return config
