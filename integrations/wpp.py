import pywhatkit

def whats_msg(phone, message):
    pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=10)