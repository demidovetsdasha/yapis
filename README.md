# СПЕЦИФИКАЦИЯ РАЗРАБОТАННОГО ЯЗЫКА


### Язык для работы с реляционными данными
Встроенные типы: table, row, column
Встроенные функции задания структур, изменения данных, поиска


### Свойства языка по варианту:
Объявление переменных – не явное
Преобразование типов – не явное
Оператор присваивания – многоцелевой, например, a, b = c, d
Структуры, ограничивающие область видимости – подпрограммы
Маркер блочного оператора – не явный, например как в python
Условные операторы – двухвариантный оператор и многовариантный switch-case
Перегрузка подпрограмм – присутствует
Передача параметров в подпрограмму – только по значению и возвращаемому значению
Допустимое место объявления подпрограмм – в любом месте программы, также и внутри другой подпрограммы.

Целевой код – LLVM IR, формат промежуточного кода для LLVM (http://llvm.org) 

### Дополнительное задание
Реализована возможность использования формул с помощью динамически вычисляемых столбцов, значение которых задаётся выражением при объявлении таблицы и автоматически вычисляется при вставке/обновлении/чтении строк этой таблицы. Данное расширение потребовало модификации основных файлов для компиляции: грамматики, семантического анализатора, генерации кода и т.д.

Для поддержки реактивных столбцов была расширена грамматика языка. В частности, изменено правило описания столбцов таблицы. Теперь язык поддерживает два вида объявлений столбцов:
+ обычные столбцы с указанием имени, типа и необязочного инициализирующего выражения;
+ реактивные столбцы, значение которых вычисляется с помощью исполняемого блока операторов.
Дополнительно были добавлены необходимые лексемы и уточнения правил, обеспечивающие корректное распознавание новых конструкций на этапе лексического и синтаксического анализа.

Семантический анализатор был расширен для обработки новых ошибок, связанных с реактивными столбцами. В частности, на этом этапе выполняется проверка корректности выражения, присваемого столбцу.

Кодогенератор был доработан для поддержки создания таблиц с вычисляемыми столбцами. В процессе генерации LLVM IR формируются дополнительные структуры, позволяющие хранить вычисляемые выражения столбцов и использовать их во время выполнения программы. При создании таблицы кодогенератор различает обычные и реактивные столбцы и формирует соответствующие описания для каждого из них.

Для обеспечения корректной работы вычисляемых столбцов была обновлена библиотека времени выполнения (runtime). При создании нового столбца таблицы сначала парсится выражение, присваемое столбцу, а далее сохраняется, при добавлении новых элементов в таблицу значения в реактивных столбцах инициализируются в соответствии заданному выражению, при обновлении элементов значения пересчитываются. 


### Демонстрация работы дополнительного задания:

Пример кода:

```
create transactions with (
    id: int,
    amount: float,
    tax: float = amount * 0.2,
    total: float = amount + tax
)

insert to transactions:
    id, amount = 1, 150.0
    id, amount = 2, 80.0

write transactions
```



Вывод при вызове исполняемого файла example-dop.exe

```
Table 'transactions' created with 4 columns

Table: transactions (2 rows, 4 columns)
  Column 'tax' is reactive: amount * 0.2
  Column 'total' is reactive: amount + tax
+----+--------+-------+--------+
| id | amount | tax   | total  |
+----+--------+-------+--------+
| 1  | 150.00 | 30.00 | 180.00 |
| 2  | 80.00  | 16.00 | 96.00  |
+----+--------+-------+--------+
```

Демонстрация работы прочих примеров кода:

1. Пример кода:

```
create users_table with (
    id: int,
    name: string,
    age: int,
    city: string
)

create orders_table with (
    id: int,
    user_id: int,
    amount: float,
    created: date
)

insert to users_table:
    id, name, age, city = 1, "Anna", 28, "Oslo"
    id, name, age, city = 2, "Ola", 35, "Bergen"
write users_table

select id from users_table as user_ids
write user_ids

insert to orders_table where user_id from user_ids:
    id, user_id, amount, created = 100, user_id, 4.95, "2025-09-01"
    id, user_id, amount, created = 101, user_id, 19.99, "2025-09-03"

join users_table with orders_table by id and user_id as joined
filter joined by amount > 10 and name[0] == 'A' as big_orders
sort <desc> big_orders by amount as sorted
write sorted
```

Вывод при вызове исполняемого файла example1.exe

```
Table 'users_table' created with 4 columns
Table 'orders_table' created with 4 columns

Table: users_table (2 rows, 4 columns)
+----+------+-----+--------+
| id | name | age | city   |
+----+------+-----+--------+
| 1  | Anna | 28  | Oslo   |
| 2  | Ola  | 35  | Bergen |
+----+------+-----+--------+

Table 'users_table_select' created with 1 columns
Inserted 1 row into table 'users_table_select'
Inserted 1 row into table 'users_table_select'

Table: users_table_select (2 rows, 1 columns)
+----+
| id |
+----+
| 1  |
| 2  |
+----+

Join condition: 'users_table.id=orders_table.user_id'
Left table: 'users_table', Right table: 'orders_table'
Table 'users_table_join_orders_table' created with 8 columns
Inserted 1 row into table 'users_table_join_orders_table'
Inserted 1 row into table 'users_table_join_orders_table'
Table 'users_table_join_orders_table_filtered' created with 8 columns
Table 'users_table_join_orders_table_filtered_sorted' created with 8 columns

Table: users_table_join_orders_table_filtered_sorted (0 rows, 8 columns)
(empty table)
```

2. Пример кода:
```
create numbers with (n: int)
for i in 1..5:
    insert to numbers:
        n = i
write numbers

x = true
switch x:
    case is true:
        write "true"
    default:
        write "false"

select n from numbers as selected
for x in selected:
    if x % 2 == 0:
        write "even:"
        write x
    else:
        write "odd:"
        write x

counter = 3
while counter > 0:
    write counter
    counter = counter - 1
write " "

x = 0.1
y = 4
z = x + y
write z
```

Вывод при вызове исполняемого файла example2.exe

```
Table 'numbers' created with 1 columns
Table: numbers (5 rows, 1 columns)
+---+
| n |
+---+
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
+---+

true
Table 'numbers_select' created with 1 columns
Inserted 1 row into table 'numbers_select'
Inserted 1 row into table 'numbers_select'
Inserted 1 row into table 'numbers_select'
Inserted 1 row into table 'numbers_select'
Inserted 1 row into table 'numbers_select'
odd:
1
even:
2
odd:
3
even:
4
odd:
5

3
2
1

4.100000
```

3. Пример кода:
```
function test_primer(n: int):
    z = 3 * n
    return z

function is_prime(x: int):
    if x <= 1:
        return false

    function has_divisor(y: int, d: int):
        if d * d > y:
            return false
        if y % d == 0:
            return true
        return has_divisor(y, d + 1)

    return not has_divisor(x, 2)

function is_prime(x: int, has_divisor: bool):
    return not has_divisor

write test_primer(5)
write is_prime(7)
write is_prime(9, true)
```

Вывод при вызове исполняемого файла example3.exe  

```
15
false
false
```
