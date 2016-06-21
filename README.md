This is the Python SDK for [salkku.co](https://salkku.co) portfolio service.
It integrates with [Salkku API](https://salkku.co/developers) for functionality.

This code is released under the MIT license, [see details](LICENSE.md).

# Install

To use this SDK, install Python 3. For example, to install Python 3 in Debian:

`apt-get install python3 python3-pip`

This SDK uses "requests" python module. You may have to install it via pip:
`pip3 install requests`

# Usage

* All commands need user and password as argument:
`python3 src/salkku-cli.py ping --user="yourusername" --password="yourpassword"`
* Using -v switch outputs verbose stuff:
`python3 src/salkku-cli.py -v ping`
* To pretty print JSON output:
`python3 src/salkku-cli.py ping | python3 -m json.tool`

## Actions

Ping API:
`python3 src/salkku-cli.py ping --user="yourusername" --password="yourpassword"`

Get list of available currencies:
`python3 src/salkku-cli.py currency --user="yourusername" --password="yourpassword"`

Get list of available exchanges:
`python3 src/salkku-cli.py exchange --user="yourusername" --password="yourpassword"`

Search securities:
`python3 src/salkku-cli.py security --user="yourusername" --password="yourpassword" --name="apple"`

Get security with id:
`python3 src/salkku-cli.py security --user="yourusername" --password="yourpassword" --id="100"`

Get list of your portfolios:
`python3 src/salkku-cli.py portfolio --user="yourusername" --password="yourpassword"`

Get portfolio info:
`python3 src/salkku-cli.py portfolio --user="yourusername" --password="yourpassword" --id="1"`

Get portfolio history:
`python3 src/salkku-cli.py portfolio-history --user="yourusername" --password="yourpassword" --id="1"`

Get portfolio performance:
`python3 src/salkku-cli.py portfolio-performance --user="yourusername" --password="yourpassword" --id="1"`

Get portfolio transactions in specified format ("json" (default) or "csv"):
`python3 src/salkku-cli.py portfolio-transaction --user="yourusername" --password="yourpassword" --id="1" --format="csv"`

Get portfolio dividends in specified format ("json" (default) or "csv"):
`python3 src/salkku-cli.py portfolio-dividend --user="yourusername" --password="yourpassword" --id="1" --format="csv"`
