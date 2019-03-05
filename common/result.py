class Result:
    """
    the class for return result
    """
    def __init__(self):
        self.ok = False
        self.msg = ''

    def set_ok(self, is_ok):
        """
        set the ok property in the result
        
        Arguments:
            is_ok {bool} -- is ok
        """        
        self.ok = is_ok
    
    def set_msg(self, msg):
        """
        set the message in the result
        
        Arguments:
            msg {str} -- the message you want to return
        """
        self.msg = msg
    