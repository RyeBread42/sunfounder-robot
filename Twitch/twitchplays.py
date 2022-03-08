#--------------------------------------------------------------------#
#      This file contains the code for a twitch controls robot       #
#--------------------------------------------------------------------#

# Imports
import twitch
import keypresser
import keyholder
t = twitch.Twitch()
k = keypresser.Keypresser()

# Main loop
while True:
    # Check for new mesasages
    new_messages = t.twitch_recieve_messages();
 
    if not new_messages:
        continue
    else:
        for message in new_messages:
            # Extract details from message
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg.encode('utf-8'));
 
            # Make approiate
            if msg == "w": keyholder.holdForSeconds(msg, 0.3);
            if msg == "s": keyholder.holdForSeconds(msg, 0.3);
            if msg == "a": keyholder.holdForSeconds(msg, 0.1);
            if msg == "d": keyholder.holdForSeconds(msg, 0.1);
            if msg == "e": keyholder.holdForSeconds(msg, 0.5);
            if msg == "q": keyholder.holdForSeconds(msg, 0.1);
            if msg == "t": keyholder.holdForSeconds(msg, 0.5);