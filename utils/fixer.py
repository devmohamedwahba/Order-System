import requests
import logging

logger = logging.getLogger(__name__)


# base_url = 'http://data.fixer.io/api/latest?access_key=34e2df461e05e5871c51b4293d8a62c8'


class FixerApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_exchange_rate_base_euro(self):
        try:
            data = requests.get(self.base_url)
        except Exception as e:
            logger.error(f'thew is an error happened in calling api {e}')
        else:
            return data.json()

