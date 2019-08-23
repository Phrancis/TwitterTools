import os
from typing import TextIO, List

import tweepy
from tweepy import TweepError

from api import get_twitter_api as tweepy_api

PATH_TO_APP_DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data')
api = tweepy_api.get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))


def hydrate_followers_from_ids(input_file_path: str) -> None:
    # Read file and parse into a list of user IDs
    followers_ids: TextIO
    followers_ids_list: List
    with open(input_file_path, 'r') as followers_ids:
        followers_ids_list = followers_ids.read().splitlines()
    # Iterate list to query API, 100 at a time
    for user_id_index in range(0, len(followers_ids_list), 100):
        current_list: List = followers_ids_list[user_id_index:user_id_index + 100]
    # Following is for testing only
        for item_index in range(0, len(current_list)):
            print(f'{user_id_index + item_index} : {followers_ids_list[user_id_index + item_index]}')
        print(f'Printed {len(current_list)} items')
    print(f'All Done. Total {len(followers_ids_list)}')


if __name__ == '__main__':
    # Temporary hard-coding file path
    _input_file_path = os.path.join(PATH_TO_APP_DATA, 'user_followers_ids francisveegee 2019-08-23.txt')
    hydrate_followers_from_ids(_input_file_path)
