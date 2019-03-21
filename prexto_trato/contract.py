import json
import requests

from .settings import API_URL, TOKEN_AUTH


class Contract(object):
    def __init__(self, contract_id, debug=False):
        self.debug = debug
        self.api_url = API_URL
        self.token_auth = TOKEN_AUTH

        self.contract_id = contract_id

    def configurate(self, data):
        endpoint = '/configuration/{}'.format(self.contract_id)

        return self.__make_request(endpoint, method='post', data=data)

    def set_vars(self, participant_id, data):
        endpoint = '/variables/{}/{}'.format(self.contract_id, participant_id)

        return self.__make_request(endpoint, method='post', data=data)

    def get_vars(self):
        endpoint = '/variables/{}'.format(self.contract_id)

        return self.__make_request(endpoint)

    def set_participant(self, participant_id, data):
        endpoint = '/participant/{}/{}'.format(self.contract_id, participant_id)

        return self.__make_request(endpoint, method='post', data=data)

    def get_participant(self, participant_id):
        endpoint = '/participant/{}/{}'.format(self.contract_id, participant_id)

        return self.__make_request(endpoint) 

    def to_sign(self):
        endpoint = '/send/{}'.format(self.contract_id)

        return self.__make_request(endpoint, method='post')

    def __make_request(self, uri='', method='get', data=None):
        headers = {        
            'Content-Type':'application/json',
            'Authorization': 'Bearer {}'.format(self.token_auth)
        }

        url = '{}{}'.format(self.api_url, uri)

        if data:
            data = json.dumps(data)

        response = getattr(requests, method)(url, headers=headers, data=data)

        response_status = response.status_code
        response_content = response.content.decode()

        if self.debug:
            print('\n\nurl: {}\nstatus: {}\ncontent: {}\n\n'.format(url, response_status, response_content))

        if response_status == 200:
            return json.loads(response.content)

        raise Exception(response_content)
