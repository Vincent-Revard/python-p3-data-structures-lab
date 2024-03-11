spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    max_heat = max(food["heat_level"] for food in spicy_foods)
    return [food for food in spicy_foods if food["heat_level"] == max_heat]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f"{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}"
        )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None


def print_spiciest_foods(spicy_foods):
    # spicy_foods = sorted(spicy_foods, key=lambda x: x["heat_level"], reverse=True)
    # print_spicy_foods(spicy_foods)
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(
                f"{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}"
        )

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods) if len(spicy_foods) > 0 else 0

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
