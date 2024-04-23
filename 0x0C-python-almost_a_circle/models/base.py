#!/usr/bin/python3
"""
Defines a fundamental model class.
"""
import json
import csv
import turtle

class Base:
    """
    Represents the primary model
    """
    __nb_objects = 0
    def __init__(self, identifier=None):
        if identifier is not None:
            self.identifier = identifier
        else:
            Base.__nb_objects += 1
            self.identifier = Base.__nb_objects


    @staticmethod
    def to_json_text(list_dicts):
        """Produces the JSON string representation of list_dicts.
        Args:
            list_dicts (list): A list of dictionaries.
        """
        if list_dicts is None or list_dicts == []:
            return "[]"
        to_json_text = json.dumps(list_dicts)

        return to_json_text

    @classmethod
    def save_to_file(cls, list_instances):
        """Records the JSON string representation of list_instances to a file.
        Args:
            list_instances (list): List of instances inheriting from Base
        """
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_instances is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for instance in list_instances:
                    list_dict.append(instance.to_dictionary())
                jsonfile.write(Base.to_json_text(list_dict))

    def from_json_text(json_text):
        """

        """
        if json_text is None or json_text == "[]":
            return []
        return json.loads(json_text)

    @classmethod
    def instantiate(cls, **data):
        """Generates an instance with all attributes pre-set.
        """
        if data and data != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**data)

            return dummy

    @classmethod
    def load_from_file(cls):
        """

        """
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_text(jsonfile.read())

                list_instances = []

                for dictionary in list_dicts:
                    list_instances.append(cls.instantiate(**dictionary))
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_instances):
        """
        Write the CSV serialization of a list of objects to a file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)

        with open(file_name, "w") as csvfile:
            if list_instances is None or list_instances == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["identifier", "width", "height", "x", "y"]
                else:
                    field_names = ["identifier", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for instance in list_instances:
                writer.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)
        
        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["identifier", "width", "height", "x", "y"]
                else:
                    field_names = ["identifier", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=field_names)

                new_list_dict = []

                converted_dict = {}

                for dictionary in list_dicts:
                    for key, value in dictionary.items():
                        converted_dict[key] = int(value)

                    new_list_dict.append(converted_dict)

                list_dicts = new_list_dict

                list_instances = []

                for dictionary in list_dicts:
                    list_instances.append(cls.instantiate(**dictionary))

                return list_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_instances_rectangles, list_instances_squares):
        """
        Opens a window and draws all the Rectangles,
        and Squares using the turtle module.
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#3399FF")

        turt.pensize(4)

        turt.shape("turtle")

        for rectangle_instance in list_instances_rectangles:
            turt.showturtle()

            turt.up()

            turt.goto(rectangle_instance.x, rectangle_instance.y)

            turt.down()

            for _ in range(2):
                turt.forward(rectangle_instance.width)

                turt.left(90)

                turt.forward(rectangle_instance.height)

                turt.left(90)

            turt.hideturtle()


        turt.color("#FFFF00")

        for square_instance in list_instances_squares:
            turt.showturtle()

            turt.up()

            turt.goto(square_instance.x, square_instance.y)

            turt.down()

            for _ in range(2):
                turt.forward(square_instance.width)
                turt.left(90)

                turt.forward(square_instance.height)

                turt.left(90)

            turt.hideturtle()

        turtle.exitonclick()



if __name__ == "__main__":

    pass

