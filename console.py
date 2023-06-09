#!/usr/bin/python3
"""AirBnB console for command interpreter"""
import cmd
import re
import ast
from models import storage


class HBNBCommand(cmd.Cmd):

    """HBNBC command interpreter"""

    prompt = '(hbnb) '

    def precmd(self, line):
        if line.endswith("all()"):
            line = "all " + line.split(".")[0]
        elif line.endswith("count()"):
            line = "count " + line.split(".")[0]
        elif re.search(r"\.show\(.+\)$", line):
            start_index = line.find("(")
            end_index = line.find(")")
            substring = line[start_index + 1:end_index]
            line = f"show {line.split('.')[0]} {substring}"
        elif re.search(r"\.destroy\(.+\)$", line):
            start_index = line.find("(")
            end_index = line.find(")")
            substring = line[start_index + 1:end_index]
            line = f"destroy {line.split('.')[0]} {substring}"
        elif re.search(r"\.update\(.+\)$", line):
            if "{" in line:
                uuid_pattern = r'User.update\("([^"]+)",'
                uuid_match = re.search(uuid_pattern, line)
                uuid_value = uuid_match.group(1)

                # Extracting the attribute dictionary
                dict_pattern = r'{(.+)}'
                dict_match = re.search(dict_pattern, line)
                dict_str = dict_match.group(0)

                # Converting the attribute dictionary string to a dictionary
                attr_dict = ast.literal_eval(dict_str)

                print(uuid_value)
                print(attr_dict)
                for k, v in attr_dict.items():
                    line = f"update {line.split('.')[0]} {uuid_value} {k} {v}"
                    return line
            else:
                pattern = r'User.update\("([^"]+)", "([^"]+)", "([^"]+)"\)'
                matches = re.match(pattern, line)

                if matches:
                    uuid_value = matches.group(1)
                    attr_name = matches.group(2)
                    attr_value = matches.group(3)
                    line = f"update {line.split('.')[0]} " \
                           f"{uuid_value} {attr_name} {attr_value}"
        return line

    def emptyline(self):
        """Should do nothing on Enter"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Handles end of file"""
        print()
        exit()

    def do_create(self, arg):
        """Creates new instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Print string representation of an instance
        based on class name and id"""
        arg_lists = arg.split()
        if len(arg_lists) == 0:
            print("** class name missing **")
        else:
            if arg_lists[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg_lists) < 2:
                print("** instance id missing **")
            else:
                key = arg_lists[0] + '.' + arg_lists[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_lists = arg.split()
        if len(arg_lists) == 0:
            print("** class name missing **")
        else:
            if arg_lists[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg_lists) < 2:
                print("** instance id missing **")
            else:
                key = arg_lists[0] + '.' + arg_lists[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        arg_lists = arg.split()
        if len(arg_lists) == 0:
            print("** class name missing **")
        else:
            if arg_lists[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg_lists) < 2:
                print("** instance id missing **")
            elif len(arg_lists) < 3:
                print("** attribute name missing **")
            elif len(arg_lists) < 4:
                print("** value missing **")
            else:
                key = arg_lists[0] + '.' + arg_lists[1]
                if key in storage.all().keys():
                    setattr(storage.all()[key], arg_lists[2], arg_lists[3])
                    storage.save()
                else:
                    print("** no instance found **")

    def do_count(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            print(len([n for n in storage.all() if arg in n.split(".")]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
