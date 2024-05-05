import os
import re
import json
import math
from strings import Strings
from data_models import Transaction
from datetime import date
from typing import Any, Union
from types import FunctionType

STRINGS: Strings = Strings()

class Utils:

    trans_type_dict: dict = {
        '1': 'Доход',
        '2': 'Расход',
        'Доход': '1',
        'Расход': '1'
    }

    def __new__(cls): ...

    @classmethod
    def __get_data(cls) -> Union[list, bool]:

        '''
        This func let reading data from json file and return list or bool value
        '''

        try:

            data: list = json.loads(open('data.json', 'r', encoding='utf-8').read())
        except:

            return False

        return data
    
    @classmethod
    def __calculate_balance(cls) -> tuple:

        '''
        This func calculate three balances - total balance, income balance and expense balance
        '''

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

        '''
        This func let wirte data to json file via Transaction model of data
        '''

        all_data: Union[list, bool] = cls.__get_data()

        if not all_data:

            all_data = []

            all_data.append(data.__dict__)

        else:

            all_data.append(data.__dict__)
            
        with open('data.json', 'w', encoding='utf-8') as f:

                f.write(json.dumps(all_data, indent=4, ensure_ascii=False))

    @classmethod
    def __edit_data(cls, transaction_id: int) -> None:

        '''
        This func let edit transactions data via transaction id from local 'database'
        '''

        data: list = cls.__get_data()

        transaction: Transaction = Transaction(frozen=True, **data[transaction_id])

        category: str = input(f'{STRINGS.transaction_type} (Enter: {transaction.category}): ')

        if category == '':

            category = transaction.category

        while category not in cls.trans_type_dict.keys() and category != '':

            print(STRINGS.category_error)

            category = input(f'{STRINGS.transaction_type} (Enter: {transaction.category}): ')

        amount: str = input(f'{STRINGS.amount} (Enter: {transaction.amount}): ')

        if amount == '':

            amount = transaction.amount

        while not amount.isdigit():

            print(STRINGS.digit_error)

            amount = input(f'{STRINGS.amount} (Enter: {transaction.amount}): ')

        description: str = input(f'{STRINGS.description} (Enter: {transaction.description}): ')

        if description == '':

            description = transaction.description

        data[transaction_id]['category'] = category
        data[transaction_id]['amount'] = amount
        data[transaction_id]['description'] = description

        with open('data.json', 'w', encoding='utf-8') as f:

            f.write(json.dumps(data, indent=4, ensure_ascii=False))



    @staticmethod
    def clear() -> None:

        os.system('clear' if os.name == 'posix' else 'cls')

    @classmethod
    def __pagination_mixin(cls, data: list) -> dict:

        '''
        Mixin to pagination that using in more parts of code
        '''

        pagination: dict = {k:[] for k in range(1, math.ceil(len(data) / 2) + 1)}

        all_data: list = data.copy()

        data.reverse()

        for page in pagination.keys():

            transaction: dict = data.pop()

            index: int = all_data.index(transaction)

            record: str = f'ID: {index + 1}\n\n' +\
                f'Дата: {transaction["date"]}\n' +\
                f'Категория: {transaction["category"]}\n' +\
                f'Сумма: {transaction["amount"]}\n' +\
                f'Описание: {transaction["description"]}\n\n'
            
            pagination[page].append(record)

            if data:

                transaction: dict = data.pop()

                index: int = all_data.index(transaction)

                record: str = f'ID: {index + 1}\n\n' +\
                    f'Дата: {transaction["date"]}\n' +\
                    f'Категория: {transaction["category"]}\n' +\
                    f'Сумма: {transaction["amount"]}\n' +\
                    f'Описание: {transaction["description"]}\n\n'
                
                pagination[page].append(record)

        return pagination
    
    @classmethod
    def __get_search_filter(cls, search_request: str) -> str:

        '''
        This function let get type of search filter - category, date or amount to autodetect this for smart search
        '''

        search_filter: str

        pattern: str = "^\d{4}-\d{2}-\d{2}$"

        if re.match(pattern, search_request):

            search_filter = 'date'

        elif search_request.isdigit():

            search_filter = 'amount'

        else:

            search_filter = 'category'
        
        return search_filter

    @classmethod
    def menu_handler(cls, stage: str, test: bool = False):

        cls.clear()

        if stage == '0':
        
            return STRINGS.menu

        elif stage == '1':

            data: Union[list, bool] = cls.__get_data()

            if data:

                balance, income, expense = cls.__calculate_balance()

                return f"{STRINGS.balance.format(balance=balance, income=income, expense=expense)}\n\n{STRINGS.back}"
            
            else:

                if test:

                    return 0, 0, 0
                
                return f"{STRINGS.balance.format(balance='0', income='0', expense='0')}\n{STRINGS.empty_trans}\n\n{STRINGS.back}"

        elif stage == '2':

            current_date: str = date.today().strftime("%Y-%m-%d")

            category: str = input(STRINGS.transaction_type)

            while category not in cls.trans_type_dict.keys():

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

            if not cls.__get_data():

                return f'\n{STRINGS.empty_trans}\n\n{STRINGS.back}'

            data: FunctionType = cls.__get_data

            if data:

                pagination: dict = cls.__pagination_mixin(data=data())

                page: int = 1

                edit_menu: str = ''

                while edit_menu != '0':

                    pagination = cls.__pagination_mixin(data=data())

                    cls.clear()

                    if edit_menu == '+' and page < len(pagination):

                        page += 1

                    elif edit_menu == '-' and page > 1:

                        page -= 1

                    elif edit_menu.isdigit() and edit_menu != '0':

                        page = int(edit_menu) if int(edit_menu) <= len(pagination) else 1

                    elif 'R' in edit_menu:

                        index: int = int(edit_menu.replace('R', ''))

                        if index <= len(data()):

                            cls.__edit_data(transaction_id=index - 1)
                            pagination = cls.__pagination_mixin(data=data())

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
            
        elif stage == '4':

            if not cls.__get_data():

                return f'\n{STRINGS.empty_trans}\n\n{STRINGS.back}'

            search_menu: str = input(STRINGS.search_menu)

            search_filter = cls.__get_search_filter(search_request=search_menu)

            data: list = [elem for elem in cls.__get_data() if elem[search_filter] == search_menu]

            if data:

                pagination: dict = cls.__pagination_mixin(data=data)

                page: int = 1

                edit_menu: str = ''

                while edit_menu != '0':

                    data = [elem for elem in cls.__get_data() if elem[search_filter] == search_menu]

                    pagination = cls.__pagination_mixin(data=data)

                    cls.clear()

                    if edit_menu == '+' and page < len(pagination):

                        page += 1

                    elif edit_menu == '-' and page > 1:

                        page -= 1

                    elif edit_menu.isdigit() and edit_menu != '0':

                        page = int(edit_menu) if int(edit_menu) <= len(pagination) else 1

                    else:

                        page = 1

                    pages: list = [str(num) for num in range(1, len(pagination) + 1)]

                    pages = [num for num in ''.join(pages).replace(str(page), f'|{page}|')]

                    for transaction in pagination[page]:

                        print(f'{transaction}\n')

                    print(' '.join(pages))
                    print(STRINGS.search_menu_pages)
                    edit_menu = input('Операция: ')

                cls.clear()
                return STRINGS.menu

            else:
                
                return f"{STRINGS.empty_trans}\n\n{STRINGS.back}"
            
        else:

            cls.clear()
            exit()
            

            



