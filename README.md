# ClubText
This is an application where you can send a shared message to multiple recipients using imessage on IOS or macOS

The code first utilises Applescript to send messages through iMessage. Requires iOS or macOS to operate
              **on run {targetPhoneNumber, targetMessageToSend}
                  tell application "Messages"
                      set targetService to 1st service whose service type = iMessage
                      set targetBuddy to buddy targetPhoneNumber of targetService
                      set targetMessage to targetMessageToSend
                      send targetMessage to targetBuddy
                  end tell
              end run**
              
The python file requires two input to use:

1. contacts = []    **# insert names and their respective place. For example 0-Jonathan 1-Bob etc**
2. number = []      **# insert the phone number with respect to the order of the contact list**

Then, the code should be ready to go
  
