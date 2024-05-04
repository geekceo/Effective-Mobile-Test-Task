from strings import Strings
from utils import Utils

STRINGS: Strings = Strings()


def main() -> None:

    menu = '0'

    while menu != '5':

        print(Utils.menu_handler(stage=menu))
        menu = input('Пункт: ')

    Utils.clear()
        


if __name__ == '__main__':

    main()