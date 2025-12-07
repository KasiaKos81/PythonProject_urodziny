import csv

class FileHandler:
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.transformations = transformations
        print(self.transformations)
        self.data = self.load_data()

    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file, delimiter=",")
            temporary_matrix = []
            for row in reader:
                temporary_row =[]
                for item in row:
                    temporary_row.append(int(item))
                temporary_matrix.append(temporary_row)
        return temporary_matrix

    def save_data(self):
        with open(self.output_file, 'w+') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

    def do_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            print(transformation_list)
            operation = transformation_list[0]
            direction = transformation_list[1]
            index = int(transformation_list[2])
            value = int(transformation_list[3])
            if operation == "substract":
                if direction == "row":
                    self.substract_row(index, value)
                else:
                    print("No such change available")

    def substract_row(self, index, value):
        for position, item in enumerate(self.data):
            self.data[position][index] += value




