import os
import pandas as pd
import requests

#action_fetch_cuisiene_data
def fetchCuisineData(column, Cuisine_Type):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        data = df[column][df['Cuisine Type'] == Cuisine_Type]
        return data.tolist()  # Changed to .tolist() for conversion to list
    else:
        return "Data file not found"

#action_fetch_calories_data
def fetchCaloriesData(column , Calories):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        data = df[column][df['Calories'] == Calories]
        return data.tolist()  # Changed to .tolist() for conversion to list
    else:
        return "Data file not found"

#action_fetch_btw_calories_data
def fetchBtwCaloriesData(column, Calories1, Calories2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Calories' column to numeric type (assuming it contains numeric values)
        df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
        
        # Filter rows where 'Calories' column lies between Calories1 and Calories2
        filtered_data = df.loc[(df['Calories'] >= Calories1) & (df['Calories'] <= Calories2), column]
        
        return filtered_data.tolist()
    else:
        return "Data file not found"

#action_fetch_price_data
def fetchPriceData(column, Price):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        # Check if 'Price' is in the columns of the DataFrame
        if 'Price ' in df.columns:
            # Filter rows where 'Price' column matches the specified Price
            data = df[column][df['Price '] == Price]
            return data.tolist()  # Changed to .tolist() for conversion to list
        else:
            return "Column 'Price' not found in the DataFrame"
    else:
        return "Data file not found"

#action_fetch_btw_price_data
def fetchBtwPriceData(column, Price1, Price2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Calories' column to numeric type (assuming it contains numeric values)
        df['Price '] = pd.to_numeric(df['Price '], errors='coerce')
        
        # Filter rows where 'Calories' column lies between Calories1 and Calories2
        filtered_data = df.loc[(df['Price '] >= Price1) & (df['Price '] <= Price2), column]
        
        return filtered_data.tolist()
    else:
        return "Data file not found"

#action_fetch_food_nutrient_data
def get_food_info(query):
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': '9zgtS5Nw1JEBMT0WwBUmqg==qLBr4xemmDM5dlVi'}).json()
    if response and len(response) > 0:
        return response[0]
    
#action_fetch_main_nutrient_data
def fetchNutrientData(column, Nutrient):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        # Check if 'Nutrient' is in the columns of the DataFrame
        if 'Most Intensive Nutrient' in df.columns:
            # Filter rows where 'Price' column matches the specified Price
            data = df[column][df['Most Intensive Nutrient'] == Nutrient]
            return data.tolist()  # Changed to .tolist() for conversion to list
        else:
            return "Column 'Most Intensive Nutrient' not found in the DataFrame"
    else:
        return "Data file not found"

#action_fetch_cuisine_price_data
def fetchCuisineAndPriceData(column,cuisine,price):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        filtered_df = df[(df['Cuisine Type'] == cuisine) & (df['Price '] == price)]
        food_names = filtered_df['Food Name'].tolist()

        return food_names
    else:
        return "Data file not found"
    
#action_fetch_cuisine_btw_price_data
def fetchCuisineAndBtwPriceData(column, cuisine, price1, price2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Price' column to numeric
        df['Price '] = pd.to_numeric(df['Price '], errors='coerce')
        
        filtered_df = df[(df['Cuisine Type'] == cuisine) & (df['Price '].between(price1, price2))]
        food_names = filtered_df[column].tolist()

        return food_names
    else:
        return "Data file not found"

#action_fetch_cuisine_calories_data
def fetchCuisineAndCaloriesData(column,cuisine,calories):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        filtered_df = df[(df['Cuisine Type'] == cuisine) & (df['Calories'] == calories)]
        food_names = filtered_df['Food Name'].tolist()
        return food_names
    else:
        return "Data file not found"
    
#action_fetch_cuisine_btw_calories_data
def fetchCuisineAndBtwCaloriesData(column, cuisine, calories1, calories2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Price' column to numeric
        df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
        
        filtered_df = df[(df['Cuisine Type'] == cuisine) & (df['Calories'].between(calories1, calories2))]
        food_names = filtered_df[column].tolist()

        return food_names
    else:
        return "Data file not found"
    
#action_fetch_cuisine_btw_calories_btw_price_data
def fetchCuisieneAndBtwCaloriesAndBtwPrice(cuisine, price1, price2, calorie1, calorie2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Price' and 'Calories' columns to numeric
        df['Price '] = pd.to_numeric(df['Price '], errors='coerce')
        df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
        
        # Filter based on cuisine, price, and calorie ranges
        filtered_df = df[(df['Cuisine Type'] == cuisine) &
                         (df['Price '].between(price1, price2)) &
                         (df['Calories'].between(calorie1, calorie2))]
        
        # Extract food names
        food_names = filtered_df['Food Name'].tolist()

        return food_names
    else:
        return "Data file not found"

#action_fetch_btw_calories_btw_price_data
def fetchBtwCaloriesAndBtwPrice(price1, price2, calorie1, calorie2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Price' and 'Calories' columns to numeric
        df['Price '] = pd.to_numeric(df['Price '], errors='coerce')
        df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
        
        # Filter based on price, and calorie ranges
        filtered_df = df[(df['Price '].between(price1, price2)) &
                         (df['Calories'].between(calorie1, calorie2))]
        
        # Extract food names
        food_names = filtered_df['Food Name'].tolist()

        return food_names
    else:
        return "Data file not found"

#action_fetch_main_nutrient_btw_price_data
def fetchNutrientAndBtwPriceData(column, nutrient, price1, price2):
    if os.path.isfile("Food Information.xlsx"):
        df = pd.read_excel("Food Information.xlsx")
        
        # Convert 'Price' column to numeric
        df['Price '] = pd.to_numeric(df['Price '], errors='coerce')
        
        filtered_df = df[(df['Most Intensive Nutrient'] == nutrient) & (df['Price '].between(price1, price2))]
        food_names = filtered_df[column].tolist()

        return food_names
    else:
        return "Data file not found"
    