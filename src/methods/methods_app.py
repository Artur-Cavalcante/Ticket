# -*- coding: utf-8 -*-

from methods_ticket import request_choice_menu, request_choice_ticket
from clear_screen import clear_screen

# Functions for each option of menu.
def emission_ticket(choice_ticket, dict_number_ticket, dict_row_ticket):
    if choice_ticket == 'P':
        dict_number_ticket['ticket_P'] += 1
        dict_row_ticket['5'].append('P' + str(dict_number_ticket['ticket_P']))
    elif choice_ticket == 'N':
        dict_number_ticket['ticket_N'] += 1
        dict_row_ticket['4'].append('N' + str(dict_number_ticket['ticket_N']))
    elif choice_ticket == 'MD':
        dict_number_ticket['ticket_MD'] += 1
        dict_row_ticket['3'].append('MD' + str(dict_number_ticket['ticket_MD']))
    elif choice_ticket == 'R':
        dict_number_ticket['ticket_R'] += 1
        dict_row_ticket['2'].append('R' + str(dict_number_ticket['ticket_R']))
    elif choice_ticket == 'G':
        dict_number_ticket['ticket_G'] += 1
        dict_row_ticket['1'].append('G' + str(dict_number_ticket['ticket_G']))

    return dict_number_ticket, dict_row_ticket

def call_ticket(dict_row_ticket, list_call_ticket):
    '''
        Call the ticket in queue according with priority.
        Parameter > dict_row_ticket: dict.
                    list_call_ticket: list.
        Return    > dict_row_ticket: dict.
                    list_call_ticket: list.
    '''
    # Do pop in list of queue.
    if len(dict_row_ticket['5']):
        print('Calling: ', dict_row_ticket['5'][0])
        list_call_ticket.append(dict_row_ticket['5'].pop(0))        
    elif len(dict_row_ticket['4']):
        print('Calling: ', dict_row_ticket['4'][0])
        list_call_ticket.append(dict_row_ticket['4'].pop(0))        
    elif len(dict_row_ticket['3']):
        print('Calling: ', dict_row_ticket['3'][0])
        list_call_ticket.append(dict_row_ticket['3'].pop(0))
    elif len(dict_row_ticket['2']):
        print('Calling: ', dict_row_ticket['2'][0])
        list_call_ticket.append(dict_row_ticket['2'].pop(0))
    elif len(dict_row_ticket['1']):
        print('Calling: ', dict_row_ticket['1'][0])
        list_call_ticket.append(dict_row_ticket['1'].pop(0))
    else:
        print('No have ticket in queue for called!')

    return dict_row_ticket, list_call_ticket

def show_queue(dict_row_ticket):
    '''
        This function only show the row of ticket.
        Parameter > dict_row_ticket: dict
        Return > None
    '''
    print('==Queue of tickets== \n ')
    print('Preferred         : ', end=' ')
    for ticket in dict_row_ticket['5']:
        print(ticket + '-', end= '')
    print()
    print('Normal Service    : ', end=' ')
    for ticket in dict_row_ticket['4']:
        print(ticket + '-', end= '')
    print()
    print('Material Delivery : ', end=' ')
    for ticket in dict_row_ticket['3']:
        print(ticket + '-', end= '')
    print()
    print('Results           : ', end=' ')
    for ticket in dict_row_ticket['2']:
        print(ticket + '-', end= '')
    print()
    print('Get Material      : ', end=' ')
    for ticket in dict_row_ticket['1']:
        print(ticket + '-', end= '')
    print()

def check_queue(dict_row_ticket):
    '''
        Check if have any ticket on queue.
        Parameter > dict_row_ticket: dict.
        Return > boolean.
    '''
    if len(dict_row_ticket['5']) > 0:
        return True
    elif len(dict_row_ticket['4']) > 0:
        return True
    elif len(dict_row_ticket['3']) > 0:
        return True
    elif len(dict_row_ticket['2']) > 0:
        return True
    elif len(dict_row_ticket['1']) > 0:
        return True
    else:
        return False
# End Functions

# Function for initialize the app.
def start_app():
    '''
        This function is for start app, it use the user' choice and dicts auxilities.
        Parameter > choice: int.
                    list_call_ticket: list.
                    dict_number_ticket: dict.
                    dict_row_ticket: dict.
        Return > None.
    '''
    #First dict for add with ticket, second for append in row.
    dict_number_ticket = {'ticket_P': 0, 'ticket_N': 0, 'ticket_MD': 0, 'ticket_R': 0, 'ticket_G': 0} 
    dict_row_ticket = {'1': [], '2': [], '3' : [], '4' : [], '5' : []}
    list_call_ticket = [] 
    
    choice = request_choice_menu() # Choice of menu
    while True:
        if choice == 1:
            clear_screen() 
            choice_ticket = request_choice_ticket() # Choice of ticket
            dict_number_ticket, dict_row_ticket = emission_ticket(choice_ticket, dict_number_ticket, dict_row_ticket) # Save the emissions
            clear_screen() 
            choice = request_choice_menu() # Choice of menu, again for contiue the menu
        elif choice == 2:
            clear_screen()
            dict_row_ticket, list_call_ticket = call_ticket(dict_row_ticket, list_call_ticket)
            choice = request_choice_menu()
        elif choice == 3:
            clear_screen()
            show_queue(dict_row_ticket)
            choice = request_choice_menu()
        elif choice == 4: # If have any in queue.
            clear_screen()
            if check_queue(dict_row_ticket):
                print('Have tickets waiting to be called! \n')
            else:
                break
            choice = request_choice_menu()
    # Quiting...
    clear_screen()
    print('''
End of Application! 
The called tickets was:
''')
    if len(list_call_ticket):
        for ticket in range(len(list_call_ticket)):
            print(list_call_ticket[ticket], end='-')
    else:
        print('No ticket called\n')
    print('\nArtur-Cavalcante')

# End Function for initialize the app.