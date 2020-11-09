class Amount:
    
    '''
    creo una classe Amount che contiene amount e description come da specifiche
    e salvo negli oggetti di classe Category una lista di oggetti Amount
    '''
    tot={}

    def __init__(self,am,descr=""):
        self.tot["amount"]=am
        self.tot["description"]=descr
    
    def getTot(self):
        return self.tot


class Category:

    title=""
    deposit_list= list()
    balance=0

    

    def __init__(self,name):
        title=name
    
    def deposit(self,amount,description):
        dep=Amount(amount,description)
        self.deposit_list.append(dep)
        self.balance+=dep.getTot()["amount"]
    
    def withdraw(self,amount,description):
        wd=Amount(-1*amount,description)
        if self.balance-amount>=0:
            self.deposit_list.append(wd)
            self.balance+=wd.getTot()["amount"]
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

def create_spend_chart(categories):
    return