def roll_call_dwarves(list):
    for index, name in enumerate(list):
        print(f"{index + 1}. {name}")
    pass


def summon_captain_planet(calls):
    list = []
    for call in calls:
        list.append(call.capitalize() + "!")
    return list
    pass


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
    pass


def find_the_cheese(list):
    cheeses = ("cheddar", "gouda", "camembert")
    for item in list:
        if item in cheeses:
            return item
    else:
        return None
    pass
