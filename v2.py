'''Class inheritance'''
import locale
import sys
class Base():
    '''represent'''
    trim='normal'
    enginelitres=1.5

    def enginesound(self):
        return 'putt,putt'
    def hornsound(self):
        return 'honk,honk'
    def __str__(self):
        return 'Base Model' 

coop=Base()

print('The %s gets %s trim level' %(coop,coop.trim))
print('The %s gets %s engine lites level' %(coop,coop.enginelitres))
print('The %s gets %s  enginesound' %(coop,coop.enginesound()))
print('The %s gets %s horn' %(coop,coop.hornsound()))


class Sport(Base):
    #inherited class
    enginelitres=2.0
    def enginesound(self):
        return 'VROOM VROOM'
    def hornsound(self):
        return 'BEEP BEEP'
    def __str__(self):
        return "Sport Model"

print('*'*50)
coopy=Sport()
print('The %s gets %s trim level' %(coopy,coopy.trim))
print('The %s gets %s engine lites level' %(coopy,coopy.enginelitres))
print('The %s gets %s  enginesound' %(coopy,coopy.enginesound()))
print('The %s gets %s horn' %(coopy,coopy.hornsound()))

class Luxury(Base):
    #inherited class
    trim='luxury'
    def enginesound(self):
        return 'vroom vroom'
    def hornsound(self):
        return 'honk honk'
    def __str__(self):
        return "Luxury Model"

print('*'*50)
coopl=Luxury()
print('The %s gets %s trim level' %(coopl,coopl.trim))
print('The %s gets %s engine lites level' %(coopl,coopl.enginelitres))
print('The %s gets %s  enginesound' %(coopl,coopl.enginesound()))
print('The %s gets %s horn' %(coopl,coopl.hornsound()))


class LuxurySport(Luxury,Sport):
    #inherited class
    def __str__(self):
        return "Luxury Sport Model"

print('*'*50)
cooplx=LuxurySport()
print('The %s gets %s trim level' %(cooplx,cooplx.trim))
print('The %s gets %s engine lites level' %(cooplx,cooplx.enginelitres))
print('The %s gets %s  enginesound' %(cooplx,cooplx.enginesound()))
print('The %s gets %s horn' %(cooplx,cooplx.hornsound()))


class SportLuxury(Sport,Luxury):
    #inherited class
    def __str__(self):
        return "Sport Luxury Model"

print('*'*50)
cooplz=SportLuxury()
print('The %s gets %s trim level' %(cooplz,cooplz.trim))
print('The %s gets %s engine lites level' %(cooplz,cooplz.enginelitres))
print('The %s gets %s  enginesound' %(cooplz,cooplz.enginesound()))
print('The %s gets %s horn' %(cooplz,cooplz.hornsound()))


coopcustom=SportLuxury()
print('The %s gets %s trim level' %(coopcustom,coopcustom.trim))
coopcustom.trim='custom'
print('The %s gets %s trim level' %(coopcustom,coopcustom.trim))
print('The %s gets %s trim level' %(SportLuxury,SportLuxury.trim))

coopcustom.brake='racing'
Base.brake='standard'
print('The %s gets %s brake level' %(coopcustom,coopcustom.brake))
print('The %s gets %s brake level' %(SportLuxury,SportLuxury.brake))
