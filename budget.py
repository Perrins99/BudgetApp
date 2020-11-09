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

    

    def __init__(self,name):
        title=name
    
    def deposit(self,amount,description):
        dep=Amount(amount,description)
        self.deposit_list.append(dep)


def create_spend_chart(categories):
    return