import os

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':

    # insert names and their respective place. For example 0-Jonathan 1-Bob etc
    contacts = []

    # insert the phone number with respect to the order of the contact list
    number = []

    # leave empty
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



