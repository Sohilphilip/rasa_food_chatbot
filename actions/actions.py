# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from excel_fetch_data import *


class ActionFetchCuisieneData(Action):
    def name(self) -> Text:
        return "action_fetch_cuisiene_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cuisine_type = tracker.get_slot("Cuisine Type")

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisineData('Food Name',cuisine_type))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []
    
class ActionFetchCaloriesData(Action):
    def name(self) -> Text:
        return "action_fetch_calories_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        calories = int(tracker.get_slot("Calories1"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCaloriesData('Food Name',calories))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchPriceData(Action):
    def name(self) -> Text:
        return "action_fetch_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        price = int(tracker.get_slot("Price1"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchPriceData('Food Name',price))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchNutrientsData(Action):

    def name(self) -> Text:
        return "action_fetch_food_nutrient_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food_name = tracker.get_slot("Food Name")
        response = get_food_info(food_name)

        if response:
            food_calories = response.get('calories')
            food_name_asked = response.get('name')
            food_serve_size = response.get('serving_size_g')
            protein = response.get('protein_g')
            carbohydrate = response.get('carbohydrates_total_g')
            total_fat = response.get('fat_total_g')
            saturated_fat = response.get('fat_saturated_g')
            fibers = response.get('fiber_g')
            sugar = response.get('sugar_g')
            sodium = response.get('sodium_mg')
            potassium = response.get('potassium_mg')
            cholesterol = response.get('cholesterol_mg')

            message = f"{food_serve_size} grams of {food_name_asked} contains the following:\n{protein} grams of protein,\n{carbohydrate} grams of carbohydrate,\n{total_fat} grams of total fat,\n{saturated_fat} grams of saturated fat,\n{fibers} grams of fibers,\n{sugar} grams of sugar,\n{sodium} milligrams of sodium,\n{potassium} milligrams of potassium,\n{cholesterol} milligrams of cholesterol.\nThe total amount of calories present in {food_name_asked} is {food_calories} cal"
        else:
            message = "Sorry, I couldn't find information about that food item."

        dispatcher.utter_message(message)
        
        return []
    

class ActionFetchBtwCaloriesData(Action):
    def name(self) -> Text:
        return "action_fetch_btw_calories_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        calories1 = int(tracker.get_slot("Calories1"))
        calories2 = int(tracker.get_slot("Calories2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchBtwCaloriesData('Food Name',calories1,calories2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchBtwPriceData(Action):
    def name(self) -> Text:
        return "action_fetch_btw_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        price1 = int(tracker.get_slot("Price1"))
        price2 = int(tracker.get_slot("Price2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisineData('Food Name',price1,price2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchBtwCaloriesBtwPriceData(Action):
    def name(self) -> Text:
        return "action_fetch_btw_calories_btw_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        calories1 = int(tracker.get_slot("Calories1"))
        calories2 = int(tracker.get_slot("Calories2"))
        price1 = int(tracker.get_slot("Price1"))
        price2 = int(tracker.get_slot("Price2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchBtwCaloriesAndBtwPrice('Food Name',price1,price2,calories1,calories2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionMainNutrientData(Action):
    def name(self) -> Text:
        return "action_fetch_main_nutrient_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nutrient = tracker.get_slot("Main Nutrient")

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchNutrientData('Food Name',nutrient))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchCuisienePriceData(Action):
    def name(self) -> Text:
        return "action_fetch_cuisine_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cuisine_type = tracker.get_slot("Cuisine Type")
        price = int(tracker.get_slot("Price1"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisineAndPriceData('Food Name',cuisine_type,price))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchCuisieneBtwPriceData(Action):
    def name(self) -> Text:
        return "action_fetch_cuisine_btw_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cuisine_type = tracker.get_slot("Cuisine Type")
        price1 = int(tracker.get_slot("Price1"))
        price2 = int(tracker.get_slot("Price2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisineAndBtwPriceData('Food Name',cuisine_type,price1,price2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []


class ActionFetchCuisieneCaloriesData(Action):
    def name(self) -> Text:
        return "action_fetch_cuisine_calories_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cuisine_type = tracker.get_slot("Cuisine Type")
        calories = int(tracker.get_slot("Calories1"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisineAndCaloriesData('Food Name',cuisine_type,calories))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchCuisieneBtwCaloriesData(Action):
    def name(self) -> Text:
        return "action_fetch_cuisine_btw_calories_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cuisine_type = tracker.get_slot("Cuisine Type")
        calories1 = int(tracker.get_slot("Calories1"))
        calories2 = int(tracker.get_slot("Calories2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisineAndBtwCaloriesData('Food Name',cuisine_type,calories1,calories2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchCuisieneBtwCaloriesBtwPriceData(Action):
    def name(self) -> Text:
        return "action_fetch_cuisine_btw_calories_btw_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cuisine_type = tracker.get_slot("Cuisine Type")
        calories1 = int(tracker.get_slot("Calories1"))
        calories2 = int(tracker.get_slot("Calories2"))
        price1 = int(tracker.get_slot("Price1"))
        price2 = int(tracker.get_slot("Price2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchCuisieneAndBtwCaloriesAndBtwPrice('Food Name',cuisine_type,price1,price2,calories1,calories2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []

class ActionFetchNutrientsBtwPriceData(Action):
    def name(self) -> Text:
        return "action_fetch_main_nutrient_btw_price_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nutrient = tracker.get_slot("Main Nutrient")
        price1 = int(tracker.get_slot("Price1"))
        price2 = int(tracker.get_slot("Price2"))

        # Generate response using the extracted entities
        response = "Here are my Reccomendations:\n" + " ,\n".join(fetchNutrientAndBtwPriceData('Food Name',nutrient,price1,price2))

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []
    
