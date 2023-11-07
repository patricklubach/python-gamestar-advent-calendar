#!/usr/bin/env python3

import configparser
import datetime
import sys

import mechanize

# Read the ini file
config = configparser.ConfigParser()
config.read("config.ini")

base_url = config["DEFAULT"]["baseUrl"]

# Current day
day = str(datetime.datetime.now().day)

# Customizable year
year = config["DEFAULT"]["year"]

# Url with current day
full_url = f"{base_url}/xmas{year}/tag{day}.html"

br = mechanize.Browser()

br.set_handle_robots(False)
br.addheaders = [("User-agent", config["DEFAULT"]["userAgent"])]
br.open(full_url)
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

if response.code != 200:
    print("Something went wrong during form submission:")
    print(f"HTTP code: {response.code}")
    sys.exit(1)

print("done")
