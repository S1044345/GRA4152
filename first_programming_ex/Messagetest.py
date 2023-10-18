## 
#  This program tests the Customer class.
#
def Messagedemo():
    import argparse 
    import textwrap
    from Message import Message

    parser = argparse.ArgumentParser(prog='Email address simulation',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=textwrap.dedent('''\
                                                 Model of an e-mail message
                                     ------------------------------------------------------------------------------------------
                                     Models an e-mail message with a recipient, sender, and a message text

                                     Methods:
                                     1) append: Adds a line of text to the body of the email
                                        @param the message

                                     2) toString: Converts the lines of the email to string
                                        @return the converted email as a string

                                     3) log_message: is automatically invoked when append is being called.
                                        @return the total number of messages added and the log of messages
                                     '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                     --------------------------------
                                      message1 = Message() # initialize an object
                                      message1.append("Hello there!") # adds a line to the body of the email
                                     ''')
                    )

    parser.add_argument('--init_sender', default= "", type=str)
    parser.add_argument('--init_recipient', default= "", type=str)
    parser.add_argument('--run_demo', action='store_true', help='runs this program')

    args = parser.parse_args()

    if args.run_demo:
        message1 = Message("Justine","Jana")
        message1.append("Hello there!")
        message1.append("How are you doing?")
        message1.append("I hope you are doing well!")
        print(Message._no_messages())
        print("Expected: 3")
        print(Message._log())
        print("Expected: {Justine: {Jana: Hello there\n How are you doing\n I hope you are doing well\n}")

if __name__ == '__main__':
    Messagedemo()