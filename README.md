# loganalysis.py
Command line reporting tool built to report the most popular articles and authors for a news online website. It will also provide health metrics from the webserver logs.  

# Design
The program is designed to run 3 queriers against the mysql database and will create a simple text report answering the following questions.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Prerequisites 
Install python 2.7, mysql, create a news database and load the records from the newsdata.sql file provided with the nano fullstack degree. 

# Run Command
Type `python loganalysis.py` at the command line to run the program.

# View Created
A view was created for this project using the following sql.
create view slugdetails as select title, '/article/' || slug as slug_path, name from articles, authors where articles.author = authors.id;

# Author
Dan Marek
