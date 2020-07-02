import csv

file = open ('111 Books.csv','a')
title = input('Enter title: ')
author = input('Enter author: ')
date = input('Enter date: ')
newRecord = tile + ',' + author + ',' + date + '\n'
file.write(str(newRecord))
file.close()
