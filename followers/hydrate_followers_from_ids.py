import os
import json
from typing import TextIO, List

import tweepy
from tweepy import TweepError

from api import get_twitter_api as tweepy_api

PATH_TO_APP_DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data')
api = tweepy_api.get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))


def hydrate_followers_from_ids(input_file_path: str) -> None:
    # Read file and parse into a list of user IDs
    followers_ids_input_file: TextIO
    all_followers_ids_list: List
    with open(input_file_path, 'r') as followers_ids_input_file:
        all_followers_ids_list = followers_ids_input_file.read().splitlines()
    all_followers_hydrated_list: List = []
    # Iterate list of all followers, 100 at a time, because that's the max the Twitter API allows per request
    for i_100_followers_slice in range(0, len(all_followers_ids_list), 100):
        # Slice 100 IDs from followers
        short_100_list: List = all_followers_ids_list[i_100_followers_slice:i_100_followers_slice + 100]
        # Query Twitter API with the 100 IDs
        hydrated_short_100_list: List = api.lookup_users(user_ids=short_100_list)
        # Testing adding from short list
        for user_entry in hydrated_short_100_list:
            all_followers_hydrated_list.append(user_entry)
    # Testing running through whole list
    for i_item in range(0, len(all_followers_hydrated_list)):
        print(f'{i_item}\t{all_followers_hydrated_list[i_item]._json}')


if __name__ == '__main__':
    # Temporary hard-coding file path
    _input_file_path = os.path.join(PATH_TO_APP_DATA, 'user_followers_ids francisveegee 2019-08-23.txt')
    hydrate_followers_from_ids(_input_file_path)
