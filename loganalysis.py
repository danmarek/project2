#!/usr/bin/env python
#
# Udacity Log Analysis Project

import datetime
import psycopg2
import sys
import logging


def connect(database_name):
    """
      connect to PostgreSQL DB and return
      connection and cursor
    """
    try:
        db = psycopg2.connect('dbname={}'.format(database_name))
    except psycopg2.Error as e:
        print("Unable to connect to {}!".format(database_name))
        print(e)
        print(e.pgerror)
        print(e.pgcode)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        logging.info('Connected')
    cursor = db.cursor()
    return db, cursor


def question1():
    # 1. What are the most popular three articles of all time?
    query = """
    SELECT slugdetails.title,
        count(*) AS num_views
    FROM log,
        slugdetails
    WHERE log.path = slugdetails.slug_path
    GROUP BY slugdetails.title
    ORDER BY num_views DESC
    LIMIT 3
    """
    db, c = connect('news')
    c.execute(query)
    popular_articles = c.fetchall()
    db.close()
    print('What are the most popular three articles of all time?\n')
    for article in popular_articles:
        print("Title \"%s\" Viewed %d" % (article[0], article[1]))


def question2():
    # 2. Who are the most popular article authors of all time?
    query = """
    SELECT slugdetails.name,
        count(*) AS num_views
    FROM log,
        slugdetails
    WHERE log.path = slugdetails.slug_path
    GROUP BY slugdetails.name
    ORDER BY num_views DESC
    """
    db, c = connect('news')
    c.execute(query)
    popular_arthors = c.fetchall()
    db.close()
    print('Who are the most popular article authors of all time?\n')
    for arthor in popular_arthors:
        print("%s -- %d views" % (arthor[0], arthor[1]))


def question3():
    # 3. On which days did more than 1% of requests lead to errors?
    query = """
    SELECT to_char(totalCount.day, 'FMMonth dd, yyyy') AS DAY,
        round(errorCount.errors/totalCount.total::decimal * 100, 2) AS percent,
        totalCount.total,
        errorCount.errors
    FROM
    (SELECT TIME::date AS DAY,
            count(*) AS total
    FROM log
    GROUP BY DAY) AS totalCount
    JOIN
    (SELECT TIME::date AS DAY,
            count(*) AS errors
    FROM log
    WHERE status != '200 OK'
    GROUP BY DAY) AS errorCount ON totalCount.day = errorCount.day
    WHERE (errorCount.errors/totalCount.total::decimal * 100) > 1
    """
    db, c = connect('news')
    c.execute(query)
    errors = c.fetchall()
    db.close()
    print("On which days did more than 1% of requests lead to errors?\n")
    for error in errors:
        print("%s -- %s%% errors" % (error[0], error[1]))


def run():
    print('Report Is Running\n')
    question1()
    print('\n')
    question2()
    print('\n')
    question3()
    print('\n')


if __name__ == '__main__':
    run()
else:
    print('Program did not run.')
