#!/usr/bin/python

import sqlite3

odm_db = "odmsql"

conn = sqlite3.connect(odm_db)
cursor = conn.cursor()

content = None

with open("odm.txt") as odm_file:
    content = odm_file.readlines()

elts = 0

for idx, test_line in enumerate(content):
    test_line = test_line.decode('Windows-1250')
    test_line = test_line.replace('\r\n', '')

    words = test_line.split(', ')
    for word in words[1:]:
        cursor.execute("INSERT INTO odmiany (forma_slowa, slowo) VALUES (?, ?)", (word, words[0]))


    if idx % 100 == 0:
        print idx

        conn.commit()

    elts += len(words)

print elts
