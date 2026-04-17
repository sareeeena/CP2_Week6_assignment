class GymMembership:
    def __init__(self,member_name,monthly_fee, remaining_month):
        self._member_name=member_name
        self.monthly_fee=monthly_fee
        self.remaining_months=remaining_month  

           #Bobur 50.0 12

    @property
    def member_name(self):
        return self._member_name   #Bobur
    
    @property
    def monthly_fee(self):
        return self._monthly_fee
    @monthly_fee.setter
    def monthly_fee(self,value):
        if value <=0:
            raise ValueError('Monthly fee must be positive')
        self._monthly_fee=value

    @property 
    def remaining_months(self):
        return self._remaining_months
    @remaining_months.setter
    def remaining_months(self,value):
        if value <1 or value >36:
            raise ValueError('Remaining months must be between 1 and 36')
        self._remaining_months=value
    @property
    def total_cost(self):
        return self.monthly_fee*self.remaining_months
    
    def extend(self,months):
        if months <=0:
            raise ValueError('Extension must be positive')
        total=self.remaining_months+months
        if total >36:
            raise ValueError('Cannot exceed 36 months')
        self.remaining_months=total
    def apply_discount(self,percent):
        if percent <1 or percent >50 :
            raise ValueError('Discount must be between 1 and 50')
        fee=self.monthly_fee*(1-percent/100)
        self.monthly_fee=fee

g = GymMembership("Bobur", 50.0, 12)
print(g.member_name, g.total_cost)

g.extend(6)
print(g.remaining_months)

g.apply_discount(10)
print(g.monthly_fee, g.total_cost)

try:
    g.extend(25)
except ValueError as e:
    print(e)

try:
    g.member_name = "X"
except AttributeError:
    print("Cannot change member name")