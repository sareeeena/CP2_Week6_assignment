class ToolRental:
    shop_name="BuildIt Hardware"
    min_deposit=10
    total_rentals=0
    def __init__ (self,renter,deposit=0,history=None):
        self.renter=renter
        self.deposit=deposit
        if history is None:
            self.history=[]
        else:
            self.history=history
        ToolRental.total_rentals+=1
    def add_deposit(self,amount):
        if amount > 0:
            self.deposit+=amount
            self.history.append(f"+{amount}")
            print(f"Added deposit {amount}. Total: {self.deposit}")
    def rent_tool(self,fee):
        if self.deposit-fee >= ToolRental.min_deposit:
            self.deposit-=fee
            self.history.append(f"-{fee}")
            print(f"Rented tool for {fee}. Remaining: {self.deposit}")
        else:
            print("Insufficient deposit for rental")
    def display_rental(self):
        print(f"Renter: {self.renter}, Deposit: {self.deposit}, Shop: {self.shop_name}")
    def show_history(self):
        for entry in self.history:
            print(entry)

rental1=ToolRental("Shokir", deposit=20)
rental1.display_rental()
rental1.add_deposit(40)
rental1.rent_tool(15)
rental1.rent_tool(25)
rental1.show_history()

print(f"Total rentals: {ToolRental.total_rentals}")
