# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def handle(self):
#         print("take detour")
# try:
#     raise Accident('car crash between two cars')
# except Accident as e:
#     e.handle()

def processfile():
    try:
        f=open("D:\\code\\PycharmProjects\\Project3\\data.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside exception")
    finally: 
        print("cleaning")
        f.close()
processfile()