#In trial progress of making a class for TV

class TV:
    #Constructing a TV object
    def __init__(self, model = "", power = "", channel = "", volume = ""):
        self.model = model
        self.power = power
        self.channel = channel
        self.volume = volume
    
    #Constructing a Power Button Object:
    def PowerButton(self):
        print("The TV is turned off")
        self.power = input("Turn on the TV? (type 'on' to turn on tv) :")
        if self.power == "on":
            print("*C l i c k*")
            return "The TV is turned on"

    #Constructing a Channel object
    def TvChannel(self):
        self.channel = int(input("Enter channel: "))
        for i in range(0,self.channel):
            self.channel = self.channel
            return self.channel
    
    #Constructing a Volume Level object
    def TvVolume(self):
        self.volume = int(input("Enter Volume Level: "))
        for i in range(0,self.volume):
            self.volume = self.volume
            return self.volume
    
    def TvModel(self):
        self.model = input("What is your TV Model? ")
        return self.model

