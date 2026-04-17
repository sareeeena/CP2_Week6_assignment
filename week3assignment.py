class LootDrop:
    def __init__(self,item_name,gold_value,count):
        self.item_name=item_name
        self.gold_value=gold_value
        self.count=count
    
    def __str__(self):
        return (f"{self.item_name}: {self.count} drop(s) worth {self.gold_value}g")
    
    def __repr__(self):
        return (f"LootDrop('{self.item_name}', {self.gold_value}, {self.count})")
    
    def __add__(self):
        return
    
    # a=LootDroop('Potion',10.0,3)
    # print(repr(a))
    
    def __add__(self,other):
        if isinstance(other,LootDrop):
            if self.item_name == other.item_name:
                new_count=self.count+other.count
                return LootDrop(self.item_name, self.gold_value,new_count)
            else:
                return NotImplemented   
        elif isinstance(other,int):
            new_value=self.count+other
            return LootDrop(self.item_name,self.gold_value,new_value)
        else:
            return NotImplemented
    
    def __eq__(self,other):
        if isinstance(other,LootDrop):
            if self.item_name == other.item_name and self.gold_value == other.gold_value:
                return True
            else:
                return NotImplemented
    
    def __bool__(self):
        if self.count > 0:
            return True
        else:
            return False
        
drop1 = LootDrop("Health Potion", 15.0, 3)
drop2 = LootDrop("Health Potion", 15.0, 2)
drop3 = LootDrop("Mana Potion", 20.0, 0)

print(str(drop1))
print(repr(drop1))
print(drop1 + drop2)
print(drop1 + 5)
print(drop1 == drop2)
print(bool(drop1))
print(bool(drop3))
    
            











