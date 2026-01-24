import json

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()

    def read_file(self):
        with open(self.filename, 'r', encoding="utf-8") as file:
            return json.loads(file.read())

    def write_file(self, city, date, new_entry):
        if not self.data.get(city):
            self.data[city] = {}
        self.data[city][date] = new_entry
        with open(self.filename, 'w', encoding="utf-8") as file:
            file.write(json.dumps(self.data, indent=4))

    def read_weather_file(self):
        with open("data.json", "r", encoding="utf-8") as file:
            weather_data = json.loads(file.read())
        print(weather_data)
        return weather_data

    def check_if_date_exists(self, city, searched_date):
        for searched_city in self.data:
            if searched_city == city:
                for date, info in self.data[searched_city].items():
                    if date == searched_date:
                        return info
