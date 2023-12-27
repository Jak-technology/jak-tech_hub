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


import cmd
from django.core.exceptions import ObjectDoesNotExist
from blog.models import BlogPost, BlogPostComment
from project_creation.models import Project, ProjectComment
from users.models import UserProfile, Skills, Specialization, JobTitle



class WebHub(cmd.Cmd):
    """ The command line tool for the jak_tech hub """

    __apps = ["blog", "dashboard", "project_creation", "users"]

    __classes = ["BlogPost",
                 "BlogPostComment",
                 "Project",
                 "ProjectComment",
                 "UserProfile",
                 "Skills",
                 "Specialization",
                 "JobTitle",
                 
                ]

    prompt = '$ >>> '


    def get_model_class(self, app_name, class_name):
        try:
            # Use the apps module to dynamically get the model class
            return apps.get_model(app_name, class_name)
        except LookupError:
            return None


    def preloop(self):
        intro = "Welcome to Jak_Tech WebHub Command-Line Tool.\n Type 'help' for a list of available commands.\n Type '<help> <command>' to see specific command help"
        print(intro)


    def do_create(self, arg):
        # Work well only for classes with single fields for now
        """
            Creates a new instance of a class and saves it in the database
            Usage: create <app_name> <class_name> <field_value_1> <field_value_2> ...
        """
        args = arg.split()

        if len(args) < 3:
            print("** invalid number of arguments **")
            return

        app_name = args[0]
        class_name = args[1]
        field_values = args[2:]

        model_class = self.get_model_class(app_name, class_name)

        if model_class is None:
            print(f"** invalid class name: ({class_name}) **")
        else:
            try:
                # Check if an instance with the specified ID already exists
                existing_instance = model_class.objects.filter(pk=field_values[0]).exists()

                if existing_instance:
                    print(f"Instance with ID {field_values[0]} already exists. Choose a different ID.")
                else:
                    instance = model_class(pk=field_values[0])

                    for i, value in enumerate(field_values):
                        field_name = model_class._meta.fields[i].name
                        setattr(instance, field_name, value)

                    instance.save()
                    print(f"Instance created successfully with values: {field_values}")
            except Exception as e:
                print(f"Error creating instance: {str(e)}")



    def do_show(self, arg):
        """
            Prints the string representation of an instance based on the app name, class name and id
            Usage: show <app_name> <class_name> <object_id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** app name missing **")
        elif args[0] not in self.__apps:
            print("** app doesn't exist **")
        elif len(args) == 1:
            print("** class name missing **")
        elif args[1] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) != 3:
            print("** instance id missing **")
        else:
            app_name = args[0]
            class_name = args[1]
            object_id = args[2]

            model_class = self.get_model_class(app_name, class_name)

            if model_class is None:
                print(f"** invalid class name: ({class_name}) **")
            else:
                try:
                    instance = model_class.objects.get(pk=object_id)
                    print(instance)
                except ObjectDoesNotExist:
                    print("** no instance found **")

        
    def do_destroy(self, arg):
        """
            Deletes an instance based on the app name, class name and id
            Usage: destroy <app_name> <class_name> <object_id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** app name missing **")
        elif args[0] not in self.__apps:
            print("** app doesn't exist **")
        elif len(args) == 1:
            print("** class name missing **")
        elif args[1] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) != 3:
            print("** instance id missing **")
        else:
            app_name = args[0]
            class_name = args[1]
            object_id = args[2]

            model_class = self.get_model_class(app_name, class_name)

            if model_class is None:
                print(f"** invalid class name: ({class_name}) **")
            else:
                try:
                    instance = model_class.objects.get(pk=object_id)
                    instance.delete()
                    print(f"Instance {object_id} deleted successfully.")
                except ObjectDoesNotExist:
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