# Python automation for participation @ GameStar.de advent calendar

This script submits your details at the gamestar.de advent calendar, so you won't miss out one of the giveaways.

*Note: This script works with python3!*

## Dependencies

Install dependencies in a virtual environment:

```shell
pip3 install --user virtualenv
virtualenv venv
source venv/bin/activate

venv/bin/pip3 install -r requirements.txt
```

## Usage

Set your details in the [`config.ini`](./config.ini) file.

```shell
python3 submit.py
```

Example cronjob: `10 09 * * * cd /home/siw/python-gamestar-advent-calendar && python3 submit.py >/dev/null 2>&1`
