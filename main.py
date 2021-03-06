from application import Application
import eel
import random

eel.init('web')
@eel.expose
def send_command(x):
    print('Hello from %s' % x)
    try:
        application.go()
        eel.update_state(application.state) 
    except Exception as e:
        eel.update_state("state machine error\r\n" + str(e)) 

@eel.expose
def py_random():
    return random.random()

application = Application()

print(application.state)
eel.update_state(application.state) 

eel.start('index.html', mode='edge')