import argparse, sys

# parameter:
# size    |   weight  |   age |   times of sports per week  | sexe
# return:
# calories/day    
def calculator(size: float, weight: float, age: int, activity: int, s: str):
    # 0-1                         = 1.2
    # 2-3                         = 1.375
    # 4-5 times of sport per week = 1.55
    # 6-7                         = 1.7
    calories = 0

    if s == 'male':
        calories = 13.707*weight + 492.3*size - 6.673*age + 77.607
    elif s == 'female':
        calories = 9.74*weight + 172.9*size - 4.737*age + 667.051
    
    match activity:
        case 0:
            calories *= 1.2
        case 1:
            calories *=  1.2
        case 2:
            calories *=  1.375
        case 3:
            calories *=  1.375
        case 4:
            calories *=  1.55
        case 5:
            calories *=  1.55
        case 6:
            calories *=  1.725
        case 7:
            calories *=  1.725
        case _:
            calories *=  1.375

    return calories

# parameter:
# calories/day : float
# return:
# prot    |   carbs   |   lipids
def macros(calories: float, weight: float):
    # equivalence
    # 1g carb = 9 cal
    # 1g prot = 4 cal
    # 1g lipid = 4 cal

    # needs
    # 1.6 - 2.2g of proteins per kg of bodyweight
    # 0.7 - 1g of lipids per kg of bodyweight
    # rest as carbs

    g_prots = 1.8 * weight
    g_lipids = 0.85 * weight
    c_prots = g_prots * 4
    c_lipids = g_lipids * 4

    c_carbs = calories - c_prots - c_lipids
    g_carbs = c_carbs / 9
    return g_prots, g_carbs, g_lipids


# type:   cut     |   bulk
# degree: slow    |   medium  |   aggressive
#         10%     |   15%     |   25%
def cut_or_bulk(type: str, degree: str, prots: int, carbs: int, lipids: int):
    match degree:
        case 'slow':
            deficit = 0.10
        case 'medium':
            deficit = 0.15
        case 'aggressive':
            deficit = 0.25
        case _:
            deficit = 0

    if type == 'cut':
        carbs -= carbs * deficit
    elif type == 'bulk':
        carbs += carbs * deficit

    return prots, carbs, lipids


def main(size, weight, age, activity, s, type_of_diet, degree):
    calories = calculator(size, weight, age, activity, s)
    prots, carbs, lipids = macros(calories, weight)
    prots, carbs, lipids = cut_or_bulk(type_of_diet, degree, prots, carbs, lipids)
    print("Prots:", prots)
    print("Carbs:", carbs)
    print("Lipids:", lipids)
    return 0

parser = argparse.ArgumentParser()
parser.add_argument('-s', type=float, dest='size', help='Size of the person.')
parser.add_argument('-w', type=float, dest='weight', help="Weight of the person.")
parser.add_argument('-a', type=int, dest='age', help="Age of the person.")
parser.add_argument('-A', type=int, dest='activity', help="Times per week the person does sport.")
parser.add_argument('-S', type=str, dest='S', help="Male or Female.")
parser.add_argument('-t', type=str, dest='typeofdiet', help="Choose the type of diet: cut or bulk.")
parser.add_argument('-d', type=str, dest='degree', help="Choose the degree of agressivity in the diet.")

if len(sys.argv) == 1:
    print(parser.print_help(), "\n")

args = parser.parse_args()

main(args.size, args.weight, args.age, args.activity, args.S, args.typeofdiet, args.degree)