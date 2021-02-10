import eel
import random

eel.init('web')
@eel.expose
def send_command(x):
    print('Hello from %s' % x)

@eel.expose
def py_random():
    return random.random()

eel.start('index.html')