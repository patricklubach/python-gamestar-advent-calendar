# Python automation for participation @ GameStar.de advent calendar

This script submits your details at the gamestar.de advent calendar, so you won't miss out one of the giveaways.

*Note: This script works with python3!*

## Dependencies

Install dependencies in a virtual environment:

```shell
pip3 install --user virtualenv
virtualenv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

Create a `config.ini` file by copying the `config.ini.example` file:

```bash
cp config.ini.example config.ini
```

Fill out all the configurations in the `FormatData` section and then run:

```bash
python3 main.py
```

## Run scheduled

In order to run the script on a daily schedule add the following line to your crontab (`crontab -e`):

```bash
# Example cronjob:
10 09 * * * cd /home/siw/python-gamestar-advent-calendar && python3 main.py >/dev/null 2>&1
```
