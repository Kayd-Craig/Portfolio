class EventManager():
    def __init__(self):
        self.__run_subscribers = []
        self.__enter_subscribers = []

        self.awaiting_input = False
        self.gui_input = ""

    
    def subscribe_run(self, function):
        self.__run_subscribers.append(function)
    
    def publish_run(self, args=None):
        if args is None:
            args = []
        
        for func in self.__run_subscribers:
            func(args)
    

    def subscribe_enter(self, function):
        self.__enter_subscribers.append(function)
    
    def publish_enter(self, args=None):
        self.awaiting_input = False
        self.gui_input = args