"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, hours_worked = 0, commission = "", commission_amount = 0, contracts_done = 0):
        self.name = name
        self.commission = commission
        self.hours_worked = hours_worked
        self.salary = salary
        self.commission_amount = commission_amount
        self.contracts_done = contracts_done

    def get_hourly_pay(self):
        hourly_pay = hours_worked * salary
        if commission != False:
            if commision == "Bonus":
                hourly_pay += commission_amount
            else:
                hourly_pay += commission_amount * contracts_done
        return hourly_pay

    def get_monthly_pay(self):
        monthly_pay = salary
        if commission != False:
            if commision == "Bonus":
                monthly_pay += commission_amount
            else:
                monthly_pay += commission_amount * contracts_done
        return monthly_pay
        

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, "Contract", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, "Contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, "Bonus", 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, "Bonus", 600, 0)
