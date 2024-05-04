from Tutter import BaseModel

class Transaction(BaseModel):
    
    date: str
    category: str
    amount: str
    description: str