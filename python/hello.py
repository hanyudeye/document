import os
import os.path
import time

#class used to handle one application instance mechanism

class ApplicationInstance:
    #specify the file used to save the application instance pid
    def __init__(self,pid_file):
        self.pid_file = pid_file
        self.check()
        self.startApplication()
