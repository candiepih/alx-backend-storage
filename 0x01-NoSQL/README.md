# NoSQL

This topics aim was to learn how to use NoSQL databases.
These are the areas I learned:

* What `NoSQL` means 
* What is difference between SQL and NoSQL 
* What is `ACID`
* What is a `document storage `
* What are NoSQL types 
* What are benefits of a NoSQL database 
* How to `query` information from a NoSQL database 
* How to `insert/update/delete` information from a NoSQL database 
* How to use `MongoDB`

## Files

The following task files were used to understand the various concepts:

[0-list_databases](./0-list_databases)

Script that lists all databases in MongoDB.

[1-use_or_create_database](./1-use_or_create_database)

Script that creates or uses the database `my_db`

[2-insert](./2-insert)

Script that inserts a document in the collection `school`

[3-all](./3-all)

Script that lists all documents in the collection `school`

[4-match](./4-match)

Script that lists all documents with `name="Holberton school"` in the collection `school`

[5-count](./5-count)

Script that displays the number of documents in the collection `school`

[6-update](./6-update)

Script that adds a new attribute to a document in the collection `school`

[7-delete](./7-delete)

Script that deletes all documents with `name="Holberton school"` in the collection `school`

[8-all.py](./8-all.py)

Contains function that lists all documents in a collection

[9-insert_school.py](./9-insert_school.py)

Contains a function that inserts a new document in a collection based on kwargs

[10-update_topics.py](./10-update_topics.py)

Contains a function that changes all topics of a school document based on the name

[11-schools_by_topic.py](./11-schools_by_topic.py)

Contains a function that returns the list of school
having a specific topic

[12-log_stats.py](./12-log_stats.py)

Contains function that provides some stats about
Nginx logs stored in MongoDB

[100-find](./100-find)

Script that lists all documents with name starting by Holberton in the collection school

[101-students.py](./101-students.py)

Contains a function that returns all students sorted
by average score

[102-log_stats.py](./102-log_stats.py)

Contains function that provides some stats and more
resent IPS about Nginx logs stored in MongoDB