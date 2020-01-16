
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* information{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
* information{"location": "delhi"}
    - slot{"location": "delhi"}
* greet

## interactive_story_2
* greet

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* information{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* send_email{"user_email": "nomail@gmail.com"}
    - slot{"user_email": "nomail@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
