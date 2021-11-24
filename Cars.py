
class Car:
    speed = 0
    tank_capacity = 50
    batary_capacity = 67

    def __init__(self , name , model , engine):
        self.engine = engine
        self.name = name
        self.model = model
        


    
    def stop(self):
        print ("Engine switched off")
        

    def check_gas(self):
        return self.tank_capacity

    def check_batary(self):
        return self.batary_capacity

    def change_speed(self):
        return self.speed
        

    def choices(self):
        while True :
            if self.engine == 'gas' :
                ask = int(input('1.check Gas 2.change Speed 3.Stop Car : '))
                if ask == 1 :
                    # self.check_gas()
                    print(self.check_gas())
                elif ask == 2 :
                    self.speed += 10
                    print(f'Your Speed {self.speed}')
                elif ask == 3 :
                    self.stop()
                    break
            elif self.engine == 'electric' :
                ask = int(input('1.check Batary 2.change Speed 3.Stop Car : '))
                if ask == 1 :
                    self.check_batary()
                elif ask == 2 :
                    self.speed += 10
                    print(f'Your Speed {self.speed}')
                elif ask == 3 :
                    self.stop()
                    break

    def start(self):
        print ("Engine started")
        self.choices()





car1 = Car('Bmw' , 2008 , 'gas')
car1.start()        


car1 = Car('Tesla' , 2008 , 'electric')
car1.start()
