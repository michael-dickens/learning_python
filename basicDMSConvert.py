while True:
    ddOrDms = str(input("Are your coordinates in Decimal Degrees (DD) or Degrees Minutes Seconds (DMS)? "))
    if ddOrDms == 'DMS':
        try:
            degrees = int(input('What is the degrees of your coordinate? '))
            minutes = int(input('What is the minutes of your coordinate? '))
            seconds = int(input('What is the seconds of your coordinate? '))
            dd =str(degrees + (minutes/60) + (seconds/3600))
            print('Your coordinate is: ' + dd + ' in decimal degrees' )
            break

        except ValueError:
            print('Please use integers for your values')

    elif ddOrDms == 'DD':
        try:
            dd = float(input('What is your coordinate in Decimal Degrees? '))
            positive_dd = dd >= 0
            if not positive_dd:
                dd = abs(dd)
            minutes, seconds = divmod(dd*3600,60)
            degrees, minutes = divmod(minutes, 60)
            seconds = round(seconds, 2)
            if not positive_dd:
                print('Your coordinate is ' + '-' + str(degrees) + ' degrees, ' + str(minutes) + ' minutes, '  + str(seconds) + ' seconds.')
                break
            else:
                print('Your coordinate is ' + str(degrees) + ' degrees, ' + str(minutes) + ' minutes, '  + str(seconds) + ' seconds.')
                break

        except ValueError:
            print('Please type a number')

    elif ddOrDms == 'Q': 
        break
    
    else:
        print("Please type DD or DMS! Or, type Q to quit!")
