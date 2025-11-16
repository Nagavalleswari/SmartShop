# SmartShop — AI Grocery & Meal Planner Agent

SmartShop is an AI-powered Concierge Agent that automates weekly meal planning, generates grocery lists based on pantry inventory, and recommends optimized, cost-efficient shopping plans.  
This project is developed for the **Kaggle Agents Intensive Capstone Project (Concierge Track)**.

---

## 🚀 Features

### 🧠 Multi-Agent System
- **Planner Agent** → orchestrates all steps  
- **Recipe Agent** → searches and filters recipes  
- **Pantry Tool** → calculates missing ingredients  
- **Price Estimator Tool** → groups items by aisle and estimates cost  

### 📦 Tools & Memory
- Custom tools (`RecipeSearchTool`, `PantryTool`, `PriceEstimator`)
- Long-term memory (JSON-backed `MemoryBank`)
- Supports user preferences: diet, dislikes, allergies

### 📊 Outputs
- Weekly meal plan  
- Shopping list grouped by aisle  
- Estimated cost  
- Uses pantry items to reduce waste  

---

## 📁 Project Structure

smartshop_repo/
│── README.md
│── requirements.txt
│── demo_notebook.ipynb
│── smartshop/
├── main.py
├── init.py
├── agents/
│ ├── planner_agent.py
│ └── recipe_agent.py
├── tools/
│ ├── recipe_search_tool.py
│ ├── pantry_tool.py
│ └── price_estimator.py
├── memory/
│ └── memory_bank.py
└── data/
└── recipes.json


---

## ▶️ Running the Project

### 1. Create and activate virtual environment
cd smartshop
python -m venv venv
venv\Scripts\activate
cd ..

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the SmartShop agent
python -m smartshop.main


---

## 📷 Example Output

--- Generated Plan ---

Veg Stir Fry with Noodles

Tomato Pasta

Banana Oat Smoothie

--- Grocery List ---
{ grouped: {...}, total_estimated_cost: ... }


---

## 🛠 Technologies Used

- **Python** (ADK-style agent structure)
- Multi-agent architecture  
- Custom tools  
- Memory system  
- Mock recipe dataset  
- CLI-based demo (no frontend needed)

---

## 🎯 Capstone Project Requirements Covered

- Multi-agent system  
- Tools (custom + built-in patterns)  
- Long-term memory  
- Session flow  
- Observability-compatible structure  
- Clean code + documentation  

---

## 🚧 Future Improvements

- Nutrition calculator  
- Real recipe API integration  
- Shopping price API  
- UI/website for meal planning  
- Voice-based agent  

---

## 📜 License
Open for educational and project use as part of the Kaggle Agents Intensive.

