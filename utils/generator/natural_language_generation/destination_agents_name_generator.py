from nltk import CFG as cfg
from nltk.parse.generate import generate


def generate_destination_agents_names():
    """
        Outputs a list of names usable for the narration system.
        Must be called just once to generate all names.
    """
    endings = [
        "Store",
        "Shop",
        "Market",
        "Garage",
        "Hut",
        "Discounts",
        "Buy"
    ]
    end = "End -> \""+'\" | \"'.join(endings)+"\"\n"
    names = [
        "AAA",
        "Aeron General",
        "Annie\'s Blue Ribbon",
        "Arbor General",
        "Brown Wave",
        "Brookshire",
        "Charlie\'s",
        "Daily Select",
        "Essential",
        "Fresh Hills",
        "Heritage",
        "Jackson Street",
        "Spruce City",
        "SpringMart",
        "North St.",
        "Woodstock",
        "Whole Mart",
        "Van\'s General",
        "Authentic",
        "Best Price",
        "BestMart",
        "Grapevines",
        "Harvest Moon",
        "The Mega",
        "Cornermall",
        "Liberty\'s",
        "One Stop",
        "Orion",
        "Upscale",
        "Delia\'s",
        "Top",
        "Yudivian\'s",
        "Suilan\'s",
        "Alejandro\'s",
    ]
    name = "Name -> \""+'\" | \"'.join(names)+"\"\n"
    grammar_string = "S -> Name | Name End\n"+name+end
    grammar = cfg.fromstring(grammar_string)
    destination_agents_name = []
    for sentence in generate(grammar):
        destination_agents_name.append(' '.join(sentence))
    return destination_agents_name