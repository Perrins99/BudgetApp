class Amount:
    
    '''
    creo una classe Amount che contiene amount e description come da specifiche
    e salvo negli oggetti di classe Category una lista di oggetti Amount
    '''
    tot={"amount":0,"description":""}

    def __init__(self,am,descr=""):
        self.tot["amount"]=am
        self.tot["description"]=descr
    
    def getTot(self):
        return self.tot


class Category:

    title=""
    deposit_list=[]
    balance=0

    def __init__(self,name):
        self.title=name
    
    def __str__(self):
        final_string=""
        length=int((30-len(self.title))/2)

        for i in range(0,length):
            final_string+="*"

        final_string+=self.title
        for i in range(0,length):
            final_string+="*"

        final_string+="\n"

        for x in self.deposit_list:
            y=x.getTot()["description"]
            y=y[0:23]
            z=float(x.getTot()["amount"])

            final_string+=y
            l=len(y)
            if l<23:
                for i in range(l,23):
                    final_string+=" "
            
            z=str(z)
            l=len(z)
            if l<7:
                for i in range(l,7):
                    final_string+=" "
            final_string+=z
            final_string+="\n"
        final_string+="Total: "
        final_string+=str(self.balance)

        return final_string

    def get_balance(self):
        return self.balance
    
    def getTitle(self):
        return self.title
        
    def deposit(self,amount,description=""):
        
        if description!="":
            description=str(description)
        dep=Amount(amount,description)
        self.deposit_list.append(dep)
        self.balance+=dep.getTot()["amount"]
    
    def withdraw(self,amount,description=""):
        
        if description!="":
            description=str(description)
        wd=Amount(-1*amount,description)
        if self.check_funds(amount):
            self.deposit_list.append(wd)
            self.balance+=wd.getTot()["amount"]
            return True
        else:
            return False

    def transfer(self,amount,dest):
        descr_dest="Transfer from "
        descr_dest+=self.getTitle()
        descr_src="Transfer to "
        descr_src+=dest.getTitle()
        if self.withdraw(amount,descr_src)==True:
            dest.deposit(amount,descr_dest)
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount>self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    return