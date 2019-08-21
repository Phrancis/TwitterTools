import datetime
import os
from typing import List, TextIO

import tweepy

from api import get_twitter_api as api

PATH_TO_APP_DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data')


def extract_all_user_followers_ids(screen_name: str = '') -> str:
    """
    Get all of an account's followers' user IDs and write them to a JSON file with today's date.
    :param screen_name: The screen name of the account to query. If left blank, will use the API user's screen name.
    :return: The file path where the queried data was written.
    """
    _api = api.get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))
    if screen_name == '':
        screen_name = api.get_current_user_json_field('screen_name')
    _output_file_name = f'user_followers_ids {screen_name} {datetime.date.today()}.txt'
    _output_file_path = os.path.join(PATH_TO_APP_DATA, _output_file_name)
    _followers_count: int = 0
    for page in tweepy.Cursor(_api.followers_ids, screen_name=screen_name).pages():
        _output_file: TextIO
        with open(_output_file_path, 'w') as _output_file:
            for item in page:
                _output_file.write(f'{item}\n')
    return _output_file_path


if __name__ == '__main__':
    output_file_path: str = extract_all_user_followers_ids()
    print(f'Results saved to file: {output_file_path}')
    followers_count: int = 0
    with open(output_file_path, 'r') as file:
        for line in file.read().splitlines():
            followers_count += 1
    print(f'Follower IDs saved: {followers_count}')
