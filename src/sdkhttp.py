import requests
import json
from requests.auth import HTTPBasicAuth


class HTTPClient:

    def __init__(self, api_uri, user, password, options):
        # type: (string, string, string, Dict[str, bool]) -> HTTPClient

        self.api_uri = api_uri
        self.user = user
        self.password = password
        self.options = options

    def __make_authenticated_get_request(self, url, payload=None):
        # type: (string, Dict) -> requests.Response
        if payload is None:
            payload = {}
        auth_token = self.authenticate()

        response = requests.get(
            url,
            headers={
                'salkku-auth-token': auth_token
            },
            params=payload,
            verify=self.options['verify'],
            allow_redirects=False
        )
        if self.options['verbose']:
            print("GET {}".format(response.url))
        if response.status_code != requests.codes.ok:
            if self.options['verbose']:
                print(response.text)
            response.raise_for_status()

        return response

    def __make_authenticated_post_request(self, url, post_data=None, auth_token=None, headers=None):
        # type: (string, Dict, string, Dict) -> requests.Response
        if headers is None:
            headers = {}
        if post_data is None:
            post_data = {}
        if auth_token is None:
            auth_token = self.authenticate()

        headers['salkku-auth-token'] = auth_token
        response = requests.post(
            url,
            headers=headers,
            data=post_data,
            verify=self.options['verify'],
            allow_redirects=False
        )
#        print(post_data)
        if self.options['verbose']:
            print("POST {}".format(response.url))
        if response.status_code != requests.codes.ok:
            if self.options['verbose']:
                print(response.text)
            response.raise_for_status()

        return response

    def __post_json(self, url, post_data, auth_token=None, headers=None):
        if headers is None:
            headers = {}
        headers['Content-Type'] = 'application/json'
        return self.__make_authenticated_post_request(url, json.dumps(post_data), auth_token, headers)

    def authenticate(self):
        # type: () -> str
        url = '{}/login'.format(self.api_uri)

        response = requests.post(
            url,
            auth=HTTPBasicAuth(self.user, self.password),
            verify=self.options['verify'],
            allow_redirects=False
        )
        if self.options['verbose']:
            print("POST {}".format(response.url))

        auth_token = ""
        if response.status_code == requests.codes.ok:
            auth_token = response.headers.get('salkku-auth-token')
        else:
            if self.options['verbose']:
                print(response.text)
            response.raise_for_status()

        return auth_token

    def ping(self):
        url = '{}/ping'.format(self.api_uri)
        return self.__make_authenticated_get_request(url)

    def get_currencies(self):
        if self.options['verbose']:
            print("Getting list of currencies...")

        url = '{}/currency'.format(self.api_uri)
        return self.__make_authenticated_get_request(url)

    def get_exchanges(self):
        if self.options['verbose']:
            print("Getting list of exchanges...")

        url = '{}/exchange'.format(self.api_uri)
        return self.__make_authenticated_get_request(url)

    def get_exchange_securities(self, exchange_id):
        if self.options['verbose']:
            print("Getting list of exchange {} securities...".format(exchange_id))

        url = '{}/exchange/{}/security'.format(self.api_uri, exchange_id)
        return self.__make_authenticated_get_request(url)

    def search_security(self, search):
        if self.options['verbose']:
            print("Searching security with \"{}\"...".format(search))
        params = {"q": search}

        url = '{}/security'.format(self.api_uri)
        return self.__make_authenticated_get_request(url, params)

    def get_security(self, security_id):
        if self.options['verbose']:
            print("Get security with id \"{}\"...".format(security_id))

        url = '{}/security/{}'.format(self.api_uri, security_id)
        return self.__make_authenticated_get_request(url)

    def get_portfolios(self):
        # type: (string, string) -> requests.Response
        if self.options['verbose']:
            print("Getting all portfolios {}...")

        url = '{}/portfolio'.format(self.api_uri)
        return self.__make_authenticated_get_request(url)

    def get_portfolio(self, portfolio_id):
        # type: (string, string) -> requests.Response
        if self.options['verbose']:
            print("Getting portfolio with id {}...".format(portfolio_id))

        url = '{}/portfolio/{}'.format(self.api_uri, portfolio_id)
        return self.__make_authenticated_get_request(url)

    def post_portfolio(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            portfolio = json.loads(f.read())

        url = '{}/portfolio'.format(self.api_uri)
        return self.__post_json(url, portfolio)

    def get_portfolio_history(self, portfolio_id):
        # type: (string, string) -> requests.Response
        if self.options['verbose']:
            print("Getting history of portfolio {}...".format(portfolio_id))

        url = '{}/portfolio/{}/history'.format(self.api_uri, portfolio_id)
        return self.__make_authenticated_get_request(url)

    def get_portfolio_performance(self, portfolio_id):
        # type: (string, string) -> requests.Response
        if self.options['verbose']:
            print("Getting performance of portfolio {}...".format(portfolio_id))

        url = '{}/portfolio/{}/performance'.format(self.api_uri, portfolio_id)
        return self.__make_authenticated_get_request(url)

    def get_portfolio_transactions(self, portfolio_id, api_format):
        # type: (string, string) -> requests.Response
        if self.options['verbose']:
            print("Getting transactions of portfolio {}...".format(portfolio_id))

        if api_format is not None:
            url = '{}/portfolio/{}/transaction?format={}'.format(
                self.api_uri, portfolio_id, api_format)
        else:
            url = '{}/portfolio/{}/transaction'.format(self.api_uri, portfolio_id)
        return self.__make_authenticated_get_request(url)

    def post_portfolio_transactions(self, portfolio_id, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            transactions = json.loads(f.read())

        for t in transactions:
            url = '{}/portfolio/{}/transaction'.format(self.api_uri, portfolio_id)
            self.__post_json(url, t)

    def get_portfolio_dividends(self, portfolio_id, api_format):
        # type: (string, string) -> requests.Response
        if self.options['verbose']:
            print("Getting dividends of portfolio {}...".format(portfolio_id))

        if api_format is not None:
            url = '{}/portfolio/{}/dividend?format={}'.format(
                self.api_uri, portfolio_id, api_format)
        else:
            url = '{}/portfolio/{}/dividend'.format(self.api_uri, portfolio_id)
        return self.__make_authenticated_get_request(url)

    def post_portfolio_dividends(self, portfolio_id, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            dividends = json.loads(f.read())

        for d in dividends:
            url = '{}/portfolio/{}/dividend'.format(self.api_uri, portfolio_id)
            self.__post_json(url, d)
