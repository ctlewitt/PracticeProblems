# given a bill and a list of suggested tip percents from the eaters, calculate average of suggested tips and final tip amount

def tip(bill, suggested_tips):
    if len(suggested_tips) == 0:
        raise Exception("need suggested tips")
    avg_tip = sum(suggested_tips)/len(suggested_tips)
    return bill * avg_tip / 100


print(tip(100, [15, 20, 10, 10, 10, 25]))
print(tip(100, [20]))
print(tip(15, [15, 20, 10, 10, 10, 25]))
print(tip(0, [15, 20, 10, 10, 10, 25]))
try:
    tip(100, [])
except Exception as e:
    print(e)