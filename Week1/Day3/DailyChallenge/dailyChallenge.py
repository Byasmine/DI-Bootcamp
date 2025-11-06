#Challenge 1: Letter Index Dictionary
print("Challenge 1 : ")
user_input = str(input("Enter a word : "))
user_input = user_input.lower().strip() #String manipulation

word_dict = {} #empty dictionary
for index,letter in enumerate(user_input): #key:postion value:letter of each character in the word
    if letter in word_dict: #check if the character is already a key and they are strings
        word_dict[letter].append(index) #append the current 
    else :
        word_dict[letter] = [index]
print("Challenge 1 : ", word_dict)

#Challenge 2: Affordable Items
print("Challege 2 : ")
#store data : 

items_purchase = {
    "Apple": "$4", 
    "Honey": "$3",
    "Fan": "$14", 
    "Bananas": "$4", 
    "Pan": "$100", 
    "Spoon": "$2"
}

#In Python (version 3.7 or newer), dictionaries keep the order of items

wallet = input("Enter your amount of money : ")
clean_wallet = float(wallet.replace("$","").replace(",",".").strip())

# clean price items
for item, price in items_purchase.items():
    clean_price = float(price.replace('$', '').replace(',', '').strip())
    items_purchase[item] = clean_price

#creating a list basket
basket = []

for item,price in items_purchase.items():
    if clean_wallet >= price:
        basket.append(item)
        clean_wallet-=price


# show results
if not basket:
    print("Nothing")
else:
    print(sorted(basket)) #alphabetical order



