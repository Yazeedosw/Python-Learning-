#Bank account project:
from datetime import datetime


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(
            f"تم إيداع {amount} ريال لرصيدك البنكي في يوم {datetime.now().strftime('%A')}، {datetime.now().strftime('%d %B %Y')}، الساعة {datetime.now().strftime('%I:%M%p')}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("لا يمكن السحب، رصيدك البنكي غير كافٍ.")
        else:
            self.balance -= amount
            print(
                f"تم خصم {amount} ريال من رصيدك البنكي في يوم {datetime.now().strftime('%A')}، {datetime.now().strftime('%d %B %Y')}، الساعة {datetime.now().strftime('%I:%M%p')}.")

    def check_balance(self):
        print(f"رصيدك البنكي الحالي هو: {self.balance} ريال.")


# إنشاء حساب بنكي جديد
my_account = BankAccount()

# إيداع مبلغ
my_account.deposit(2000)

# سحب مبلغ
my_account.withdraw(150)

# الاستعلام عن الرصيد
my_account.check_balance()
