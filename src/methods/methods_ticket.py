# -*- coding: utf-8 -*-

from clear_screen import clear_screen

# Menu and Auxilites

def show_menu():
    '''
        Function for show menu with options:
        1 - Emission Ticket
        2 - Call Ticket
        3-- Show Queue
        4 - Quit
        Parameter > None.
        Return > None.
    '''
    print('''
========== Menu ==========
| 1 - Emission Ticket    |
| 2 - Call Ticket        |
| 3 - Show Queue         | 
| 4 - Quit               |
==========================
    ''')


def check_choice_menu(choice):
    '''
        Check choice of menu.
        Parameter > choice: int.
        Return > boolean.
    '''
    if choice == 1:
        return True
    elif choice == 2:
        return True
    elif choice == 3:
        return True
    elif choice == 4:
        return True
    else:
        return False


def request_choice_menu():
    '''
        Request of choice for menu.
        Options:
        | 1 - Emission Ticket    |
        | 2 - Call Ticket        | 
        | 3 - Queue              |
        | 4 - Quit               |   
        Parameter > None
        Return >  choice: int. 
    '''
    while True:
        try:
            show_menu()
            choice = int(input('Type the option (Only numbers): '))
            if check_choice_menu(choice):
                return choice
            else:
                clear_screen()
                print("Option Incorret! Try again.")
                choice = request_choice_menu()
                return choice
        except ValueError:  # Case it isn't a number
            clear_screen()
            print("Option it isn't a number! Try again.\n")
            choice = request_choice_menu()
            return choice
        except KeyboardInterrupt:
            clear_screen()
            print('Quit application, trought of option 4 in Menu! \n')
# End Menu


# Ticket and Auxilites
def show_ticket():
    '''
        Function for show tickets with options:
        P = Preferred 
        N = Normal Service 
        MD = Material Delivery 
        R = Results 
        G = Get Material 
        Parameter > None.
        Return > None.
    '''
    print('''
========== Choose Ticket ==========
| P = Preferred                   |
| N = Normal Service              | 
| MD = Material Delivery          |
| R = Results                     |  
| G = Get Material                |
===================================
''')


def check_choice_ticket(ticket):
    '''
        This function check the user's ticket.
        Parameter > ticket: string.
        Return > boolean.
    '''
    list_ticket = ['P', 'N', 'MD', 'R', 'G']
    if ticket in list_ticket:
        return True
    else:
        return False


def request_choice_ticket():
    '''
        Request of ticket.
        Options:
        | P = Preferred           |
        | N = Normal Service      |
        | MD = Material Delivery  |
        | R = Results             |
        | G = Get Material        |  
        Parameter > None
        Return >  ticket: string. 
    '''
    while True:
        try:
            show_ticket()
            ticket = input('Type the option: ')
            ticket = ticket.upper()
            if check_choice_ticket(ticket):
                return ticket
            else:
                clear_screen()
                print('Option Incorret! Try again.\n')
                ticket = request_choice_ticket()
                return ticket
        except KeyboardInterrupt:
            clear_screen()
            print('Quit application trought of option 4 in Menu! \n')
# End Ticket and Auxilities
