import os

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    contacts = ['0-zaboo', '1-dylan', '2-shawn', '3-joshua',
                '4-troy', '5-joe', '6-conner', '7-teddy', '8-isaac', '9-jonah', '10-jordan',
                '11-aditya', '12-ryan', '13-atticus', '14-rylan', '15-nathan', '16-ethan']
    number = ['8082065346', '6266880453', '9494260240', '5627469214',
              '5627436168', '2015517176', '8083674772', '9252763247', '9103220006', '3103038607', '6268262795',
              '8189677383', '6268008681', '2132920980', '7144735543', '5627020264', '6268419429']
    text_list = []

    message = input("Type your message:\n>")

    # run = True
    #
    # while run == True:
    print("\n")
    print(contacts)
    print("\n")

    # List numbers like this: 0 1 2 3 4 5 etc
    contact = input("Who would you like to text? Please list all of the numbers separate by space:\n>")
    contact = contact.split(" ")

    contact_place = [eval(i) for i in contact]

    for counter in contact_place:
        text_list.append(number[counter])

    for number in text_list:
        send_message(number, message)



