#!/usr/bin/python
# -*- coding: utf-8 -*-

from sets import Set
from storm.locals import *
from corpus import *


# class Person(object):
#     __storm_table__ = "person"
#     CREATE_SQL = "CREATE TABLE " + __storm_table__ + "(id INTEGER PRIMARY KEY, name VARCHAR)"
#     id = Int(primary=True)
#     name = Unicode()
#
#
# class Company(object):
#     __storm_table__ = "company"
#     CREATE_SQL = "CREATE TABLE " + __storm_table__ + "(id INTEGER PRIMARY KEY, name VARCHAR)"
#     id = Int(primary=True)
#     name = Unicode()
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Employee(Person):
#     __storm_table__ = "employee"
#     CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
#         "(id INTEGER PRIMARY KEY, name VARCHAR, company_id INTEGER)"
#     company_id = Int()
#     company = Reference(company_id, Company.id)
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Accountantt(Person):
#     __storm_table__ = "accountant"
#     CREATE_SQL = "CREATE TABLE " + __storm_table__ + "(id INTEGER PRIMARY KEY, name VARCHAR)"
#
#     def __init__(self, name):
#         self.name = name
#
#
# class CompanyAccountant(object):
#     __storm_table__ = "company_accountant"
#     __storm_primary__ = "company_id", "accountant_id"
#     CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
#         "(company_id INTEGER, accountant_id INTEGER, PRIMARY KEY (company_id, accountant_id))"
#     company_id = Int()
#     accountant_id = Int()

database = create_database("sqlite:")
store = Store(database)

# store.execute(Company.CREATE_SQL)
# store.execute(Employee.CREATE_SQL)
# store.execute(Accountantt.CREATE_SQL)
# store.execute(CompanyAccountant.CREATE_SQL)
#
#
# circus = store.add(Company(u"Circus Inc."))
# store.flush()
#
# ben = store.add(Employee(u"Ben Bill"))
# ben.company = circus
# print "%r, %r" % (ben.company_id, ben.company.name)
#
# sweets = store.add(Company(u"Sweets Inc."))
# store.flush()
#
# ben.company_id = sweets.id
# print "%r, %r" % (ben.company_id, ben.company.name)
#
# store.commit()
#
# Company.employees = ReferenceSet(Company.id, Employee.company_id)
#
# print sweets.employees.count()
#
# mike = store.add(Employee(u"Mike Mayer"))
# sweets.employees.add(mike)
#
# for employee in sweets.employees:
#     print "%r, %r" % (employee.id, employee.name)
#
# store.commit()
#
# karl = Accountantt(u"Karl Kent")
# frank = Accountantt(u"Frank Fourt")
#
# Company.accountants = ReferenceSet(Company.id,
#                                    CompanyAccountant.company_id,
#                                    CompanyAccountant.accountant_id,
#                                    Accountantt.id)
#
# sweets.accountants.add(karl)
# sweets.accountants.add(frank)
# circus.accountants.add(frank)
#
# print sweets.accountants.count()
# print circus.accountants.count()
#
# Accountantt.companies = ReferenceSet(Accountantt.id,
#                                      CompanyAccountant.accountant_id,
#                                      CompanyAccountant.company_id,
#                                      Company.id)
#
# print [company.name for company in frank.companies]
# print [company.name for company in karl.companies]
#

MovieTitlesMetadata.genres = ReferenceSet(MovieTitlesMetadata.id,
                                          MovieGenreLine.movie_id,
                                          MovieGenreLine.genre_id,
                                          Genre.id)
Genre.movies = ReferenceSet(Genre.id,
                            MovieGenreLine.genre_id,
                            MovieGenreLine.movie_id,
                            MovieTitlesMetadata.id)

store.execute(MovieTitlesMetadata.CREATE_SQL)
store.execute(Genre.CREATE_SQL)
store.execute(MovieGenreLine.CREATE_SQL)


# m0 +++$+++ 10 things i hate about you +++$+++ 1999 +++$+++ 6.90 +++$+++ 62847 +++$+++ ['comedy', 'romance']
# m1 +++$+++ 1492: conquest of paradise +++$+++ 1992 +++$+++ 6.20 +++$+++ 10421 +++$+++ ['adventure', 'biography', 'drama', 'history']
# m2 +++$+++ 15 minutes +++$+++ 2001 +++$+++ 6.10 +++$+++ 25854 +++$+++
# ['action', 'crime', 'drama', 'thriller']

store.add(Genre("comedy"))
store.add(Genre("romance"))
store.add(Genre("adventure"))
store.add(Genre("biography"))
store.add(Genre("drama"))
store.add(Genre("history"))
store.add(Genre("action"))
store.add(Genre("crime"))
store.add(Genre("thriller"))
store.flush()


list = [0, "10 things i hate about you", 1999, 6.90, 62847, Set(["comedy"])]
list.pop()
movie0 = store.add(MovieTitlesMetadata(*list))

# movie0 = store.add(MovieTitlesMetadata(0,
#                                        u"10 things i hate about you",
#                                        1999,
#                                        6.90,
#                                        62847))
movie0.genres.add(store.find(Genre, Genre.name == "comedy".decode("utf-8")).one())
movie0.genres.add(store.find(Genre, Genre.name == u"romance").one())

movie1 = store.add(MovieTitlesMetadata(1,
                                       "1492: conquest of paradise",
                                       1992,
                                       6.20,
                                       10421))
movie1.genres.add(store.find(Genre, Genre.name == u"adventure").one())
movie1.genres.add(store.find(Genre, Genre.name == u"biography").one())
movie1.genres.add(store.find(Genre, Genre.name == u"drama").one())
movie1.genres.add(store.find(Genre, Genre.name == u"history").one())

movie2 = store.add(MovieTitlesMetadata(2,
                                       "15 minutes",
                                       2001,
                                       6.10,
                                       25854))
movie2.genres.add(store.find(Genre, Genre.name == u"action").one())
movie2.genres.add(store.find(Genre, Genre.name == u"crime").one())
movie2.genres.add(store.find(Genre, Genre.name == u"drama").one())
movie2.genres.add(store.find(Genre, Genre.name == u"thriller").one())

store.commit()

print movie0.title
print [genre.name for genre in movie0.genres]

drama = store.find(Genre, Genre.name == u"drama").one()
print drama.name
print [movie.title for movie in drama.movies]
