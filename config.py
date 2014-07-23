#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import ConfigParser
import MySQLdb
from commands import getoutput
from datetime import datetime, timedelta, tzinfo

config_file = '/home/kyau/public_html/mysql.cfg'
db = None
mysql = {}
sql = None
stats = ['', '']

def main():
    return 0

def populate():
    """ populate list with configuration information """
    global mysql
    cfg = ConfigParser.RawConfigParser(allow_no_value=True)
    cfg.read(config_file)
    mysql['host'] = cfg.get('MYSQL', 'host')
    mysql['port'] = int(cfg.get('MYSQL', 'port'))
    mysql['user'] = cfg.get('MYSQL', 'user')
    mysql['passwd'] = cfg.get('MYSQL', 'passwd')
    mysql['db'] = cfg.get('MYSQL', 'bbsdb')
    return 0

def sql_connect():
    """ mysql database connectivity """
    try:
        db = MySQLdb.connect(host=mysql['host'], user=mysql['user'], \
                             passwd=mysql['passwd'], port=mysql['port'], \
                             db=mysql['db'])
    except MySQLdb.OperationalError:
        exit(1)
    return db

def sql_cmd(sql_string, ret = 0):
    """
    sql command
    0:commit() 1: fetchone(), 2:fetchall()
    """
    global db, sql
    data = None
    count = None
    try:
        count = sql.execute(sql_string)
        if ret == 1:
            data = sql.fetchone()
        elif ret == 2:
            data = sql.fetchall()
        else:
            db.commit()
    except:
        db.rollback()
    if ret > 0:
        return data
    else:
        return count

def tstruct(timestamp):
    """ create time struct from mysql dates """
    time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    dt = timedelta(minutes=3*60)
    time-=dt
    return time

def sys_stat():
    """ report back shell system stats """
    global stats
    stats[0] = getoutput('uptime')
    stats[1] = getoutput('uname -sr')
    return stats

def git_version():
    """ report back the git commit code """
    global git
    git = getoutput('git rev-parse --short HEAD')
    return git


if __name__ == '__main__':
    main()
