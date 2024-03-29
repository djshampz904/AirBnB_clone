#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB project"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing on empty input line
        """
        pass

    def do_create(self, line):
        """Creates a new instance of the specified class"""
        if not line:
            print("** class name missing **")
        elif line not in models.CLASSES:
            print("** class doesn't exist **")
        else:
            new_model = models.CLASSES[line]()  # Create an instance of the specified class
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    class HBNBCommand(cmd.Cmd):
        """Command interpreter class for HBNB project"""
        prompt = '(hbnb) '

        # ... other methods ...

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        if line and line not in models.CLASSES:
            print("** class doesn't exist **")
        elif line in models.CLASSES:
            print([str(obj) for obj in models.storage.all().values() if obj.__class__.__name__ == line])
        else:
            print([str(obj) for obj in models.storage.all().values()])

    def do_update(self, line):
        """usage update <class name> <id> <attribute name>
        "<attribute value>"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                if args[2] not in ["id", "created_at", "updated_at"]:
                    setattr(models.storage.all()[key], args[2], args[3].strip('"'))
                    models.storage.all()[key].save()

    def do_count(self, line):
        """Retrieve the number of instances of a class
        """
        count = 0
        for obj in models.storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
