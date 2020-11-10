import copy

class Amount:
    
    

    def __init__(self,am,descr=""):
        self.tot={"amount":0,"description":""}
        self.tot["amount"]=am
        self.tot["description"]=descr
    
    def getTot(self):
        return self.tot


class Category:



    def __init__(self,name):
        self.title=name
        self.ledger=list()
        self.balance=0
    
    def __str__(self):
        final_string=""
        length=int((30-len(self.title))/2)

        for i in range(0,length):
            final_string+="*"

        final_string+=self.title
        for i in range(0,length):
            final_string+="*"

        final_string+="\n"

        for x in self.ledger:
            y=x["description"]
            y=y[0:23]
            z=float(x["amount"])

            final_string+=y
            l=len(y)
            if l<23:
                for i in range(l,23):
                    final_string+=" "
            
            z=str("{:7.2f}".format(z))
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
        self.ledger.append(dep.getTot())
        self.balance+=dep.getTot()["amount"]
        
    
    def withdraw(self,amount,description=""):
        
        if description!="":
            description=str(description)
        
        wd=Amount(-1*amount,description)

        if self.check_funds(amount):
            self.ledger.append(wd.getTot())
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
    
    chart="Percentage spent by category\n"
    '''
    per ogni barra verticale stampare 3 trattini 
    + 1 trattino finale
    '''
    
    
    percentages=[]
    
    sum=0
    for x in categories:
        for y in x.ledger:
            if y["amount"]<0:
                sum+=y["amount"]

    part_sum=0
    for x in categories:
        for y in x.ledger:
            if y["amount"]<0:
                part_sum+=y["amount"]
        percentages.append(part_sum*100/sum)
        part_sum=0

    k=100

    while k>=0:
        if k<100:
            if k==0:
                chart+="  "
            else:
                chart+=" "
        
        chart+=str(k)
        chart+="|"
        
        for x in percentages:
            if x>=k:
                chart+=" o "
            else:
                chart+="   "
            
        chart+=" \n"
        k-=10

    chart+="    "
    for x in range(0,len(categories)):
        chart+="---"
    chart+="-\n"

    l=0
    for x in categories:
        if len(x.title)>l:
            l=len(x.title)

    for k in range(0,l):
        chart+="     "
        for x in categories:
            if len(x.title)<k+1:
                chart+=" "
            else:
                chart+=x.title[k]

            chart+="  "
        
        if k!=l-1:
            chart+="\n"

    return chart