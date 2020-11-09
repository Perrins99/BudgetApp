class Amount:
    
    '''
    creo una classe Amount che contiene amount e description come da specifiche
    e salvo negli oggetti di classe Category una lista di oggetti Amount
    '''
    tot={"amount":0,"description":""}

    def __init__(self,am,descr=""):
        tot["amount"]=am
        tot["description"]=descr



class Category:

    title=""
    deposit_list= list()

    

    def __init__(self,name):
        title=name
    
    def deposit(amount,description):




def create_spend_chart(categories):
    return