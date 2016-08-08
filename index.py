#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from os import environ
import cgitb;cgitb.enable(1,'/home/kyau/public_html/kyau_net/bbs/_pylog',5,'html')
import cgi
import config
import html


def main():
    maintenance = 0
    helpmsg = 0
    if maintenance:
        print('Location: /_blank.py\r\n\r')
    #if not environ.has_key('QUERY_STRING'):
    if environ['QUERY_STRING'] == '':
        query = 'main'
    else:
        query = environ['QUERY_STRING']
    html.header(str(query))
    if query == 'main':
        html.main_v2()
        helpmsg = 1
    elif query == 'enter':
        html.enter_v2()
    elif query == 'flash':
        html.flash_v2()
    elif query == 'about':
        html.about_v2()
    elif query == 'gossip':
        html.gos_v2()
    elif query == 'who':
        html.who_v2()
    elif query == 'top':
        html.top_v2()
    elif query == 'topgang':
        html.topg_v2()
    elif query == 'rules':
        html.rules_v2()
    elif query == 'realm':
        html.realm_v2()
    elif query == 'notes':
        html.notes_v2()
    elif query == 'files':
        html.files_v2()
    elif query == 'megamud':
        html.filesection('mega', 'MegaMud')
    elif query == 'majormud':
        html.filesection('mmud', 'MajorMUD')
    elif query == 'wgserv':
        html.filesection('wgserv', 'Worldgroup')
    elif query == 'aftermud':
        print('<pre>')
        with open('AFTERMUD.REL', 'r') as file:
            print(file.read())
        print('</pre>')
    else:
        html.error(404)
    html.footer(helpmsg)
    return 0


if __name__ == '__main__':
    main()
