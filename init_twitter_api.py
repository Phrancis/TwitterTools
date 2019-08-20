import json
from typing import Dict


def initialize_api() -> None:
    print('Initializing Twitter API.')
    print('1: Go to https://developer.twitter.com/en/apps')
    print('2: Log in with your Twitter Developer account. If you don\'t have one, you\'ll have to request one first')
    print('3: If you have created an app already, click the "Details" button. If not, then create one and follow the steps.')
    print('4: Click the "Keys and tokens" link.')
    print('5: You will need both "Consumer API keys" (automatic) and "Access token & access token secret". Generate the 2nd set if needed.')
    print('6: Copy-paste or enter the following values from that page (input is CASE-SENSITIVE) and press Enter. Values will be saved locally for later use.')

    api_key: str = input('Enter API key: ').strip()
    api_secret: str = input('Enter API secret key: ').strip()
    access_token: str = input('Enter Access token: ').strip()
    access_secret: str = input('Enter Access token secret: ').strip()

    # Write values to file
    with open('app_data/twitter_api_keys.json', 'w') as f:
        data: Dict = dict(
            api_key=api_key,
            api_secret=api_secret,
            access_token=access_token,
            access_secret=access_secret)
        json.dump(data, f)
    print('Twitter API data saved locally.')


if __name__ == '__main__':
    initialize_api()
