#How to use "continue"
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        print("I'm ignoring "+ item)
        continue
    print("Buy " + item)

#another scenario dude...
meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        #i hate spam
        nasty_food_item = item
        break
    else:
        print("I'll have a plate of that, then, please")
