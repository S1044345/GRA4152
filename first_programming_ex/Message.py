
# Creates a Message class that models an e-mail message. A message has a recipient, a sender, and a message text.

class Message:

    _no_messages = 0 #A class variable for saving the total number of messages sent.
    _log = {} #A class variable that saves a log of the messages sent.

    #Constructs a Message class that takes a sender and a recipient

    def __init__ (self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.body = ""

    #Method that adds a line to the body of the email
    def append (self, line):
        self.body += line + "\n"
        self.log_messages()

    #Method that converts the message into a string
    def toString (self):
        message = "From: {}\nTo: {}\n\n{}\n".format(self.sender,self.recipient,self.body)
        return message

    #Method that automatically increases no of messages and add a log of the message
    def log_messages (self):
        Message._no_messages = Message._no_messages + 1
        if self.sender not in Message._log:
            Message._log[self.sender] = {}

        Message._log[self.sender][self.recipient] = self.body
