import argparse
import sdkhttp

DEFAULT_HOST = "https://salkku.co"

options = {
    'verbose': False
}


def parse_command_line():
    # type: () -> Namespace
    parser = argparse.ArgumentParser(description='CLI commands for paaomat.fi.')
    parser.add_argument('command', help='Main command name')
    parser.add_argument('--data', help='Post data file')
    parser.add_argument('--host', help='Salkku host address', default=DEFAULT_HOST)
    parser.add_argument('--user', help='HTTP auth user')
    parser.add_argument('--password', help='HTTP auth password')
    parser.add_argument('--id', help='Optional resource id', type=int)
    parser.add_argument('--email', help='Optional user email')
    parser.add_argument('--date', help='Begin date')
    parser.add_argument('--name', help='Optional resource name')
    parser.add_argument('--format', help='API response format')
    parser.add_argument('-v', '--verbose', action='store_true',
                        dest="verbose", help='Verbose output')
    parser.add_argument('-d', '--dev', action='store_true',
                        dest="debug", help='Development mode')

    args = parser.parse_args()

    return args


def main():
    args = parse_command_line()

    if args.verbose:
        options['verbose'] = True
    if args.debug:
        options['verify'] = False
    else:
        options['verify'] = True

    api_url = '{}/api/v1'.format(args.host)
    client = sdkhttp.HTTPClient(api_url, args.user, args.password, options)

    if args.command == "currency":
        stdout(client.get_currencies())
    elif args.command == "exchange":
        stdout(client.get_exchanges())
    elif args.command == "exchange-security":
        if args.id is not None:
            stdout(client.get_exchange_securities(args.id))
        else:
            raise Exception("Need exchange id")
    elif args.command == "transaction-type":
        stdout(client.get_transaction_types())
    elif args.command == "security":
        if args.name is not None:
            stdout(client.search_security(args.name))
        elif args.id is not None:
            stdout(client.get_security(args.id))
    elif args.command == "portfolio":
        if args.data is not None:
            stdout(client.post_portfolio(args.data))
        elif args.id is not None:
            stdout(client.get_portfolio(args.id))
        else:
            stdout(client.get_portfolios())
    elif args.command == "portfolio-history":
        if args.id is not None:
            stdout(client.get_portfolio_history(args.id))
        else:
            raise Exception("Need portfolio id")
    elif args.command == "portfolio-performance":
        if args.id is not None:
            stdout(client.get_portfolio_performance(args.id))
        else:
            raise Exception("Need portfolio id")
    elif args.command == "ping":
        stdout(client.ping())
    elif args.command == "portfolio-transaction":
        if args.id is not None:
            if args.data is not None:
                client.post_portfolio_transactions(args.id, args.data)
            else:
                stdout(client.get_portfolio_transactions(args.id, args.format))
        else:
            raise Exception("Need portfolio id")
    elif args.command == "portfolio-dividend":
        if args.id is not None:
            if args.data is not None:
                client.post_portfolio_dividends(args.id, args.data)
            else:
                stdout(client.get_portfolio_dividends(args.id, args.format))
        else:
            raise Exception("Need portfolio id")


def stdout(response):
    print(response.text)

if __name__ == "__main__":
    main()
