import json

class FileHandler:
    def __init__(self, filepath):
        self.file = filepath
        # self.tuple = self.load_data_from_file()
        # self.stock_account_balance = self.tuple[0]
        # self.history = self.tuple[1]
        # self.stock = self.tuple[2]
        # you can write the above commented 4 lines as one:
        self.stock_account_balance, self.history, self.stock = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file, "r") as file:
            data = json.load(file)
            return data.get("stock_account_balance"), data.get("history"), data.get("stock")
#             that structure above is tuple (krotka)

    def save_data_to_file(self, new_stock_account_balance, new_history, new_stock):
        with open(self.file, "w", encoding="utf-8") as file:
            temporaray_data = {
                "stock_account_balance": new_stock_account_balance,
                "history": new_history,
                "stock": new_stock
            }
            file.write(json.dumps(temporaray_data, indent=4, ensure_ascii=False))

file_handler = FileHandler("stock.json")