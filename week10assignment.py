class BlendError(Exception):
    pass

class BlendNotFoundError(BlendError):
    def __init__(self,blend_name):
        self.blend_name=blend_name
        super().__init__(f'Blend not found: {blend_name}')

class DuplicateBlendError(BlendError):
    def __init__(self, blend_name):
        self.blend_name=blend_name
        super().__init__(f"Blend already exists: {blend_name}")

class InvalidPlotsError(BlendError):
    def __init__(self,plots):
        self.plots=plots
        super().__init__(f"Invalid plots: {plots}. must be positive")

class MissingMineralsError(BlendError):
    def __init__(self, blend_name,missing):
        self.blend_name=blend_name
        self.missing=missing
        super().__init__(f"Cannot prepare {blend_name}: missing {missing}")

class BlendPlanner:
    def __init__(self):
        self.blends={}

    def add_blend(self,name,plots: int,minerals: float):
        # self.name =name
        # self.plots= plots
        # self.minerals = minerals
        if name in self.blends:
            raise DuplicateBlendError(name)
        
        if plots <= 0:
            raise InvalidPlotsError(plots)
        
        self.blends[name] = {"plots": plots, "minerals": minerals}

    def scale_blend(self, name,desired_plots):
        try:
            blend1 = self.blends[name]
        except KeyError:
            raise BlendNotFoundError(name) from None
        
        if desired_plots < 0:
            raise InvalidPlotsError(desired_plots)
        
        factor = desired_plots / blend1["plots"]
        calculated = {}
        for mineral, amount in blend1["minerals"].items():
            calculated[mineral] = round(amount * factor, 2)
        return calculated
    
    def check_stock(self, name, stock):
        try:
            minerals = self.blends[name]["minerals"]
        except KeyError:
            raise BlendNotFoundError(name) from None
        missing = {}
        for mineral_name, amount in minerals.items():
            available = stock.get(mineral_name, 0)
            if amount > available:
                missing_amount = round(amount - available, 2)
                missing[mineral_name] = missing_amount
                raise MissingMineralsError(name, missing)
        return True
            
planner = BlendPlanner()

planner.add_blend("Growth Mix", 5, {"nitrogen": 10.0, "phosphorus": 4.0, "potassium": 6.0})
planner.add_blend("Bloom Boost", 3, {"phosphorus": 9.0, "potassium": 3.0, "iron": 1.5})

scaled = planner.scale_blend("Growth Mix", 10)
print(f"growth mix for 10: {scaled}")

scaled = planner.scale_blend("Bloom Boost", 1)
print(f"bloom boost for 1: {scaled}")

stock = {"nitrogen": 10.0, "phosphorus": 1.0, "potassium": 6.0}
try:
    planner.check_stock("Growth Mix", stock)
except BlendError as e:
    print(e)

stock2 = {"phosphorus": 15.0, "potassium": 5.0, "iron": 3.0}
result = planner.check_stock("Bloom Boost", stock2)
print(f"can prepare bloom boost: {result}")

tests = [
    lambda: planner.add_blend("Growth Mix", 5, {"nitrogen": 2.0}),
    lambda: planner.scale_blend("Root Strong", 4),
    lambda: planner.scale_blend("Growth Mix", -3),
]

for test in tests:
    try:
        test()
    except BlendError as e:
        print(e)

        
    

        


    
