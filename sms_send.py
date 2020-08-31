#lets put some explanation here

try:
    # Fix UTF8 output issues on Windows console.
    # Does nothing if package is not installed
    from win_unicode_console import enable
    enable()
except ImportError:
    pass

#import json
#import csv
import io
import pprint as pp
from kavenegar import *
try:
    '''#creating a file including receptor numbers
    def Store_some_numbers():
        numbers = ['09351894213', '09123586399','09127904139']
        filename = 'numbers.js'
        with open(filename, 'w') as f_obj:
              json.dump(numbers, f_obj)
    #loading stored numbers
    def load_stored_numbers():
        filename = 'numbers.js'
        with open(filename) as f_obj:
              numbers = json.load(f_obj)
        return numbers
    Store_some_numbers()'''

    api = KavenegarAPI('56466D5134784B41736E575175726B32556572525A372B464E7A3049316D7061')
    #sms_send method will use params for sending sms
    params = {
        'sender': '10001009003000',#sender_number
        'receptor': '09351894213',#multiple mobile number, split by comma
        'message': 'تست وب سرویس پیام کوتاه',
    }
    #sms_recieve method will use params2 for checking inbox
    params2 ={
        'linenumber': '10001009003000',
        'isread': '1',#isread can be true or false.if isread is 1 we will see read messages in inbox
            }
    #params['receptor']=load_stored_numbers()
    #this line get recieved messages(inbox)
    inbox=api.sms_receive(params2)
    #printing inbox
    pp.pprint(inbox)
    #sending sms
    response = api.sms_send(params)
    #printing sending status
    print(response)
#APIException returns a code that shows  API errors (methods,account,...)
except APIException as e:
    print(e)
#HTTPException returns a code that shows web errors
except HTTPException as e:
    print(e)
# just trying to send a pull request to niloofar
#another request that only niloofar should push
#the third request
#pull
#new branch created
