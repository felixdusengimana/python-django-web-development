# SQL vs NoSQL

SQL: stores data in tabular form
NoSQL: stores value in key/value format

### Which is better?

None is better than another. but for django models it works well with tabular db.
You shouldn't choose a db base on that is sound cool but on what you're doing.

# SQL engines

1. MySQL
2. SQLite
3. PostgressSQL
4. MS SQL
5. ....

SQLite is already included with python.

# Models and Database Table

Models are converted into database table.

### creating new data(insertion)

- Inserting new data in table we create instanse of object and call `.save` method or use 
build in method `.objects.creat()` which create and push data into database with a single line.

- When you want to create mutlipe instance of data use `.objects.bulk_create()`

### Reading and querrying database

- We use `.all()` or `.get()` method call. we can also use `.filter()` or `.exclude()` thse last two doesn't explicitly call the database
without `.all()` or `.get()`

- `.all()` to get everything from a table
- `.get()` allows to grab single item from the table
- `.filter()` get data based on condition. They can also be chained together
- `.exclude()`

