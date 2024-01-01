#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    """def all(self):
        Returns a dictionary of models currently in storage
        return FileStorage.__objects
    """

    def all(self, cls=None):
        """
        Return a dictionary of instantiated objects in __objects.
        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary
        """
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    cls_dict[key] = value
            return cls_dict
        return self.__objects

        # if cls is None:
        #     return FileStorage.__objects
        # else:
        # filtered_objects = {key: obj for key,
        # obj in FileStorage.__objects.items() if isinstance(obj, cls)}
        #     return filtered_objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

        # """Adds new object to storage dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {
            obj_key: self.__objects[obj_key].to_dict()
            for obj_key in self.__objects.keys()
            }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

        # """Saves storage dictionary to file"""
        # with open(FileStorage.__file_path, 'w') as f:
        #     temp = {}
        #     temp.update(FileStorage.__objects)
        #     for key, val in temp.items():
        #         temp[key] = val.to_dict()
        #     json.dump(temp, f)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects, if it exists.
        """
        # from models.base_model import BaseModel
        # from models.user import User
        # from models.place import Place
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.review import Review

        # classes = {
        #             'BaseModel': BaseModel, 'User': User, 'Place': Place,
        #             'State': State, 'City': City, 'Amenity': Amenity,
        #             'Review': Review
        #           }
        # try:
        #     temp = {}
        #     with open(FileStorage.__file_path, 'r') as f:
        #         temp = json.load(f)
        #         for key, val in temp.items():
        #                 self.all()[key] = classes[val['__class__']](**val)
        # except FileNotFoundError:
        #     pass

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for obj_dict in json.load(file).values():
                    name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(name)(**obj_dict))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        # if obj is not None:
        #     key = obj.to_dict()['__class__'] + '.' + obj.id
        #     if key in FileStorage.__objects:
        #         del FileStorage.__objects[key]
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
