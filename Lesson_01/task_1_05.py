class BigBell():
    def __init__(self):
        self.sound_bool = True
    def sound(self):
        if self.sound_bool == True:
            print("ding")
        else:
            print("dong")
        self.sound_bool = not(self.sound_bool)
    
bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
bell.sound()