## complete path with send mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_ask_email
* send_email{"user_email": "nomail@gmail.com"}
    - action_send_email
    - slot{"user_email": "nomail@gmail.com"}
    - utter_goodbye
    - export


## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_ask_email
* send_email{"user_email": "nomail@gmail.com"}
    - action_send_email
    - slot{"user_email": "nomail@gmail.com"}
    - utter_goodbye
    - export

## interactive_story_1
* greet

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* information{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - utter_ask_cuisine
* information{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* information
    - action_search_restaurants
    - slot{"location": "Lucknow"}
* affirm
    - utter_ask_email
    - action_send_email

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* information{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - utter_ask_cuisine
* information{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* information{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
* affirm
    - utter_ask_email
* send_email{"user_email": "nomail@gmail.com"}
    - slot{"user_email": "nomail@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
