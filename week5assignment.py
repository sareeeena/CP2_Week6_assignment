from abc import ABC, abstractmethod
class Calculator(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def compute(self,value):
        pass

    def describe(self,value):
        computed=self.compute(value)
        return f"{self.name}: {value} -> {computed}"

class CaloriesToKilojoules(Calculator):
    def __init__(self):
        super().__init__("CaloriesToKilojoules")

    def compute(self,value):
        self.value=value
        return round(self.value* 4.184, 2)
    
class GramsToOunces(Calculator):
    def __init__(self):
        super().__init__("GramsToOunces")

    def compute(self, value):
        self.value=value
        return round(value * 0.035274, 2)
    
class CupsToMilliliters(Calculator):
    def __init__(self):
        super().__init__("CupsToMilliliters")

    def compute(self,value):
        self.value=value
        return round(value * 236.588, 2)
    
class CustomCalculator:
    def __init__(self,name,factor):
        self.factor=factor
        self.name=name 
    
    def compute(self,value):
        self.value=value
        return round(value * self.factor, 2)
    
    def describe(self,value):
        computed=self.compute(value)
        return f"{self.name}: {value} -> {computed}"
    
class CalculationLog:
    def __init__(self):
        self.entries=[]

    def record(self,calc_name,original,computed):
        self.entries.append(f"{calc_name}: {original} -> {computed}")

    def show(self):
        for entry in self.entries:
            print(entry)
      
class NutritionLab:
    def __init__(self,name):
        self.name=name
        self.calculators=[]
        self.calc_log = CalculationLog()

    def add_calculator(self,calculator):
        self.calculators.append(calculator)
        

    def compute_all(self,value):
        print(f"=== {self.name} ===")
        for calculator in self.calculators:
            result1=calculator.describe(value)
            print(result1)
            result2=calculator.compute(value)
            self.calc_log.record(calculator.name,value, result2)

    def show_log(self):
        print (f"--- Log for {self.name} ---")
        self.calc_log.show()


lab = NutritionLab('Diet Clinic')
lab.add_calculator(CaloriesToKilojoules())
lab.add_calculator(GramsToOunces())
lab.add_calculator(CupsToMilliliters())
lab.add_calculator(CustomCalculator('TspsToMl', 4.929))

lab.compute_all(500)
print()
lab.compute_all(120)
print()
lab.show_log()

try:
    c = Calculator('test')
except TypeError:
    print('Cannot instantiate abstract class')


    
        





    



















































































































































































































































    