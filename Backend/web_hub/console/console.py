#!/usr/bin/python3
import cmd


class WebHub(cmd.Cmd):
    """ The command line tool for the jak_tech hub """
    __classes = []
    prompt = '$ >>> '

    def preloop(self):
        intro = "Welcome to Jak_Tech WebHub Command-Line Tool.\n Type 'help' for a list of available commands."
        print(intro)

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