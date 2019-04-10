#!/usr/bin/env python3

import psycopg2
from psycopg2 import Error


def print_answers():
    print("The most popular 3 articles of all time:")
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute("select path, count(path) as c, slug, title from log "
                  "join articles on path = '/article/' || articles.slug "
                  "where status = '200 OK' and path like '/article/%' "
                  "group by slug, path, title "
                  "order by c DESC limit 3;")
        results = c.fetchall()
        title = 3
        number = 1
        for article in results:
            print '{article} -- {count} views'\
                .format(article=article[title],
                        count=article[number])
        print("")
        print("The most popular authors of all time:")
        c.execute("select count(l.path) c, au.name from articles a "
                  "join log l on l.path = '/article/' || a.slug "
                  "join authors au on a.author = au.id "
                  "where l.status = '200 OK' and l.path like '/article/%' "
                  "group by au.name order by c DESC;")
        results = c.fetchall()
        for author in results:
            print '{author} -- {views} views'\
                .format(author=author[1],
                        views=author[0])
        print("")
        print("Days had more than 1% of requests lead to errors:")
        c.execute("select time::date as dates, "
                  "(count(status) filter "
                  "(where status = '404 NOT FOUND'))/"
                  "(count(*)::float)*100 as p "
                  "from log group by dates "
                  "having (count(status) "
                  "filter (where status = '404 NOT FOUND'))/"
                  "(count(*)::float)*100 > 1;")
        results = c.fetchall()
        for date in results:
            print '{results} -- {error}  % errors'\
                .format(results=results[0][0],
                        error=round(results[0][1], 2))
        db.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def main():
    print_answers()


main()
