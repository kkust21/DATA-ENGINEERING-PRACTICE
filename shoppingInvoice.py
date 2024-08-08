store_items = [
    {"itemid": 1, "itemname": "Apple", "itemprice": 200},
    {"itemid": 2, "itemname": "Mango", "itemprice": 20},
    {"itemid": 3, "itemname": "Biscuits", "itemprice": 40},
    {"itemid": 4, "itemname": "pineapple", "itemprice": 0.4},
    {"itemid": 5, "itemname": "orange", "itemprice": 0.6},
    {"itemid": 6, "itemname": "Milk", "itemprice": 60}
]

shopping_cart = []


def view_store():
    print("store item:")
    for item in store_items:
        print("itemid:", item["itemid"], "itemname:", item["itemname"], "itemprice:", item["itemprice"])


def purchase_item():
    while True:
        item_id = input("enter itemid  to purchase")
        quantity = int(input("enter the quantity to purchase"))
        item = None
        #if item_input.isdigit():
        #item_id = int(item_input)
        for i in store_items:
            if i["itemid"] == item_id:
                shopping_cart.append(
                    {"itemid": item['itemid'], "itemname": item["itemname"], "itemprice": item['itemprice'],
                     "quantity": quantity})
            break
        cont = input("Do you want to continue adding item? (yes/no)")
        if cont == "no":
            break


def update_purchase_item():
    item_id = input("enter itemid")
    for item in shopping_cart:
        if item["itemid"] == item_id:
            quantity = int(input("enter the quantity to purchase"))
            item["quantity"] = quantity
        break


def remove_item():
    item_id = input("enter itemid")
    for item in shopping_cart:
        if item["itemid"] == item_id:
            del item["itemid"]
        break


def view_purchased_item():
    if not shopping_cart:
        print("\n nothing in shopping cart")
        return
    print("\nPurchased Item:")

    idx = 1
    for i in range(len(shopping_cart)):
        item =shopping_cart[i]
        total_price = item["quantity"] * item["itemprice"]
        print(item["itemname"], item["quantity"], item["itemprice"])
        idx += 1


def generate_invoice():
    if not shopping_cart:
        print("\n No item in cart")
        return
    total_amount = 0
    print("\nInvoice:")
    for item in shopping_cart:
        total_price = item["quantity"] * item["itemprice"]
        total_amount += total_price
        print(item["itemid"],item["itemname"], item["quantity"], item["itemprice"])
    print("\nTotal Amount:",total_amount)


def main():
    while True:
        print("1. view the store")
        print("2. Purchase an item")
        print("3. update the purchase item")
        print("4. remove an item")
        print("5. View the purchase item list")
        print("6. Exit and generate invoice")
        choice = input("Enter the choice")
        if choice == '1':
            view_store()
        elif choice == '2':
            purchase_item()
        elif choice == '3':
            update_purchase_item()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            view_purchased_item()
        elif choice == '6':
            generate_invoice()
            break
        else:
            print("invalid choice")

#if __name__ == "__main()__":
main()
