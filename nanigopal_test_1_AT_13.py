
'''Python Section
--------------
1. What is decorator , write a decorator?

ans: Decorator is a function that modify a another function  without modify the previous code.
ex:
def decorator_add(func):
    def mul(a,b):
        return func(a,b),a*b
    return mul
@decorator_add
def sum(a,b):
    return a+b

print(sum(10,20))

2. What is lambda expression, write a lambda expression?

ans: Lambda expression is a small function that can be defined inline within a larger expression.

ex: for addition

sum = lambda x, y: x + y
print(sum(3, 4))

3. WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
repetitive character , without using any inbuilt function.
ans:
S = 'Hello everyone'

char_count = {}
repetitive_chars = []

for i in S:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print("Character counts:", char_count)

for j, k in char_count.items():
    if k > 1:
        repetitive_chars.append((j,k))
print("Repetitive characters:", repetitive_chars)
'''
 4. WAF , Reverse a string words. > Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function
5. WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’

6. Sort a list integer element without using inbuilt function?

7. Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}
Take a two list a parameter, return dictionary, look like above result.

8. Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
the csv and print in console bar

9. What is exception handling , how handel the exception in python , explain with each
block


'''10. Difference between Moudle and Packages (3 diff)
ans:
Module: 1.A single file containing Python code with a .py extension.
2.To use a module, we use the import statement
3.example, math.py is a module.

Package: 1.A directory that contains multiple modules.
2.To use a module we use from package name import madule name .
3.For example, a directory my_package with files module1.py and module2.py inside it.
'''

'''11. Difference between List vs tuple vs set vs dictionary?
ans:
 List
1.list is an collection of items.
2.list enclosed with[]
3.We can change, add, or remove items in list.
4.List Allows Duplicates
5.ex:my_list = [1, 2, 3, 3]

Tuple
1.Tuple is an ordered collection of items, similar to a list but immutable.
2.it enclosed with( )
3.Once created, we cannot change, add, or remove items.
4.it Allows Duplicates
5.ex:my_tuple = (1, 2, 3, 3)

Set
1.it is an unordered collection of unique items.
2.enclosed with {}
3.we can add or remove items, but we cannot have duplicates.
4.Each item must be unique.
5.ex:my_set = {1, 2, 3,}

Dictionary
1.it is a collection of key-value pairs.
2.Syntax: {key1: value1, key2: value2}
3.we can change, add, or remove key-value pairs.
4.Keys Must Be Unique, but values can be duplicated.
5.Ex:my_dict = {'a': 1, 'b': 2}
'''


'''12. What is Garbage Collection?
ans:
Garbage collection means grabage the data or memory that are no
longer in use.
ex:
we declear a variable A = 10 in fast and next second time we declear a same variable A=20,
then, python automatically remove 1st data from memory.'''


'''13. What is list comprehension , write code in list comprehension?
ans:
List comprehension  is a  way to create lists by specifying their elements in a single line of code.
ex:
num = [0, 1, 2, 3, 4]
doubled_numbers = [x * 2 for i in num]
print(doubled_numbers)'''


14. Difference between Shallow copy vs Deep Copy?



'''15. Explain break, continue, pass with code?
ans:
break: Exits the loop immediately.
continue: Skips the current iteration and moves to the next one.
pass: when a statement is required, but we do not want to execute any code.
examples:
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when number is 3
    print(i)

for j in range(1, 6):
    if j == 3:
        continue  # Skip the rest of the loop body when number is 3
    print(j)

for k in range(1, 6):
    if k == 3:
        pass  # Do nothing and move to the next iteration
    else:
        print(k)
'''


'''SQL
----

1. Explain about the DML,DDL,TCL,DQL commands?
ans:
1.DML-Data Manipulation Language
it Used to manipulate and manage data within the database.
Commands are:
SELECT: Retrieves data from a database.
INSERT: Adds new rows to a table.
UPDATE: Modifies existing rows in a table.
DELETE: Removes rows from a table.

2.DDL - Data Definition Language
it Used to define and modify the structure of database objects.
Commands are:
CREATE: Creates new tables, databases.
ALTER: Modifies existing database objects, such as adding a new column to a table.
DROP: Deletes tables, databases etc.
TRUNCATE: Removes all rows from a table but keeps the table structure.

3.TCL (Transaction Control Language)
use to manages transactions in the database.
Commands:
COMMIT: Saves all changes made during the current transaction.
ROLLBACK: Undoes changes made during the current transaction.
SAVEPOINT: Sets a point within a transaction to which we can later roll back.
SET TRANSACTION: Configures the properties of the transaction.

4.DQL (Data Query Language)
Purpose: Used to query and retrieve data from a database.
Commands:
SELECT: Retrieves data from one or more tables.
'''


'''2. What is join, explain about the all joins?
ans:
a join is a technique used to combine rows 
from two or more tables based on a related column between them.

1.INNER JOIN: Matches rows from both tables.
2.LEFT JOIN: Includes all rows from the left table and matched rows from the right table.
3.RIGHT JOIN: Includes all rows from the right table and matched rows from the left table.
4.FULL JOIN: Includes all rows from both tables, matching where possible.
5.CROSS JOIN: Produces a Cartesian product of both tables.'''


'''3. Difference between Joins vs Subquery?
ans:
Joins: Combine data from multiple tables based on related columns.
joins are INNER,LEFT,RIGHT,FULL,CROSS

Subqueries: A query within a query that performs additional filtering
or also called inner query.
Subqueries are Single-row Subquery,Multi-row Subquery'''


'''4. Find 3rd Highest Salary Of employee table ?
ans:
SELECT DISTINCT salary
FROM employee table
ORDER BY salary DESC
LIMIT 1 OFFSET 2'''


'''5. Find the top seller in this month, according to date in customer table?
ans:
SELECT seller_id
FROM customer
WHERE sale_date BETWEEN '2024-08-01' AND '2024-08-25'
GROUP BY seller_id
ORDER BY SUM(sales_amount) DESC
LIMIT 1;'''

6. Difference between Rank vs Dense_rank


'''Unix
-----
1. Copy a file one directory to another directory?
ans: using cp command 
cp copy_filename  destination_directory
'''
2. How do you find the process IF(PID) of a running process.

'''3. difference between chown vs chmod?
ans:
chown: Changes the owner and/or group of a file or directory.

chmod: Changes the permissions (read, write, execute) 
for a file or directory.'''

'''4. In a directory a find a file name abc.txt?
ans:
find [directory] -name "abc.txt"
'''
'''5. Why we are using sed command?
ans:
sed use for :
1.Substitute Text
2.Delete Lines
3.Print Lines
4.Insert/Apppend Text

6. How to list directories in Unix?
ans:
using ls command'''