# 🍽️ AI Food Recommendation Chatbot with Rasa

Your **personal food assistant**, built using [Rasa](https://rasa.com/), that helps you discover delicious meals based on your **nutritional needs**, **budget**, and **taste preferences** — all through **natural conversation**.  
Whether you're counting calories, managing macros, or just looking for cuisine-specific options — this chatbot has you covered.

---

## 💡 Key Features

- 🧠 Built with **Rasa Open Source**
- 📊 Uses **Excel-based food database**
- 🌐 **Nutrition API** integration for real-time info
- 🔍 Smart filtering based on:
  - Calories (exact or range)
  - Price (exact or budget)
  - Cuisine (e.g., Indian, Italian, etc.)
  - Nutrients (Protein-rich, Low-Carb, etc.)
  - Combined filters for personalized results
- 📥 Simple Excel integration, no complex databases
- 🤖 Fully customizable with new intents/actions

---

## 🛠️ How It Works

1. **User chats** with the bot:  
   ➤ “Find Chinese food between 400–700 calories.”  
   ➤ “Show me low-carb dishes under $10.”  
   ➤ “What’s the nutritional breakdown of pasta?”

2. **Rasa NLU** extracts slots like:
   - `calories`, `price`, `cuisine`, `nutrient`, etc.

3. **Custom actions**:
   - Pull from `Food Information.xlsx`
   - Use filtering logic in `excel_fetch_data.py`
   - Optionally call Nutrition API for fresh data

4. **Response delivered** in friendly, readable format

---

## 📁 Code Structure

```
├── actions/
│   └── actions.py               # Custom action logic
├── excel_fetch_data.py         # Excel-based filtering functions
├── domain.yml                  # Intent-slot-action configuration
├── data/
│   └── nlu.yml                 # Training examples
├── Food Information.xlsx       # Food dataset
└── README.md                   # You're here!
```

---

## 🧠 Core Logic (Sample Action)

```python
class ActionFetchCaloriesData(Action):
    def name(self) -> Text:
        return "action_fetch_calories_data"

    def run(self, dispatcher, tracker, domain):
        calories = int(tracker.get_slot("Calories1"))
        response = "Here are my Recommendations:
" + " ,
".join(fetchCaloriesData('Food Name', calories))
        dispatcher.utter_message(text=response)
        return []
```

This fetches foods from Excel that match the given calorie count.

---

## 📡 Real-Time Nutrient Lookup (API)

```python
def get_food_info(query):
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    return response.json()
```

---

## 🔍 Example Queries Supported

| Query Type                        | Sample Input                                      |
|----------------------------------|--------------------------------------------------|
| Calories only                    | “Foods with 500 calories”                        |
| Price range                      | “Meals under $15”                                |
| Cuisine filter                   | “Show me Italian food”                           |
| Nutrient-based                   | “High protein foods”                             |
| Combo filters                    | “Chinese food under 600 calories and $10”        |
| Nutritional breakdown (API)      | “What are the macros in pizza?”                  |

---

## 📊 Data Sample (Excel)

| Food Name | Cuisine | Calories | Price | Nutrient |
|-----------|---------|----------|-------|----------|
| Pizza     | Italian | 266      | 8     | Carbs    |
| Tofu Bowl | Asian   | 320      | 10    | Protein  |

---

## 🚀 Setup Guide

1. Clone the repo  
   `git clone https://github.com/Sohilphilip/rasa_food_chatbot.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Train the model  
   `rasa train`

4. Run actions server  
   `rasa run actions`

5. Launch the chatbot  
   `rasa shell`

---

## 🖼️ Demo Preview

![Chatbot Demo](https://github.com/Sohilphilip/rasa_food_chatbot/blob/main/chatbot%20demo.gif?raw=true)

---
