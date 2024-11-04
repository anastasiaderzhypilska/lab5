class Furniture:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
    
    def __del__(self):
        print(f"{self.name} has been removed.")
    
    def move(self, new_coordinates):
        print(f"Moving {self.name} from {self.coordinates} to {new_coordinates}.")
        self.coordinates = new_coordinates

    def display(self):
        print(f"{self.name} is located at {self.coordinates}")


class Bed(Furniture):
    def __init__(self, coordinates):
        super().__init__("Bed", coordinates)


class Sofa(Furniture):
    def __init__(self, coordinates):
        super().__init__("Sofa", coordinates)


class Table(Furniture):
    def __init__(self, coordinates):
        super().__init__("Table", coordinates)


class Carpet(Furniture):
    def __init__(self, coordinates):
        super().__init__("Carpet", coordinates)


class Room:
    def __init__(self):
        self.furniture_items = []

    def add_furniture(self, furniture):
        self.furniture_items.append(furniture)
        print(f"Added {furniture.name} to the room.")

    def remove_furniture(self, furniture):
        if furniture in self.furniture_items:
            self.furniture_items.remove(furniture)
            del furniture
        else:
            print(f"{furniture.name} is not in the room.")

    def rearrange(self, furniture, new_coordinates):
        if furniture in self.furniture_items:
            furniture.move(new_coordinates)
        else:
            print(f"{furniture.name} is not in the room.")

    def display_furniture(self):
        print("Furniture in the room:")
        for item in self.furniture_items:
            item.display()


def main():
    my_room = Room()
    
    bed = Bed([0, 0])
    sofa = Sofa([1, 2])
    table = Table([3, 4])
    carpet = Carpet([2, 1])

    my_room.add_furniture(bed)
    my_room.add_furniture(sofa)
    my_room.add_furniture(table)
    my_room.add_furniture(carpet)

    my_room.display_furniture()

    my_room.rearrange(bed, [5, 5])
    my_room.rearrange(sofa, [0, 2])

    my_room.display_furniture()

    my_room.remove_furniture(table)

    my_room.display_furniture()


if __name__ == "__main__":
    main()
