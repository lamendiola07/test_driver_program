#Trial progress for creating <class> for TV

from TV import TV

TV()
def TvUnit():
    #Creating a Television Model Number #1
    television_one = TV()
    print(television_one.setTvModel())
    print(television_one.getPowerButton())
    print(television_one.getTvChannel())
    print(television_one.getTvVolume())
    print(television_one.setTvModel, "'s channel is " + television_one.getTvChannel + "and volume level is" + television_one.getTvVolume)
    
    
    #Creating a Television Model Number #2


TvUnit()