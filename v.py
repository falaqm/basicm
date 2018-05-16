'''Class'''
import locale
import sys
class Base():
    '''represent'''
    trim='normal'
    enginelitres=1.5
    milesrange=450
    tankcapacity=45
    color='white'
    transmission='automatic'

    @staticmethod
    def milesperlitre(milesrange,tankcapacity):
        return milesrange/tankcapacity
    
    def milespergallon(milesrange,tankcapacity):
        return Base.milesperlitre(milesrange,tankcapacity)*3.78451
    milespergallon=staticmethod(milespergallon)




    

    def __init__(self,price,transmission='automatic',color='white'):
        self.price=price
        self.transmission=transmission
        self.color=color

    def info(self):
        if sys.platform.startswith('win'):
            locale.setlocale(locale.LC_ALL,'zh-CN')
           
        else:
            locale.setlocale(locale.LC_ALL,'en_US.utf8')
        print('price of %s was %s' %(self,locale.currency(self.price)))

    def enginesound(self):
        return 'putt,putt'
    def hornsound(self):
        return 'honk,honk'
    def __str__(self):
        return ' %s base model with %s transmission' %(self.color,self.transmission) 

coop=Base(25000,color='red',transmission='fast')
coop.info()
print('The %s gets %4.1f miles per gallon' %(coop,coop.milespergallon(coop.milesrange,coop.tankcapacity)))
print('The %s gets %4.1f miles per gallon' %(Base,Base.milespergallon(Base.milesrange,Base.tankcapacity)))


class Sport(Base):
    #inherited class
    enginelitres=2.0
    milesrange=400

print('*'*50)
sport=Sport(color='orange',transmission='manual',price=50000)
sport.info()

print('The %s gets %4.1f miles per gallon' %(sport,sport.milespergallon(sport.milesrange,sport.tankcapacity)))
print('The %s gets %4.1f miles per gallon' %(Sport,Sport.milespergallon(Sport.milesrange,Sport.tankcapacity)))




