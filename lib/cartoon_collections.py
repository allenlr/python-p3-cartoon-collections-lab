def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves):
        print(f"{index + 1}. {dwarf}")
    pass

def summon_captain_planet(calls):
    return [f"{call.capitalize()}!" for call in calls]
    pass

def long_planeteer_calls(calls):
    ls = []
    for call in calls:
        if len(call) > 4:
            ls.append(True)
        else:
            ls.append(False)
    return True in ls
    pass

def find_the_cheese(ls):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in ls:
            return ls[ls.index(cheese)]
    return None
            
    pass
