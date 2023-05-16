from simple_colors import *

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
            self.power = input("Turn on the TV? (type 'on' to turn on tv): ")
            if self.power == "on":
                print("*C l i c k*")
                return "The TV is turned on \n"

        #Constructing a Channel object
        def TvChannel(self):
            self.channel = int(input("Enter channel: "))
            for i in range(0,self.channel):
                self.channel = self.channel

                #Changing channel number
                change_channel = input("Change channel number? (type '^' or 'v' to increase/decrease channel number) :")
                if change_channel == "^":
                    self.channel = (green(self.channel + 1))
                    return self.channel

                elif change_channel == "v":
                    self.channel = (red(self.channel - 1))
                    return self.channel

        #Constructing a Volume Level object
        def TvVolume(self):
            self.volume = int(input("\nEnter Volume Level: "))
            for i in range(0,self.volume):
                self.volume = self.volume
            
                change_volume = input("change volume level? (type '^' or 'v' to increase/decrease channel number) :")

                #Changing volume level
                if change_volume == "^":
                    self.volume = (green(self.volume + 1))
                    return self.volume

                elif change_volume == "v":
                    self.volume = (red(self.volume - 1))
                    return self.volume

        def TvModel(self):
            self.model = input("What is your TV Model? ")
            self.model = (yellow(self.model))
            return self.model

