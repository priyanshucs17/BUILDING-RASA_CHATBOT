import json, re
import constants

def get_slot_value(tracker, slot_name):
    return str(tracker.get_slot(slot_name)).lower()

def is_servicable_city(city_name):
    return city_name in constants.allowed_cities

def is_valid_cuisine(cuisine_name):
    return cuisine_name in constants.allowed_cuisines

def map_budget(budget_value):
    pass

def prepare_email_subject(tracker):
    loc = get_slot_value(tracker, 'location')
    cuisine = get_slot_value(tracker, 'cuisine')
    # budget = get_slot_value(tracker, 'budget')

    return "Your {}restaurant search in {}.".format(cuisine + " ", loc)


def is_valid_email(email):
    pattern = "([^@|\s]+@[^@]+\.[^@|\s]+)"
    return re.match(pattern, email, re.M|re.I)


def get_city_details(city_name):
    return filter(lambda x: x.get("city_name").lower() == city_name, constants.allowed_cities_data)