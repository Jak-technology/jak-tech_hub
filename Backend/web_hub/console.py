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
                    print(f"{instance} deleted successfully.")
                except ObjectDoesNotExist:
                    print("** no instance found **")


    def do_all(self, arg):
        """ 
            Prints all string representation of all instances based on the class name
            Usage: all <app_name> <class_name>
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
        else:
            app_name = args[0]
            class_name = args[1]

            model_class = self.get_model_class(app_name, class_name)

            try:
                instance = model_class.objects.all()
                print()
                for lists in instance:
                    print(lists)
                    print()
                print(f"There are a total of ({model_class.objects.all().count()}) enteries")
                print()
            except ObjectDoesNotExist:
                print("** no instance found **")


    def default(self, arg):
        """ The command interpreter can retrieve all instances of a class
                Usage: <app name>.<class name>.all()
            It can retrieve the number of instances of a class
                Usage: <app name>.<class name>.count()
            It can retrieve an instance based on its ID
                Usage: <app name>.<class name>.show(<id>)
            It can create an instance 
                Usage: <app name>.<class name>.create()
            It can destroy an instance based on its ID
                Usage: <app name>.<class name>.destroy(<id>)
            It can update an instance based on its ID #Not implemented yet
                Usage: <app name>.<class name>.update(<id>, <attr name>, <attr value>)
            It can update an instance based on its ID with a dictionary #Not implemented yet
                Usage: <app name>.<class name>.update(<id>, <dictionary representation>)
        """
        args = arg.split('.')

        if len(args) >= 3 and args[-1] == 'all()':
            app_name = args[0]
            class_name = args[1]
            self.do_all(f"{app_name} {class_name}")
        
        elif len(args) >= 3 and args[-1] == 'count()':
            app_name = args[0]
            class_name = args[1]
            obj = self.get_model_class(app_name, class_name)
            print(obj.objects.all().count())

        elif len(args) >= 3 and args[-1].startswith('show'):
            app_name = args[0]
            class_name = args[1]
            obj_id_split = args[-1].split('(')[1]
            obj_id = obj_id_split.split(')')[0]
            self.do_show(f"{app_name} {class_name} {obj_id}")
        
        elif len(args) >= 3:
            app_name = args[0]
            class_name = args[1]
            if args[-1].startswith('create'):
                # Extract field name and value from the command
                create_args = args[-1].split('(')[1].split(')')[0].split()
                print(create_args)
                if len(create_args) == 2:
                    field_name = create_args[0]
                    field_value = create_args[1]
                    # Call do_create with the appropriate arguments
                    self.do_create(f"{app_name} {class_name} {field_name} {field_value}")

        elif len(args) >= 3 and args[-1].startswith('destroy'):
            app_name = args[0]
            class_name = args[1]
            obj_id_split = args[-1].split('(')[1]
            obj_id = obj_id_split.split(')')[0]
            self.do_destroy(f"{app_name} {class_name} {obj_id}")
        else:
            print("** Invalid command format **")
                

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