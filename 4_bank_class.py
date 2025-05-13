class Bank:
    bank_name = "State Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

# Test
b1 = Bank()
b2 = Bank()

print("Initial Bank Name:", Bank.bank_name)

Bank.change_bank_name("New Bank of Pakistan")

print("Bank Name from b1:", b1.bank_name)
print("Bank Name from b2:", b2.bank_name)
print("Bank Name from class:", Bank.bank_name)
