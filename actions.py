from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import emailsender as sender, helper, message_composer
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		print("inside run:: ")
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"

		response = response + "\n\n Would you like me to share this information on your email ?"
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		print("tracker:: ")
		print(tracker.current_slot_values())

		# get all slot values.
		# at this point we assume all the valid slots are filled and the information provided is correct
		loc = helper.get_slot_value(tracker, 'location')
		cuisine = helper.get_slot_value(tracker, 'cuisine')
		budget = helper.get_slot_value(tracker, 'budget')
		email = helper.get_slot_value(tracker, 'user_email')

		if not helper.is_valid_email(email):
			dispatcher.utter_message("It seems that the given email is  invalid. Can you please provide me a correct email?")
			return [SlotSet('user_email',None)]


		# getting city search on zomato
		cityObj = helper.get_city_details(loc)

		if cuisine in cuisine_dict:
			cuisine_search_param = cuisine_dict.get(cuisine)
		else:
			cuisine_search_param = ""

		results=zomato.restaurant_search(query="", latitude=lat, longitude=lon, cuisines=cuisine_search_param, limit=10)
		dresults = json.loads(results)

		# @TODO::  if price filter then apply filter price records

		if dresults['results_found'] == 0:
			dispatcher.utter_message("I was unable to find the requested data for sending the email.")
			return [SlotSet('user_email',None)]
			pass
		else:
			# we have results. parse and show them
			mail_subject = helper.prepare_email_subject(tracker);
			html = message_composer.get_message_email(dresults, mail_subject)

			try:
				sender.send_email_message(mail_subject, email, html)
				dispatcher.utter_message("Email sent to " + email)
				return [SlotSet('user_email',email)]
			except Exception as e:
				print(e)
				dispatcher.utter_message("I am facing a problem in sending the email. \n Please try again in sometime.")
				return [SlotSet('user_email',None)]