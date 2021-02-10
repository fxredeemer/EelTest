from transitions import Machine
from typing import List

class Application(object):
    states : List[str] = ["Starting", "Running", "Closing", "Aborted"]

    state : str
    
    def __init__(self) -> None:
        self.machine = Machine(model=self, states=Application.states, initial="Starting")

        self.machine.add_transition(trigger="go", source="Starting", dest="Running", before="do_run")

        self.machine.add_transition(trigger="close", source="Running", dest="Closing")
        
        self.machine.add_transition(trigger="abort", source='*', dest='Aborted')

    def do_run(self) -> None:
        print("running")

    def do_close(self) -> None:
        print("closing")