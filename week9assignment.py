from dataclasses import dataclass, field
@dataclass
class Supply:
    name: str
    liters: float
    cost_per_liter: float

    def total_cost(self) -> float:
        return self.liters * self.cost_per_liter
@dataclass
class Event:
    title: str
    guests: int
    supplies: list[Supply] = field(default_factory=list)
    total_cost: float=field(init=False)

    def __post_init__(self):
        self.calculated_cost()

    def calculated_cost(self):
        total=0
        for i in self.supplies:
            total+=i.total_cost()
        self.total_cost = total


    def add_supply(self,supply: Supply):
        self.supplies.append(supply)
        self.calculated_cost()

    def cost_per_guest(self) -> float:
        return self.total_cost / self.guests

    def scale(self,new_guests: int):
        if self.guests == 0:
            raise ValueError("There is no guests")
        result= new_guests / self.guests

        for supply in self.supplies:
            supply.liters *= result
        self.guests=new_guests
        self.calculated_cost()
    
    def display(self) -> str:
        output = []
        output.append(f"{self.title} ({self.guests} guests):")

        for supply in self.supplies:
           output.append(f"  {supply.name}: {supply.liters}L (${supply.total_cost()})")
        output.append(f"Per guest: ${round(self.cost_per_guest(), 1)}")
        return "\n".join(output)
    
e = Event("Gala Dinner", 50)
e.add_supply(Supply("Juice", 25.0, 4.0))
e.add_supply(Supply("Water", 50.0, 1.5))
e.add_supply(Supply("Coffee", 15.0, 6.0))

print(e.total_cost)
print(e.cost_per_guest())
print(e.display())

e.scale(25)
print(e.display())
