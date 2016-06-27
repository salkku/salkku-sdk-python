This is Python SDK for [salkku.co](https://salkku.co) portfolio service.
The SDK integrates with Salkku API for functionality, see [API documentation](https://salkku.co/developers) for further
reference. The SDK is released under the MIT license, [see details](LICENSE.md).

# Install

To use this SDK, install Python 3. For example, to install Python 3 in Debian:
```
apt-get install python3 python3-pip
```

This SDK uses "requests" python module. You may have to install it via pip:
```
pip3 install requests
```

# Usage

By default, SDK outputs JSON response from API. Some actions can be instructed to return CSV instead, see below.
If API returns HTTP response code other than 200, an exception is raised.

* All commands need user and password as argument:
```
python3 src/salkku-cli.py ping --user="yourusername" --password="yourpassword"
```
* Using -v switch outputs verbose stuff:
```
python3 src/salkku-cli.py -v ping
```
* To pretty print JSON output:
```
python3 src/salkku-cli.py ping --user="yourusername" --password="yourpassword" | python3 -m json.tool
```
* POSTing data is done by adding "data" parameter:
```
python3 src/salkku-cli.py portfolio-transaction --user="yourusername" --password="yourpassword" --id="1" --data="data.json"
```

## Actions

* Ping API:
```
python3 src/salkku-cli.py ping --user="yourusername" --password="yourpassword"
```
* Get list of available currencies:
```
python3 src/salkku-cli.py currency --user="yourusername" --password="yourpassword"
```
* Get list of available exchanges:
```
python3 src/salkku-cli.py exchange --user="yourusername" --password="yourpassword"
```
* Get list of transaction types:
```
python3 src/salkku-cli.py transaction-type --user="yourusername" --password="yourpassword"
```
* Search securities:
```
python3 src/salkku-cli.py security --user="yourusername" --password="yourpassword" --name="apple"
```
* Get security with id:
```
python3 src/salkku-cli.py security --user="yourusername" --password="yourpassword" --id="100"
```
* Get list of your portfolios:
```
python3 src/salkku-cli.py portfolio --user="yourusername" --password="yourpassword"
```
* Get portfolio info:
```
python3 src/salkku-cli.py portfolio --user="yourusername" --password="yourpassword" --id="1"
```
* Post new portfolio:
```
python3 src/salkku-cli.py portfolio --user="yourusername" --password="yourpassword" --data="portfolio.json"
```
* Get portfolio history:
```
python3 src/salkku-cli.py portfolio-history --user="yourusername" --password="yourpassword" --id="1"
```
* Get portfolio performance:
```
python3 src/salkku-cli.py portfolio-performance --user="yourusername" --password="yourpassword" --id="1"
```
* Get portfolio transactions in specified format ("json" (default) or "csv"):
```
python3 src/salkku-cli.py portfolio-transaction --user="yourusername" --password="yourpassword" --id="1" --format="csv"
```
* Post portfolio transactions:
```
python3 src/salkku-cli.py portfolio-transaction --user="yourusername" --password="yourpassword" --id="1" --data="data.json"
```
* Get portfolio dividends in specified format ("json" (default) or "csv"):
```
python3 src/salkku-cli.py portfolio-dividend --user="yourusername" --password="yourpassword" --id="1" --format="csv"
```
* Post portfolio dividends:
```
python3 src/salkku-cli.py portfolio-dividend --user="yourusername" --password="yourpassword" --id="1" --data="data.json"
```
