import datetime
import os
from api import get_twitter_api as api

PATH_TO_APP_DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data')


def extract_all_follower_user_ids(screen_name: str = '') -> None:
    """
    Get all of an account's followers' user IDs and write them to a JSON file with today's date.
    :param screen_name:
    :return:
    """
    _api = api.get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))
    if screen_name == '':
        screen_name = api.get_current_user_json_field('screen_name')
    _file_name = f'follower_user_ids {screen_name} {datetime.date.today()}'
    print(_file_name)


if __name__ == '__main__':
    extract_all_follower_user_ids()
