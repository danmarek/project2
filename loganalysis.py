#!/usr/bin/env python
#
# Udacity Log Analysis Project

import datetime
import psycopg2

DBNAME = 'news'

# program will print analysis report
# 1. What are the most popular three articles of all time?
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('''select slugdetails.title, count(*) as num_views from log,
    slugdetails where log.path = slugdetails.slug_path
    group by slugdetails.title order by num_views desc limit 3''')
popular_articles = c.fetchall()
db.close()
print('\n\nWhat are the most popular three articles of all time?\n')
for article in popular_articles:
    print("Title \"%s\" Viewed %d" % (article[0], article[1]))

# 2. Who are the most popular article authors of all time?
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('''select slugdetails.name, count(*) as num_views from log,
    slugdetails where log.path = slugdetails.slug_path
    group by slugdetails.name order by num_views desc''')
popular_arthors = c.fetchall()
db.close()
print('\n\nWho are the most popular article authors of all time?\n')
for arthor in popular_arthors:
    print("%s -- %d views" % (arthor[0], arthor[1]))

# 3. On which days did more than 1% of requests lead to errors?
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('''select to_char(totalCount.day,'FMMonth dd, yyyy') as day,
    round(errorCount.errors/totalCount.total::decimal * 100,2) as percent,
    totalCount.total, errorCount.errors
    from (select time::date as day, count(*) as total from log group by day)
    as totalCount join (select time::date as day, count(*) as errors from log
    where status != '200 OK' group by day) as errorCount
    on totalCount.day = errorCount.day where
    (errorCount.errors/totalCount.total::decimal * 100) > 1''')
errors = c.fetchall()
db.close()
print("\n\nOn which days did more than 1% of requests lead to errors?\n")
for error in errors:
    print("%s -- %s%% errors" % (error[0], error[1]))

print('\n')
