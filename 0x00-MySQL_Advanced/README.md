# MySQL advanced

Aim of this topic was to understand the following concepts:

* How to create tables with constraints
* How to optimize queries by adding indexes
* What is and how to implement stored procedures and functions in MySQL
* What is and how to implement views in MySQLWhat is and how to implement triggers in MySQL

## FILES

The following task files were used to test understanding on the various concepts:

[0-uniq_users.sql](./0-uniq_users.sql)

Script that creates a table users with follwing fields id, email, name

[1-country_users.sql](./1-country_users.sql)

Script that creates a table users following these requirements: id, email, name, country(enumeration of US, CO and TN)

[2-fans.sql](./2-fans.sql)

Script that ranks country origins of bands, ordered by the number of (non-unique) fans

[3-glam_rock.sql](./3-glam_rock.sql)

Script that lists all bands with Glam rock as their main style, ranked by their longevity

[4-store.sql](./4-store.sql)

Script that creates a trigger that decreases the quantity of an item after adding a new order.

[5-valid_email.sql](./5-valid_email.sql)

Script that creates a trigger that resets the attribute valid_email only when the email has been changed.

[6-bonus.sql](./6-bonus.sql)

Script that creates a stored procedure AddBonus that adds a new correction for a student.

[7-average_score.sql](./7-average_score.sql)

Script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

[8-index_my_names.sql](./8-index_my_names.sql)

Script that creates an index idx_name_first on the table names and the first letter of name.

[9-index_name_score.sql](./9-index_name_score.sql)

Script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

[10-div.sql](./10-div.sql)

Script that creates a function SafeDiv that divides (and returns) the first by the second number
or returns 0 if the second number is equal to 0.

[11-need_meeting.sql](./11-need_meeting.sql)

Script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
