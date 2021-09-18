class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is",self.cpu,self.ram)

com1 = computer("i5",16)
com2 = computer("Ryzen 3",8)

com1.config()
com2.config()

if com1.ram == com2.ram:
    print("They are same")
else:
    print("not same")