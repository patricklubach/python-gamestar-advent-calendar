import configparser
import datetime

import mechanize

# Read the ini file
config = configparser.ConfigParser()
config.sections()
config.read("config.ini")

# Current day
day = datetime.datetime.now().day

# Url with current day
url = f"https://www.gamestar.de/kalender/xmas2022,10/tag{str(day)}.html"

br = mechanize.Browser()

br.set_handle_robots(False)
br.addheaders = [("User-agent", "Mozilla/63.0.3")]
br.open(url)
br.select_form(nr=0)
form = br.form

form["firstname"] = config.get("FormData", "firstname")
form["lastname"] = config.get("FormData", "lastname")
form["street"] = config.get("FormData", "street")
form["streetext"] = config.get("FormData", "streetnumber")
form["additionalAddressInfo"] = config.get("FormData", "adressext")
form["zipcode"] = config.get("FormData", "zipcode")
form["city"] = config.get("FormData", "city")
form["country"] = [config.get("FormData", "country")]
form["email"] = config.get("FormData", "email")
form["age"] = config.get("FormData", "age")

br.find_control("usage").items[0].selected = True

response = br.submit()

print("done")
