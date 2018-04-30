import time

class TimeControlTwitter():
    def __init__(self):
        self.initial_time = time.time()

    def check_one_hour_has_passed(self):
        if time.time() - self.initial_time > 3600:
            return True
        else:
            return False