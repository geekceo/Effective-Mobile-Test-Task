from Tutter import BaseModel

class Transaction(BaseModel):
    
    '''
    This model let build easy data storage to edit and using it in program
    '''

    date: str
    category: str
    amount: str
    description: str