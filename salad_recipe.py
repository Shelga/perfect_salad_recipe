import random


base = [
    "Lettuce",
    "Spinach",
    "Kale",
    "Chard",
    "Collards",
    "Arugula",
    "Pea Shoots",
    "Cabbage",
]
unexpected = [
    "Watermelon",
    "Cottage Cheese",
    "Hummus",
    "Bacon",
    "Pickled Veggies",
    "Herbs",
    "Dried Fruit",
    "Peanuts",
]
crunch = [
    "Carrot",
    "Sprouts",
    "Cucumber",
    "Croutons",
    "Zucchini",
    "Bell Pepper",
    "Apple",
    "Seeds",
]
protein = ["Beans", "Eggs", "Tuna", "Chicken", "Steak", "Tofu", "Quinoa", "Peas"]
soft = ["Sweet Potatoes", "Cheese", "Avocado", "Tomatoes", "Rice", "Olive"]
dressing = [
    "Mustard-Based",
    "Tahini-Based",
    "Dairy-Based",
    "Vinaigrette",
    "Pesto-Based",
    "Fruity",
]


base_random = base[random.randint(0, len(base) - 1)]
unexpected_random = unexpected[random.randint(0, len(unexpected) - 1)]
crunch_random = crunch[random.randint(0, len(crunch) - 1)]
protein_random = protein[random.randint(0, len(protein) - 1)]
soft_random = soft[random.randint(0, len(soft) - 1)]
dressing_random = dressing[random.randint(0, len(dressing) - 1)]

print(
    "We could create a perfect recipe for you or you could create it for yourself. Print 'get' to get a recipe or print 'create' to create yourself recipe"
)
answer = input("Your answer is: ")

if answer.isdigit():
    print("Print correct request число")
else:
    if answer == "get":
        print(
            "Your perfect salad recipe for today is: ",
            base_random,
            " as base + ",
            unexpected_random,
            " as unexpected ingredient + ",
            crunch_random,
            " as crunchy + ",
            protein_random,
            " as protein + ",
            soft_random,
            " as soft and ",
            dressing_random,
            " for dressing",
        )
    elif answer == "create":
        print("Choose a number for each ingredient")
        base_random_c = base[int(input("Choose a number between  0 and 7 for base: "))]
        unexpected_random_c = unexpected[
            int(input("Choose a number between  0 and 7 for unexpected ingredient: "))
        ]
        crunch_random_c = crunch[
            int(input("Choose a number between  0 and 7 for crunchy: "))
        ]
        protein_random_c = protein[
            int(input("Choose a number between  0 and 7 for protein: "))
        ]
        soft_random_c = soft[int(input("Choose a number between  0 and 5 for soft: "))]
        dressing_random_c = dressing[
            int(input("Choose a number between  0 and 5 for dressing: "))
        ]
        print(
            "Your chosen  salad recipe for today is: ",
            base_random_c,
            " as base + ",
            unexpected_random_c,
            " as unexpected ingredient + ",
            crunch_random_c,
            " as crunchy + ",
            protein_random_c,
            " as protein + ",
            soft_random_c,
            " as soft and ",
            dressing_random_c,
            " for dressing",
        )
    else:
        print("Print correct request")
