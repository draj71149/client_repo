import time

class GroupExpenseCalculator:
    def __init__(self):
        self.groups = {}

    def run(self):
        while True:
            print("Welcome to Group Expense Calculator")
            print("1. Add the expense")
            print("2. Calculate debts")
            print("3. Exit")
            option = input("Enter option: ")

            if option == '1':
                spender = input("Enter spender’s name: ").strip()
                amount = self.get_float_input("Please input the total spent amount: ")
                members = [m.strip() for m in input("Enter the members of the group including yourself: ").split(",")]

                try:
                    self.add_expense(spender, amount, members)
                    print(self.groups)
                except ValueError:
                    print("Invalid input. Please ensure the amount is a valid number.")

            elif option == '2':
                self.calculate_debts()

            elif option == '3':
                break

    def get_float_input(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                return amount
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def add_expense(self, spender, amount, group_members):


        expense_per_person = amount / len(group_members)

        for member in group_members:
            if member != spender:
                self.update_balance(spender, member, expense_per_person)

    def update_balance(self, payer, payee, amount):
        if payer not in self.groups:
            self.groups[payer] = {}
        if payee not in self.groups:
            self.groups[payee] = {}

        if payee in self.groups[payer]:
            self.groups[payer][payee] += amount
        else:
            self.groups[payer][payee] = amount

        if payer in self.groups[payee]:
            self.groups[payee][payer] -= amount
        else:
            self.groups[payee][payer] = -amount

    def calculate_debts(self):
        for payer, balances in self.groups.items():
            for payee, amount in balances.items():
                if amount > 0:
                    print(f"{payee} owes Rs.{amount:.2f} to {payer}")

if __name__ == "__main__":
    calculator = GroupExpenseCalculator()
    calculator.run()
