#initialise snack lists

name = ['a','b','c','d','e']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water，
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice':orange_juice
    }

test_data = [
    [[1,'Water'], [1,'Pita Chips'],[1, 'M&Ms']],
    [[1,'Pita Chips'],[1, 'Orange Juice'], [2, 'M&Ms']],
    [[1,'Water']]
]

count = 0
for client_order in test_data:

    #assume no snacks have been bought..
    for item in snack_lists:
        item.append(0)


