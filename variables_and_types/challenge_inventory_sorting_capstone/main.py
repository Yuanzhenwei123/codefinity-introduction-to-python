# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# items_word = items.split(", ")
# candy1 = items_word[0]
# candy2 = items_word[1]
# dry_goods = items_word[2]
candy1 = items[:9]
candy2 = items[11:20]
dry_goods = items[22:]

# categories_word = categories.split(", ")
# category1 = categories_word[0]
# category2 = categories_word[1]
category1 = categories[:11]
category2 = categories[13:]

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# print("we have " + candy1 + "for " + bubblegum_price + "in the " + category1)
print(f"we have {candy1} for {bubblegum_price} in the {category1}")
print(f"we have {candy2} for {chocolate_price} in the {category1}")
print(f"we have {dry_goods} for {pasta_price} in the {category2}")