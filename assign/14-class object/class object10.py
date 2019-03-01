#2.define a class Account with static variable rate_of_interest.instance variable
#balance and accountno. Make function to set values in instance object of account
#,show balance,show rate_of_interest,withdraw and deposite.
class Account:
    rate_of_interest=eval(input("enter rate of interest\n"))
    def info(self,balance,ac):
        print("balance is %d"%balance,",","account no is %d"%ac)
bal=int(input("enter account balance\n"))
acc=int(input("enter account no\n"))
c1=Account()
Account.rate_of_interest=2
print(Account.rate_of_interest)
c1.info(bal,acc)
