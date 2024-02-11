def help(name):
    if name == "play":
        print('''
        play(freq, duration)
        This function plays a sound at the frequency inputted for the inputted number of seconds
        :param freq: integer
        :param duration: integer
        ''')
    elif name == "search":
        print('''
        search(measured)
        This function finds and retuns the button state that matches the inputted measurement
        The state is returned as a list of the buttons: [left, center, right, bluetooth]
        :param measured: integer
        :return btn: list of integers
        ''')
    elif name == "read":
        print('''
        read()
        This function returns the current state of the buttons as 1s and 0s in a list
        [left, center, right, bluetooth]
        ''')
    
