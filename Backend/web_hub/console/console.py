#!/usr/bin/python3
import os
import sys
import django
from django.conf import settings
from django.apps import apps

sys.path.append(os.getcwd())

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_hub.settings")

# Ensure the app registry is populated only once
if not apps.ready:
    django.setup()

# Move import after setup
import cmd
from users.models import UserProfile

class WebHub(cmd.Cmd):
    """ The command line tool for the jak_tech hub """

    __classes = ["UserProfile"]

    prompt = '$ >>> '

    def preloop(self):
        intro = "Welcome to Jak_Tech WebHub Command-Line Tool.\n Type 'help' for a list of available commands."
        print(intro)


    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        Usage: show <class_name> <object_id>
        """
        args = arg.split()
        
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            object_id = args[1]

            try:
                instance = UserProfile.objects.get(pk=object_id)
                print(instance)
            except UserProfile.DoesNotExist:
                print("** no instance found **")

        

    def do_quit(self, arg):
        """ Quits the command interpreter """
        return True

    def emptyline(self):
        """ Method called with empty line is entered """
        return
    
    def do_EOF(self, arg):
        """ Exits command interpreter when it receives (Ctrl + D or Command + D) """
        print()
        return True

    def postloop(self):
        print('Exiting... Goodbye!')

if __name__ == "__main__":
    WebHub().cmdloop()