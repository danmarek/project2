# loganalysis.py Design
loganalysis.py is a script to analyze web site log files and create a report
the script will query the news database to answer questions about web 
application usage and error requests.

# Prerequisites 
Install the vagrant vm provided with the udacity full stack nanodegrees virtual machine installation instructions and load the newsdata.sql file to setup database records.

# Run Command
`python loganalysis.py`

# View Created
A view was created for this project using the following sql.
create view slugdetails as select title, '/article/' || slug as slug_path, name from articles, authors where articles.author = authors.id;

# Author
Cheers from Dan

