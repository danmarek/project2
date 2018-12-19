# Project Name: News Website Statistics
This project sets up a **PostgreSQL** database for news website and creates a command line reporting tool built to report the most popular articles and authors for a news online website. It will also provide health metrics from the webserver logs.  

The **loganalysis.py** uses **psycopg2** library to query the database and will create a text report answering the following questions.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Prerequisites 
Install the nano degree full stack vagrant virtual machine which includes python 2.7 and PostgreSQL
### Install Git
If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads)
### Install Virtual Box
Install [Virtual Box from here](https://www.virtualbox.org/wiki/Downloads), the extension pack and SDK are not required
### Install Vagrant
Download and install the correct vagrant version for your operating system from [vagrantup](https://www.vagrantup.com/downloads.html)
### Download Vagrant VM Configuration
Within GitHub fork and clone the [fullstack repository]:(https://github.com/udacity/fullstack-nanodegree-vm)
### Starting VM
run the commands to start vm
```sh
cd vagrant
vagrant up
vagrant ssh
```
### Database import
The news database content zip file can be downloaded from [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
Unzip the file and run `psql -d news -f newsdata.sql` to import the data into the news database

# Run Command
`python loganalysis.py`

# View Created
A view was created for this project.
run `psql -d news -f create_view.sql` command to create the view.

# Database
-	The log table contains a database row for each time a user accesses a web page
-	The log table contains a status column storing the HTTP status code return from the news web server to the users browser (HTTP Status 200 and 404) 
-	The authors table contains a database row for each author with a name column allowing full name text string and bio column for a bio description.
-	The articles table contains a row for each article available on the web site. 
-	The articles table contains a column for the author id, title, slug text string used in the web page url, lead and body containing the full article text.

# Author
Cheers
Dan Marek
