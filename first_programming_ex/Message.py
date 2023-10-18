
# Creates a Message class that models an e-mail message. A message has a recipient, a sender, and a message text.

class Message:

    _no_messages = 0 #A class variable for saving the total number of messages sent.
    _log = {} #A class variable that saves a log of the messages sent.

    #Constructs a Message class that takes a sender and a recipient

    def __init__ (self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

        Message._no_messages = Message._no_messages + 1

     