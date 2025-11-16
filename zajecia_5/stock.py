# Create a program, which will store operations related to the bank account & stock status
#
# After the program is launched the user can see the following available commands:
#
# balance
# sale
# buy
# account
# list
# stock
# history
# end
#
# After user enters the respective command, the program is behaving accordingly:
#
# balance - Program fetches the amount, which should be added or substracted from the bank account
# sale - Program fetches the product name, price and number of pcs. Produkt needs to be presesnt in the stock. Required calculations related to bank account and stock (i.e. product "bicycle" that cost 100 and 1 pcs sold results in substraction 1 pcs of "bicycle" from the stock and addition of 100 PLN to bank account).
# buy - Program fetches the product name, price and number of pcs. Produkt is being added to the stock, if it wasn't there. Calculations made in opposite way that for "sale" operation. Account balance after "buy" operation cannot be negative.
# account - Program displays the account balance.
# list - Program displays current state of stock including prices and quantities od products.
# stock - Program displays current state of given product.
# history - Program fetches two variables "from" and "to", based on them is displays the history of transactions. If user gives empty value of "from" or "to" , program should print history from the beginning or/and end. If user gave variable which is out of range, program should inform the user and print the no of saved comments (to let the user pick the correct range).
# end - Program finish.
#
# Additional requirements:
#
# Program works till user gives "end" command
# Commends: balance, sale, amd buy are saved so user can use "history" command.
# After performing one of the commands (i.e. "balance") program again displays the information about other available commands, and also asks for entering one of the available commands.
# Take care of errors that may occur during perfoming of an operation (i.e. while executing the "buy" command if the cost is negative, program should give a message that operation is not possible due to peform). Data types should be also appropriate.

stock_account_balance = 20000.0
history = ["account_balance_displayed", "end"]
stock = [
    {
        "product": "chocolate",
        "price": 15.0,
        "quantity_in_stock": 10,
        "product_code": "112233"
    },
    {
        "product": "halvah",
        "price": 8.0,
        "quantity_in_stock": 5,
        "product_code": "223344"
    },
    {
        "product": "lollypop",
        "price": 2.0,
        "quantity_in_stock": 100,
        "product_code": "334455"
    },
    {
        "product": "donut",
        "price": 40.0,
        "quantity_in_stock": 8,
        "product_code": "556677"
    },
    {
        "product": "waffle",
        "price": 6.0,
        "quantity_in_stock": 50,
        "product_code": "667788"
    }
]

while True:
    command = input("""
        available commands:
        1. balance
        2. sale
        3. buy
        4. account
        5. list
        6. stock
        7. history
        8. end
        Give the command's no: """)

    match command:
        case "1":
            balance = float(input("Provide the amount to be added or substracted from the account balance: "))
            if stock_account_balance + balance < 0:
                print("It is not allowed to have a negative balance")
            else:
                stock_account_balance += balance
                print(f"Current balance is: {stock_account_balance} PLN")
                history.append("Balance change")
        case "2":
            product_code = input("Please give the product number: ")
            product_found = False
            for p in stock:
                if p.get("product_code") == product_code:
                    product_found = True
                    quantity_for_sale = int(input("Provide the quantity for sale: "))
                    if quantity_for_sale < p.get("quantity_in_stock"):
                        p["quantity_in_stock"] -= quantity_for_sale
                        product_price = p.get("cena")
                        print(f"The price is: {product_price} PLN")
                        stock_account_balance = stock_account_balance + (product_price * quantity_for_sale)
                        print(f"Stock account balance is now: {stock_account_balance} PLN")
                        history.append(f"Sold poduct {product_code}")
                    else:
                        print("No such product in stock")
                        break
            if not product_found:
                    print("Product not found")
        case "3":
            product = input("Provide the product name: ")
            price = float(input("Provide the price: "))
            quantity_in_stock = int(input("Provide the quantity: "))
            product_code = input("Provide product code: ")
            if stock_account_balance - (price * quantity_in_stock) < 0:
                print("Product is too expensive, you cannot buy it")
                continue
            else:
                stock_account_balance -= price * quantity_in_stock
            stock.append({
                "product": product,
                "price": price,
                "quantity_in_stock": quantity_in_stock,
                "product_code": product_code,
            })
            print(stock)
            history.append(f"Purchased product {product_code}")
        case "4":
            print(f"Current stock account balance: {stock_account_balance} PLN")
        case "5":
            print("Entire stock")
            print(stock)
        case "6":
            product_code = input("Podaj nr produktu: ")
            product_found = False
            for p in stock:
                if p.get("kod_produktu") == product_code:
                    product_found = True
                    print(f"Found product: {p}")
                    break
            if not product_found:
                print("No such product available")
        case "7":
            od = input("Provide value from (transaction no), if you don't want, don't provide: ")
            do = input("Provide value to (transaction no), if you don't want, don't provide: ")
            if od:
                od = int(od)
            else:
                od =0
            if do:
                do = int(do)
            else:
                do = len(history)
            print(f"Transaction history: {history[od:do]}")
        case "8":
            print("Program end")
            break
