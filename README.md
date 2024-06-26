# Effective Mobile Test Task


[![Python 3.8](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/release/python-380/)
[![GitHub](https://img.shields.io/badge/Tutter-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/geekceo/Tutter)
##### При разрабротке была использована самописная библиотека для работы с моделями данных - Tutter
#
#
#
### Главное меню

##### При запуске программы вы увидите тектовое меню и приглашение для ввода одного из пунктов меню
#
#
![SNIMOK-EKRANA-2024-05-07-V-00.09.42.png](https://ltdfoto.ru/images/2024/05/07/SNIMOK-EKRANA-2024-05-07-V-00.09.42.png)

### Вывод баланса

##### Если файл с записями о "транзацкиях" пуст, то мы получим нулевые балансы и соответствующее сообщение
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.09.47.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.09.47.png)
#
##### В противном случае, если записи имеются, то мы получим расчет трех балансов - общий, доходы и расходы
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.12.30.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.12.30.png)

### Добавить запись

##### При добавлении новой записи от вас потребуется ввод таких данных, как категория, сумма и описание. Дата записи будет сформирована автоматически
#
##### При возникновении ошибок во время заполнения полей записи, приложение будет вас информировать и приглашать сделать новый ввод
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.32.32.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.32.32.png)
#
##### После успешной записи приложение нас об этом проинформирует
#
#
### Редактирование записи

##### При выборе пункта о редактировании записи, в случае, если записей нет, нас встретит соответствующее сообщение
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.35.03.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.35.03.png)
#
#
##### В противном случае мы увидим постраничный вывод всех записей, по 2 на каждой странице и удобную систему пагинации, как с последовательным переключением по страницам символами '+' и '-', так и просто вводом необходимой страницы
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.37.00.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.37.00.png)

##### Под записями можно увидеть систему отслеживания выбранной страницы и общий список доступных страниц. Введя в поле "Операция" символ плюса мы попадаем на следующую страницу, символ минуса - на предыдущую соответственно. При поппытке переключиться на следующую страницу, находясь на последней, приложение просто вернет нас на первую
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.39.13.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.39.13.png)
#
#
##### Так же можно попасть на конкретную страницу, если ввести ее номер. В случае ввода номера, которого не существует в списке доступных страниц, приложение так же вернет нас на первую страницу с записями 
#
#
##### Возможность редактирования существующей записи открывается при вводе команды R[1 ... N], где [1 ... N] - это один из ID записей, доступных из списка выше. При вводе несуществующего ID ничего не произойдет
#
#
##### Отредактируем добавленную нами запись о продаже подушек, она имеет ID - 9 и находится на пятой странице. Введем в поле "Операция" команду R9
#
#
##### Нас встретит поле ввода каждого, доступного для ввола критерия записи, мы можем либо оставить критерий, как есть (Нажав Enter), либо поменять его введя новое значение. Так же присутствует система защиты от ошибок, которая нас предупредит
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.48.51.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.48.51.png)
##### В данном случае мы оставили категорию, как есть, отредактировали сумму и описание. После редактирвоания нас вернуло на экран с только что отредактированной нами записью
#
#
### Поиск по записи
##### При выборе данного пункта меню нас переведет на экран с приглшанием для ввода критерия поиска - это может быть дата, сумма или категория. Можете ввести, что угодно из этого, приложение само определит по какому критерию вы хотите искать и выдаст вам нужную информацию с той же системой постраничной навигации
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.53.20.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.53.20.png)
#
#
##### В данном случае мы осуществляем поиск по дате и вот, что нам выдало приложение
#
#
![SNIMOK-EKRANA-2024-05-05-V-12.54.35.png](https://ltdfoto.ru/images/2024/05/05/SNIMOK-EKRANA-2024-05-05-V-12.54.35.png)


#
#
##### Для выхода в главном меню напишите '5' и нажмите Enter
