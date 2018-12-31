import json

PLACES = (
    'Reykjavik',
    'Vien',
    'Zadar',
    'Venice',
    'Wrocaw',
    'Bolognia',
    'Berlin',
    'Slubice',
    'New York',
    'Dehli', )


def get_config():

    CONFIG_FILE = "./config.json"
    try:
        with open(CONFIG_FILE) as f:
            config = json.load(f)
            return config
    except json.decoder.JSONDecodeError as e:
        msg = f'設定ファイル：{CONFIG_FILE} を確認してください'
        raise ValueError(msg)
