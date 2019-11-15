def clear_screen():
    '''
        Only clear the console.
        Parâmeter-> none
        Return-> none
    '''
    import os
    if 'linux' in os.sys.platform:
        os.system('clear')
    else:
        os.system('cls')
    #os.system('cls') - Windows
    #os.system('clear') - Linux