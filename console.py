#!/usr/bin/python3
"""AirBnB console for command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):

    """HBNBC command interpreter"""

    prompt = '(hbnb) '


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
