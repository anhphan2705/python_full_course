# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run

# Module that has if __name__ == '__main__' can be 
# 1. run as a standalone program
# 2. imported and used by other modules

# when you import __name__ from another module, the __name__ will be assign as the name of the module
# The main purppose of if __name__ == '__main__' is to check if the module is being run directly or indirectly

def main():
    print("Hello!")
    
if __name__ == '__main__':
    main() 