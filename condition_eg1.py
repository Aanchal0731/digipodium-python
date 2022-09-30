name = input('enter yout name: ')
email = input('enter your email: ')
mobile = input('enter mobile: ')
city = input('enter city: ')


#nested if-else
if len(name) > 1:
    if '@' in email and len(email) > 11:
        if len(mobile) == 10 and mobile.isnumeric():
            if city in ['lko','delhi','jaipur']:
                print('yr data is saved, Thnk u')
            else:
                print('We are not available in yr city')
        else:
            print('Invalid mobile number🌫')
    else:
        print('Invalid email')
else:
    print('Ye kaisa naam h ❓')
    

