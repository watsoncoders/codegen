import csv
import random
import PySimpleGUI as sg

# Sample data for different categories (same as before)
categories = ["Appetizer", "Main Course", "Dessert", "Side Dish", "Snack", "Beverage"]
dish_types = ["Salad", "Soup", "Casserole", "Pizza", "Burger", "Stew", "Stir-fry", "Pasta", "Grill", "Dessert"]
diets = ["Vegetarian", "Vegan", "Gluten-Free", "Keto", "Paleo", "Low-Carb", "High-Protein", "Dairy-Free"]
cooking_methods = ["Baking", "Grilling", "Roasting", "Frying", "Steaming", "Boiling", "Slow Cooking", "Sous Vide"]
meal_types = ["Breakfast", "Lunch", "Dinner", "Snack", "Brunch", "Dessert"]
cuisines = ["Italian", "Chinese", "Indian", "Mexican", "French", "Greek", "Japanese", "Thai", "American"]
seasons_occasions = ["Summer", "Winter", "Christmas", "Thanksgiving", "Easter", "New Year's Eve", "Fall", "Spring"]

# Equipment list with Amazon href links (same as before)
equipment_list = {
    "Mixer": "https://www.amazon.com/s?k=mixer",
    "Baking Tray": "https://www.amazon.com/s?k=baking+tray",
    "Oven": "https://www.amazon.com/s?k=oven",
    "Whisk": "https://www.amazon.com/s?k=whisk",
    "Measuring Cups": "https://www.amazon.com/s?k=measuring+cups",
    "Spatula": "https://www.amazon.com/s?k=spatula",
    "Rolling Pin": "https://www.amazon.com/s?k=rolling+pin"
}

# Ingredients list with quantities (same as before)
ingredients_list = {
    "Flour": "200g",
    "Sugar": "100g",
    "Butter": "50g",
    "Eggs": "2",
    "Milk": "250ml",
    "Salt": "1tsp",
    "Baking Powder": "2tsp",
    "Vanilla Extract": "1tsp",
    "Chocolate Chips": "100g",
    "Olive Oil": "2tbsp"
}

# Generate SEO-optimized recipe titles
def generate_title():
    return f"{random.choice(['Delicious', 'Tasty', 'Mouthwatering', 'Irresistible', 'Healthy'])} {random.choice(['Chocolate', 'Vanilla', 'Strawberry', 'Lemon', 'Citrus'])} {random.choice(['Cake', 'Salad', 'Burger', 'Soup', 'Casserole'])}"

# Generate detailed instructions
def generate_instructions():
    steps = [
        "1. Preheat the oven to 180°C (350°F). This ensures that the oven is hot enough to bake your dish evenly and thoroughly.",
        "2. In a large bowl, combine flour, sugar, and salt. Mix them together until well blended. This will be the base of your dish.",
        "3. Add eggs and milk to the dry ingredients. Stir the mixture until smooth and free of lumps. This will help in achieving a consistent texture.",
        "4. Pour the mixture into a greased baking tray. Make sure to spread it evenly to ensure uniform cooking.",
        "5. Bake in the preheated oven for 25-30 minutes or until a toothpick inserted in the center comes out clean. This step is crucial for perfect baking."
    ]
    return "\n".join(steps)

# Generate nutritional facts in HTML table format, including ingredients
def generate_nutrition_facts():
    vitamins = ["vitamin-a", "vitamin-c", "calcium", "iron", "potassium", "vitamin-d", "vitamin-e", "vitamin-k", 
                "thiamin", "riboflavin", "niacin", "vitamin-b6", "folate", "vitamin-b12", "biotin", 
                "pantothenic-acid", "phosphorus", "iodine", "magnesium", "zinc", "selenium", "copper", 
                "manganese", "chromium", "molybdenum", "chloride"]
    
    # Nutrition facts per serving
    nutrition_html_single_serving = """
    <table class="table table-striped">
        <tr><th>Nutrient</th><th>Amount</th></tr>
    """
    for vitamin in vitamins:
        nutrition_html_single_serving += f"<tr><td><a href='https://www.betterhealth.vic.gov.au/health/healthyliving/Vitamins-and-minerals#{vitamin}'>{vitamin.replace('-', ' ').title()}</a></td><td>{random.randint(10, 100)}mg</td></tr>"
    nutrition_html_single_serving += "</table>"
    
    # Nutrition facts for the entire serving
    nutrition_html_total_serving = """
    <table class="table table-striped">
        <tr><th>Nutrient</th><th>Amount</th></tr>
    """
    for vitamin in vitamins:
        nutrition_html_total_serving += f"<tr><td><a href='https://www.betterhealth.vic.gov.au/health/healthyliving/Vitamins-and-minerals#{vitamin}'>{vitamin.replace('-', ' ').title()}</a></td><td>{random.randint(100, 500)}mg</td></tr>"
    nutrition_html_total_serving += "</table>"
    
    # Add ingredient list in the nutrition facts
    ingredient_nutrition_html = """
    <h3>Ingredients and Amounts</h3>
    <table class="table table-striped">
        <tr><th>Ingredient</th><th>Amount</th></tr>
    """
    for ingredient, amount in ingredients_list.items():
        ingredient_nutrition_html += f"<tr><td>{ingredient}</td><td>{amount}</td></tr>"
    ingredient_nutrition_html += "</table>"
    
    return ingredient_nutrition_html + nutrition_html_single_serving + nutrition_html_total_serving

# Generate a recipe
def generate_recipe(index):
    title = generate_title()
    subtitle = f"A wonderful recipe for {title.lower()} lovers."
    difficulty_level = random.choice(["Easy", "Medium", "Hard"])
    keywords = f"{title.lower()}, {random.choice(categories).lower()}, {random.choice(cuisines).lower()}"
    prep_time = f"{random.randint(10, 30)} min"
    cook_time = f"{random.randint(15, 45)} min"
    perform_time = f"{random.randint(20, 60)} min"
    total_time = f"{random.randint(60, 120)} min"
    ready_in = f"{random.randint(90, 150)} min"
    recipe_yield = f"{random.randint(2, 6)} servings"
    serving_size = f"{random.randint(150, 250)}g"
    energy = f"{random.randint(200, 500)} kcal"
    total_cost = f"${random.uniform(5, 20):.2f}"
    cost_per_serving = f"${random.uniform(2, 5):.2f}"
    cuisine = random.choice(cuisines)
    course = random.choice(dish_types)
    diet = random.choice(diets)
    
    ingredients = "\n".join([f'<i class="trg-icon eicon-check" aria-hidden="true"></i> {qty} {ingredient}' for ingredient, qty in ingredients_list.items()])
    
    equipment = "\n".join([f'<a href="{link}">{item}</a>' for item, link in random.sample(list(equipment_list.items()), random.randint(3, len(equipment_list)))])
    
    instructions = generate_instructions()
    nutrition_facts = generate_nutrition_facts()
    
    image_featured = f"https://www.pontalo.net/wp-content/uploads/2024/07/{title.replace(' ', '-').lower()}{index:02}.webp"
    image_path = f"/home/pontalo/htdocs/www.pontalo.net/wp-content/uploads/2024/07/{title.replace(' ', '-').lower()}{index:02}.webp"
    
    tags = f"{random.choice(diets).lower()}, {random.choice(dish_types).lower()}, {random.choice(cuisines).lower()}, {random.choice(seasons_occasions).lower()}"
    
    return {
        "Recipe Title": title,
        "Recipe Subtitle": subtitle,
        "Difficulty Level": difficulty_level,
        "Recipe Keywords": keywords,
        "Prep Time": prep_time,
        "Cook Time": cook_time,
        "Perform Time": perform_time,
        "Total Time": total_time,
        "Ready In": ready_in,
        "Recipe Yield": recipe_yield,
        "Serving Size": serving_size,
        "Energy": energy,
        "Total Cost": total_cost,
        "Cost per Serving": cost_per_serving,
        "Cuisine": cuisine,
        "Course": course,
        "Suitable for Diet": diet,
        "Ingredients List": ingredients,
        "Equipment Needed": equipment,
        "Instructions": instructions,
        "Nutrition Facts (Single Serving and Total Serving)": nutrition_facts,
        "Image Featured": image_featured,
        "Image Path": image_path,
        "Tags": tags
    }

# Generate and export 5000 recipes to a CSV file with progress bar
def export_recipes_to_csv(filename="recipes_for_wordpress.csv"):
    fieldnames = ["Recipe Title", "Recipe Subtitle", "Difficulty Level", "Recipe Keywords", "Prep Time", "Cook Time", "Perform Time", "Total Time", "Ready In", "Recipe Yield", "Serving Size", "Energy", "Total Cost", "Cost per Serving", "Cuisine", "Course", "Suitable for Diet", "Ingredients List", "Equipment Needed", "Instructions", "Nutrition Facts (Single Serving and Total Serving)", "Image Featured", "Image Path", "Tags"]
    
    # Create the window layout
    layout = [
        [sg.Text('Generating Recipes...')],
        [sg.ProgressBar(5000, orientation='h', size=(50, 20), key='progress')],
        [sg.Cancel()]
    ]

    # Create the window
    window = sg.Window('Recipe Generator', layout)
    
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Generate recipes and update progress bar
        for i in range(5000):
            event, values = window.read(timeout=10)
            if event == 'Cancel' or event is None:
                break
            recipe = generate_recipe(i + 1)
            writer.writerow(recipe)
            window['progress'].update(i + 1)

    window.close()
    sg.popup('Recipes Generated!', f'Successfully generated 5000 recipes and saved to {filename}')

# Run the script
if __name__ == "__main__":
    export_recipes_to_csv()
