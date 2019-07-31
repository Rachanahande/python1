class car:

    def __init__(self, regno,no_gears):
        self.regno=regno
        self.no_gears=no_gears
        self.is_started=False
        self.c_gear=0
    def start(self):
        if self.is_started:
            print(f"car with {self.regno}is already started")
        else:
            print(f"car with {self.regno}is started")
            self.is_started=True

    def stop(self):
        if self.is_started:
            print(f"car with {self.regno}is stopped")
            self.is_started=False
        else:
            print(f"car with {self.regno}is already started")
    def change_gear(self):
        if self.is_started:
            if self.c_gear< self.no_gears:
                self.c_gear+=1
                print(f"car with {self.regno} change gear....{self.c_gear}")
            else:
                 print(f"car with {self.regno}car already in top gear {self.c_gear} ")  
        else:
            print(f"car with {self.regno}is stopped......you cannot change the gear")    
    def showInfo(slef):
        print("{self.regno} ")       