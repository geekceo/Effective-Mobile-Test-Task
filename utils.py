import os
import json
import math
from strings import Strings
from data_models import Transaction
from datetime import date
from typing import Any, Union

STRINGS: Strings = Strings()

class Utils:

    trans_type_dict: dict = {
        '1': 'Доход',
        '2': 'Расход'
    }

    def __new__(cls): ...

    @classmethod
    def __get_data(cls) -> Union[list, bool]:

        try:

            data: list = json.loads(open('data.json', 'r', encoding='utf-8').read())
        except:

            return False

        return data
    
    @classmethod
    def __calculate_balance(cls) -> tuple:

        data: list = cls.__get_data()

        balance: int = 0
        income: int = 0
        expense: int = 0

        for transaction in data:

            if transaction['category'] == 'Доход':

                balance += int(transaction['amount'])
                income += int(transaction['amount'])

            else:

                balance -= int(transaction['amount'])
                expense += int(transaction['amount'])

        return balance, income, expense
    
    @classmethod
    def __write_data(cls, data: Transaction) -> None:

        all_data: Union[list, bool] = cls.__get_data()

        if not all_data:

            all_data = []

            all_data.append(data.__dict__)

        else:

            all_data.append(data.__dict__)
            
        with open('data.json', 'w', encoding='utf-8') as f:

                f.write(json.dumps(all_data, indent=4, ensure_ascii=False))


    def __edit_data(cls, **data) -> None:

        ...

    @staticmethod
    def clear() -> None:

        os.system('clear' if os.name == 'posix' else 'cls')

    @classmethod
    def menu_handler(cls, stage: str):

        cls.clear()

        if stage == '0':
        
            return STRINGS.menu

        elif stage == '1':

            data: Union[list, bool] = cls.__get_data()

            if data:

                balance, income, expense = cls.__calculate_balance()

                return f"{STRINGS.balance.format(balance=balance, income=income, expense=expense)}\n\n{STRINGS.back}"
            
            else:
                
                return f"{STRINGS.balance.format(balance='0', income='0', expense='0')}\n{STRINGS.empty_trans}\n\n{STRINGS.back}"

        elif stage == '2':

            current_date: str = date.today().strftime("%Y-%m-%d")

            category: str = input(STRINGS.transaction_type)

            while not cls.trans_type_dict[category]:

                print(STRINGS.category_error)

                category = input(STRINGS.transaction_type)

            amount: str = input(STRINGS.amount)

            while not amount.isdigit():

                print(STRINGS.digit_error)

                amount = input(STRINGS.amount)

            description: str = input(STRINGS.description)

            transaction: Transaction = Transaction(frozen=True, date=current_date, category=cls.trans_type_dict[category],
                              amount=amount, description=description)
            
            cls.__write_data(data=transaction)

            return f"\n\n{STRINGS.new_data_success}\n\n{STRINGS.back}"
        
        elif stage == '3':

            data: Union[list, bool] = cls.__get_data()

            if data:

                pagination: dict = {k:[] for k in range(1, math.ceil(len(data) / 2) + 1)}

                data.reverse()

                for page in pagination.keys():

                    transaction: dict = data.pop()

                    index: int = cls.__get_data().index(transaction)

                    record: str = f'ID: {index + 1}\n\n' +\
                        f'Дата: {transaction["date"]}\n' +\
                        f'Категория: {transaction["category"]}\n' +\
                        f'Сумма: {transaction["amount"]}\n' +\
                        f'Описание: {transaction["description"]}\n\n'

                    pagination[page].append(record)

                    if data:

                        transaction: dict = data.pop()

                        index: int = cls.__get_data().index(transaction)

                        record: str = f'ID: {index + 1}\n\n' +\
                            f'Дата: {transaction["date"]}\n' +\
                            f'Категория: {transaction["category"]}\n' +\
                            f'Сумма: {transaction["amount"]}\n' +\
                            f'Описание: {transaction["description"]}\n\n'

                        pagination[page].append(record)

                page: int = 1

                edit_menu: str = ''

                while edit_menu != '0':

                    cls.clear()

                    if edit_menu == '+' and page < len(pagination):

                        page += 1

                    elif edit_menu == '-' and page > 1:

                        page -= 1

                    else:

                        page = 1

                    pages: list = [str(num) for num in range(1, len(pagination) + 1)]

                    pages = [num for num in ''.join(pages).replace(str(page), f'|{page}|')]

                    for transaction in pagination[page]:

                        print(f'{transaction}\n')

                    print(' '.join(pages))
                    print(STRINGS.edit_menu)
                    edit_menu = input('Операция: ')

                cls.clear()
                return STRINGS.menu

            else:
                
                return f"{STRINGS.empty_trans}\n\n{STRINGS.back}"
            

            



