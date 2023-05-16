from TV import TV
from simple_colors import *

print(blue("\n\nLOGIE A. MENDIOLA | BSCPE 1 - 5 | OBJECT ORIENTED PROGRAMMING - ASSIGNMENT #6 "))
print(blue("INSTRUCTIONS: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV\n\n"))

print(magenta(" - - - - - - - - - - - - - S T A R T I N G    P R O G R A M - - - - - - - - - - - - - - -\n"))
def TvUnit():
    #Creating a Television Model Number #1
    television_one = TV()
    print(television_one.PowerButton())
    print(television_one.TvModel(),"'s channel is", television_one.TvChannel(), "and volume level is", television_one.TvVolume())

      
    print("\n\n")

    #Creating a Television Model Number #2
    television_two = TV()
    print(television_two.PowerButton())
    print(television_two.TvModel(),"'s channel is", television_two.TvChannel(), "and volume level is", television_two.TvVolume())

TvUnit()
print(yellow("\n - - - - - - - - - - - - - -  E N D I N G     P R O G R A M - - - - - - - - - - - - - - - - -"))