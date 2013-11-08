import MySQL
import mysql.connector
from mysql.connector import errorcode
from mySQL import get_data, get _cnx
import sys, re
import config
# sourceTable is where we put all network queries, source is the attribute
# sketchySource is where we put naughty queries when they misbehave.   
global network_address = '10.20.30.40'
global flush, threshold = config.freqVars()


def analyzeTraffic(table):-
    cnx = get_cnx()
    data = get_data(cnx, "SELECT src FROM "+ table +" WHERE dst = "+ network_address)
    cursor = cnx.cursor()
    addDNS = ("INSERT INTO sourceTable "
                   "(source)"
                   "VALUES (%s)")
		cursor.execute(addDNS, data)
		cnx.commit()        
    cnx.close()

def analyzeQueries(table):
    cnx = get_cnx()
    data = get_data(cnx, "SELECT source FROM "+ table)
    cnx.close()
    if network_address == query_address:
    print 'match found!'

def flushsources():
    cnx = mysql.connector.connect(user='root', passwd='password', host = '127.0.0.1', database = 'dynama')
    cursor = cnx.cursor()
    
    flush = ("DELETE FROM sourceTable WHERE sqlID > 0")
    cursor.execute(flush)
    
