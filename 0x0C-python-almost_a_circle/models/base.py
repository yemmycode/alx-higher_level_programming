#!/usr/bin/python3
"""
A base model class.
"""
import json
import csv
import turtle

class Base:
    """
    Represents the base model
    """
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id if id is not None else (Base.__nb_objects := Base.__nb_objects + 1)


    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): List of instances who inherits of Base
        """
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            jsonfile.write(Base.to_json_string([obj.to_dictionary() for obj in list_objs]) if list_objs else "[]")

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to list of dictionaries."""
        return json.loads(json_string) if json_string and json_string != "[]" else []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads objects from a JSON file."""
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file."""
        file_name = "{}.csv".format(cls.__name__)

        with open(file_name, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"])
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads objects from a CSV file."""
        file_name = "{}.csv".format(cls.__name__)

        try:
            with open(file_name, "r") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"])
                list_dicts = [{key: int(value) for key, value in d.items()} for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws shapes using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#3399FF")
        turt.pensize(4)
        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#FFFF00")

        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

if __name__ == "__main__":
    pass

