#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from __future__ import division
from cgi import escape
from os import stat
from random import randrange
from sys import version
from time import localtime, strftime
import config as cfg
import math

mod = strftime('%b %d %Y %H:%M:%S', localtime(stat(__file__).st_mtime))
webver = '2.1'


def main():
    return 0

def header(menu):
    """default html header"""
    ver=version.split('\n')
    quote=['attacking the shadow healer since \'94.',
          'coming to a general store near you.',
          'now running 2400 baud !!']
    rand=randrange(0, len(quote), 1)
    print 'Content-type: text/html\n'
    print
    print '''<!DOCTYPE html>
<html lang="en">\n
\t<head>
\t\t<meta charset="utf-8" />
\t\t<title>VOID:  %s</title>
\t\t<link rel="icon" href="/favicon.ico" type="image/x-icon" />
\t\t<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
\t\t<link rel="stylesheet" href="/css/style.css" type="text/css" media="screen, projection" />
\t\t<meta name="author" content="Sean Bruen" />
\t\t<meta name="description" content="VOID is running on Worldgroup v3.30-NT with MajorMUD v1.11p!" />
\t\t<meta name="generator" content="Python %s" />
\t\t<meta name="keywords" content="void, majormud, mmud, mud, bbs, worldgroup, tlord, t-lord, Sean Bruen, aftermud, amud" />''' % (quote[rand], ver[0].strip())
    print '\t\t<script src="//code.jquery.com/jquery-1.10.2.min.js"></script>'
    if menu == 'main':
        print '\t\t<script src="/js/main.js" charset="utf-8"></script>'
    else:
        print '\t\t<script src="/js/other.js" charset="utf-8"></script>'
    print '''\t</head>\n
<body>\n
\t<div id="statusbar"><a href="https://github.com/kyau/bbs-kyau_net"><img alt="Github" src="/img/github.png" /> %s</a></div>
\t<div id="term">''' % cfg.git_version()
    return 0

def footer(warning):
    """ default html footer """
    print '\t</div>'
    if warning:
        print '\t<div id="msg" style="font-weight:bold">Press <span class="darkcyan">?</span> for help.</div>'
    else:
        print '\t<div id="msg">This *IS* an actual terminal window.</div>'
    print '''\t<div id="help"><img alt="Help!" src="/img/help.png" /></div>
\n</body>\n
</html>\n'''
    return 0

def error(e):
    if e == 404:
        print '''\t\t<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> 404<br/>
\t\t<br/><br/><br/><br/>
\t\t<img alt="404" src="/img/404.ANS.png" style="margin-left:60px" />
\t\t<pre>                               <span class="darkcyan" style="font-weight:bold;">404</span><span class="white" style="font-weight:bold;">:</span> <span class="lightgrey">File Not Found</span></pre><br/><br/><br/><br/><br/><br/>
\t\t<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'''
        return 0
    else:
        return 0


def main_v2():
    """ main menu """
    print '\t\t<span class="white">V O I D</span> <span class="lightyellow">v%s-WEB (%s)</span><br/>' % (webver, mod)
    print '''\t\t<span class="lightgrey">{BBS of Legends}</span><br/>
\t\t<span class="lightmagenta">*ANSI RECOMMENDED*</span><br/><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?enter">E</a><span class="darkgrey">] .</span> <a class="menutext" href="/?enter">Enter the Realm</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="http://kyau.net/wiki/Category:MajorMUD">H</a><span class="darkgrey">] .</span> <a class="menutext" href="http://kyau.net/wiki/Category:MajorMUD">Wiki</a> <span class="darkcyan">*WIP*</span><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?about">A</a><span class="darkgrey">] .</span> <a class="menutext" href="/?about">About the BBS</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?cap">C</a><span class="darkgrey">] .</span> <a class="menutext" href="/?cap">Captures</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?files">D</a><span class="darkgrey">] .</span> <a class="menutext" href="/?files">Downloads</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?gossip">S</a><span class="darkgrey">] .</span> <a class="menutext" href="/?gossip">Gossip Chat</a> <span class="darkcyan">*NEW*</span><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?rules">R</a><span class="darkgrey">] .</span> <a class="menutext" href="/?rules">Realm Rules</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?top">T</a><span class="darkgrey">] .</span> <a class="menutext" href="/?top">Top Adventurers</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?topgang">G</a><span class="darkgrey">] .</span> <a class="menutext" href="/?topgang">Top Gangs</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?who">W</a><span class="darkgrey">] .</span> <a class="menutext" href="/?who">Who\'s in the Realm</a><br/><br/>

\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?realm">!</a><span class="darkgrey">] .</span> <a class="menutext" href="/?realm">Realm Settings</a><br/><br/>
\t\t<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>
\t\t<br/><br/><br/><br/><br/><br/><br/>&nbsp;'''
    return 0

def enter_v2():
    """ enter the realm """
    print '\t\t<span class="white">V O I D</span> <span class="lightyellow">v%s-WEB (%s)</span><br/>' % (webver, mod)
    print '''\t\t<span class="lightgrey">{BBS of Legends}</span><br/>
\t\t<span class="darkgreen">*Enter the Realm*</span><br/><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="telnet://bbs.majormud.org">T</a><span class="darkgrey">] .</span> <a class="menutext" href="telnet://bbs.majormud.org">Telnet</a><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/?flash">F</a><span class="darkgrey">] .</span> <a class="menutext" href="/?flash">Flash</a><br/><br/>
\t\t<span class="darkgrey">[</span><a class="menuitem" href="/">X</a><span class="darkgrey">] .</span> <a class="menutext" href="/">BBS Main Menu</a><br/><br/>
\t\t<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'''
    return 0

def flash_v2():
    """ enter the realm: flash """
    print '''\t<script type="text/javascript" src="swfobject.js"></script>
\t<script type="text/javascript">
\t\tvar flashvars = {};
\t\tvar params = {};
\t\tparams.menu = "false";
\t\tparams.bgcolor = "000000"
\t\tvar attributes = {};
\t\tswfobject.embedSWF("flashterm.swf", "flash", "650", "440", "9.0.115", "expressInstall.swf", flashvars, params, attributes);
\t\tfunction setFocusOnFlash() {
\t\t\tvar fl = document.getElementById("term");
\t\t\tfl.focus(); }
\t\tswfobject.addLoadEvent(setFocusOnFlash);
\t</script>
\t<div id="flash"></div>
\t<style><!-- #term {background:#131313;border:0px;padding:0;} --></style>'''
    return 0

def about_v2():
    """ about the bbs """
    stats = cfg.sys_stat()
    print '''<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> A<br/>\n<pre>\n
<span class="darkmagenta">   _________________________________________________________________________</span>\n
<span class="lightblue">                                   V O I D</span>\n
<span class="lightgrey">      VOID is running on Worldgroup v3.30-NT inside a WindowsXP Virtual
         Machine, the stats for the system the VM is running on are:</span>\n
<span class="darkmagenta">                  Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
                             %s
                            2 x 1TB HDD (RAID1)
                            100mbit from OVH.ca</span>\n
   <span class="darkgrey">%s</span>\n
<span class="lightgrey">        If you have any questions please direct them to the user Kyau
                using the Electronic Mail built into the BBS.</span>\n
<span class="darkmagenta">   _________________________________________________________________________</span>
</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>''' % (stats[1], stats[0])
    return 0

def gos_v2():
    """ gossip log """
    print '<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> S<br/><br/>'
    sqlstr = 'SELECT * FROM (SELECT * FROM gossip ORDER BY timestamp DESC LIMIT 20) AS ttbl ORDER BY ID ASC'
    tmp = cfg.sql_cmd(sqlstr, 2)
    if not tmp == None:
        for row in tmp:
            dt = cfg.tstruct(str(row[3]))
            tzone = ''
            if dt.hour > 12:
                timestamp = '0'+str(dt.hour-12)+':'
                tzone = 'p'
            else:
                timestamp = str(dt.hour)+':'
                tzone = 'a'
            if len(str(dt.minute)) < 2:
                timestamp += '0'+str(dt.minute)
            else:
                timestamp += str(dt.minute)
            timestamp += tzone
#            timestamp = strftime('%I:%M', timestamp)
            print '<div id="wrap"><span class="darkgrey">%s</span> <span class="lightgrey">%s gossips:</span> <span class="darkmagenta">%s</span></div>\n' % (timestamp, row[1], escape(row[2]))
    print '<br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'
    return 0

def who_v2():
    """ who's online """
    color = None
    exphr = None
    xphr = None
    kph = 0.0
    print '<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> W<br/>\n<pre>\n'
    sqlstr = 'SELECT count(*) FROM online'
    tmp = cfg.sql_cmd(sqlstr, 1)
    if tmp[0] > 0:
        print '<span class="lightyellow">         Current Adventurers</span>'
        print '<span class="darkgrey">         ===================</span>'
        sqlstr = 'SELECT user, busy FROM online'
        tmp = cfg.sql_cmd(sqlstr, 2)
        for row in tmp:
            sqlstr = 'SELECT alignment, title, exp, expold, gang FROM users WHERE user LIKE \''+row[0]+'%\''
            tmp = cfg.sql_cmd(sqlstr, 1)
            if tmp[0] == 'Criminal': color = 'darkyellow'
            elif tmp[0] == 'Villain': color = 'lightyellow'
            elif tmp[0] == 'Outlaw': color = 'darkred'
            elif tmp[0] == 'FIEND': color = 'lightred'
            else: color = 'white'
            if tmp[2] == tmp[3]:
                exphr = '<span class="idle">idle</span>'
            else:
                xphr = (tmp[2] - tmp[3]) * 12
                kph = xphr / 1000
                if round(kph, 0) > 10:
                    xphr = '%d' % kph
                else:
                    xphr = round(kph, 1)
                exphr = '<span class="xphr">%sk/hr</span>' % str(xphr)
            if tmp[4] == '':
                print '<span class="line"><span class="%s">%8s</span> <span class="darkgreen">%-20s %s</span>  <span class="darkmagenta">%s</span>%s</span>' % (color, tmp[0], row[0][:20], row[1], tmp[1], exphr)
            else:
                print '<span class="line"><span class="%s">%8s</span> <span class="darkgreen">%-20s %s</span>  <span class="darkmagenta">%s</span>  <span class="darkgreen">of</span> <span class="darkyellow">%s</span>%s</span>' % (color, tmp[0], row[0][:20], row[1], tmp[1], tmp[4], exphr)

    else:
        print '<span class="darkmagenta">There are no users in the game at the moment.</span>'
    print '</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'
    return 0

def top_v2():
    """ top 100 adventurers """
    rank = 1
    print '<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> T<br/>\n<pre>\n'
    sqlstr = 'SELECT count(*) FROM users'
    tmp = cfg.sql_cmd(sqlstr, 1)
    if tmp[0] > 0:
        print '<span class="darkyellow">Top Heroes of the Realm</span>'
        print '<span class="lightgrey">-=-=-=-=-=-=-=-=-=-=-=-</span>\n'
        print '<span class="darkred">Rank</span> <span class="darkgreen">Name</span>                  <span class="darkmagenta">Class</span>      <span class="darkyellow">Gang/Guild</span>          <span class="darkgreen">Experience</span>     <span class="darkgrey">k/hr</span>'
        print '<span class="darkgrey">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>'
        sqlstr = 'SELECT user, class, gang, exp, expold FROM users ORDER BY exp DESC'
        tmp = cfg.sql_cmd(sqlstr, 2)
        for row in tmp:
            if row[3] == row[4]:
                exphr = '<span style="color:#434343">   &#42;</span>'
            else:
                xphr = (row[3] - row[4]) * 12
                kph = xphr / 1000
                if round(kph, 0) > 10:
                    xphr = '%d' % kph
                else:
                    xphr = round(kph, 1)
                exphr = '<span class="darkgrey">%4s</span>' % str(xphr)
            print '<span class="line"><span class="darkred">%3d.</span> <span class="darkgreen">%-21s</span> <span class="darkmagenta">%-10s</span> <span class="darkyellow">%-19s</span> <span class="darkgreen">%-14d</span> %s</span>' % (rank, row[0][:21], row[1], row[2], row[3], exphr)
            rank = rank + 1
    else:
        print '<span class="darkmagenta">Realm recently reset.</span>'
    print '</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'
    return 0

def topg_v2():
    """ top 100 gangs """
    rank = 1
    print '<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> G<br/>\n<pre>\n'
    sqlstr = 'SELECT count(*) FROM gangs'
    tmp = cfg.sql_cmd(sqlstr, 1)
    if tmp[0] > 0:
        print '<span class="darkyellow">Top Gangs of the Realm</span>'
        print '<span class="lightgrey">-=-==-=-=-=-=-=-=-=-=-</span>\n'
        print '<span class="darkred">Rank</span> <span class="darkgreen">Gangname</span>            <span class="darkmagenta">Leader</span>      <span class="darkyellow">Members</span> <span class="darkgreen">Created</span>      <span class="darkyellow">Exp</span>            <span class="darkgrey">xp/hr</span>'
        print '<span class="darkgrey">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>'
        sqlstr = 'SELECT gang, leader, members, exp, expold, creation FROM gangs ORDER BY exp DESC'
        tmp = cfg.sql_cmd(sqlstr, 2)
        for row in tmp:
            if row[3] == row[4]:
                exphr = '<span style="color:#434343">     &#42;</span>'
            else:
                xphr = (row[3] - row[4]) * 12
                kph = xphr / 1000
                if round(kph, 0) > 10:
                    xphr = '%d' % kph
                else:
                    xphr = round(kph, 1)
                exphr = '<span class="darkgrey">%6s</span><span style="color:#434343">k</span>' % str(xphr)
#            print '%3s. %-19s %-11s %-7s %-12s %s' % (rank, name, leader, members, creation, exp)
            print '<span class="line"><span class="darkred">%3d.</span> <span class="darkgreen">%-19s</span> <span class="darkmagenta">%-11s</span> <span class="darkyellow">%-7d</span> <span class="darkgreen">%-12s</span> <span class="darkyellow">%-13d</span> %s</span>' % (rank, row[0][:19], row[1], row[2], row[5], row[3], exphr)
            rank = rank + 1
    else:
        print '<span class="darkmagenta">There are no gangs currently.</span>'
    print '</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'
    return 0

def rules_v2():
    print '<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> I<br/>\n<pre>\n'
    print '<img alt="Rules Header" src="/img/rules.png" border="0" />'
    print '<span class="darkgrey">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>'
    print '''
<span class="lightgrey">     -  You are allowed to create as many characters as you like,
        however you are limited to 2 characters logged in at once.

     -  PvP (Player vs. Player) is limited to +/-5, 1v1 and both toons
        must be at the keyboard (not scripting).
        *Multi-telnet PvP is not allowed*

     -  Characters that *can* backstab are allowed two limited weapons.
     -  Characters that *cannot* backstab are allowed one limited weapon.

        This means you may have a limited weapon for backstab and one
        for normal attacks, or just one for normal attacks if your toon
        cannot backstab.

     -  NO limited item hoarding of any kind.
        &#8226; All limited items *MUST* be equipped, not including backstab
          weapons.
        &#8226; Limited items may not be stored in gang houses.
        &#8226; Stashing or hiding items is allowed however doing so makes
          these items fair game and no gaurantees are made.
        &#8226; Limited items you cannot use or equip must be auctioned, or
          stashed/given away within 24 hours of obtaining.

     -  There is no AFK limit.

     -  Accounts that have 30 days or more of inactivity are *INACTIVE*.
     -  Limited items on inactive accounts will be reset.

     -  Class "SYSOP" are not playing accounts and are only active
        for troubleshooting and/or greivences (re-rolls, etc.).

     -  Class "ELITE" are considered MUDOPs, and as such are only given
        SYS GOTO, SYS MAP, SYS STATUS, SYS LIST, & SYS REPORT.
        (this class is mostly for playing Sysops)</span>'''
    print '</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'
    return 0

def realm_v2():
    print '''<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> !<br/>\n<pre>\n
<span class="white">MajorMUD Settings</span> <span class="lightmagenta">[<span class="darkmagenta">VOID</span>]</span>
<span class="darkgrey">-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>
<span class="lightgrey">Talk Char</span>                   <span class="lightcyan">- .</span>
<span class="lightgrey">Yell Char</span>                   <span class="lightcyan">- "</span>
<span class="lightgrey">Death HP</span>                    <span class="lightcyan">- -25</span>
<span class="lightgrey">Runic Name</span>                  <span class="lightcyan">- runic coins</span>
<span class="lightgrey">Gender Change Cost</span>          <span class="lightcyan">- 5,000</span> <span class="darkcyan">gold crowns</span>
<span class="lightgrey">Hangup Penalties</span>            <span class="lightcyan">-</span> <span class="white">None</span> <span class="darkcyan">(</span><span class="lightgrey">never punish</span><span class="darkcyan">)</span>
<span class="lightgrey">PVP Range</span>                   <span class="lightcyan">- +/- 5</span> <span class="darkcyan">levels</span>
<span class="lightgrey">Keep Exp on Reroll</span>          <span class="lightcyan">- Yes</span>
<span class="lightgrey">Max Stacked Levels</span>          <span class="lightcyan">- 10</span> <span class="darkcyan">levels</span>
<span class="lightgrey">Gang Exp for Gang House</span>     <span class="lightcyan">- 100,000,000</span> <span class="darkcyan">experience</span>
<span class="lightgrey">Evil Point Forgive Rate</span>     <span class="lightcyan">- 1</span> <span class="darkcyan">EP every</span> <span class="lightcyan">60</span> <span class="darkcyan">minutes (</span><span class="lightcyan">18</span> <span class="darkcyan">EP max/day)</span>
<span class="lightgrey">EP % Kept on Reroll</span>         <span class="lightcyan">- 50</span><span class="darkcyan">%</span>
<span class="lightgrey">Lawful Enabled</span>              <span class="lightcyan">- Yes</span>
<span class="lightgrey">Max Top List</span>                <span class="lightcyan">- 30</span>
<span class="lightgrey">Profanity Checking</span>          <span class="lightcyan">- No</span>
<span class="lightgrey">Registered Addons</span>           <span class="lightcyan">- Dragon\'s Teeth (1)
                              The Cursed Ruins (2)
                              Strangers in the Night (3)
                              Terror from Below (4)
                              The Rising Dawn (5)
                              The Sands of Time (6)
                              Savage Lands (7)
                              A Call to Arms (8)
                              Prophecy of Plague (9)</span>
<span class="darkgrey">-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>
</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>'''
    return 0

def files_v2():
    print '''<span class="white">V O I D</span> <span class="lightyellow">v%s-WEB (%s)</span><br/>
<span class="lightgrey">{BBS of Legends}</span><br/>
<span class="darkgreen">*Download Section*</span><br/><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/b2h_v2_1_.3.0.10.zip">B</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/b2h_v2_1_.3.0.10.zip">Blood2HTML v2.3.0.10</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/MegaMUD_v1.03u.exe">M</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/MegaMUD_v1.03u.exe">MegaMUD v1.03u</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/megamud_keygen.zip">K</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/megamud_keygen.zip">MegaMUD Keygen</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/Winterhawks_Paths_Installer_v2_1_.0.zip">P</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/Winterhawks_Paths_Installer_v2_1_.0.zip">Winterhawks Mod9 Path Updates</a><br/><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/Winterhawks word maps 1.11o 6-1.zip">1</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/Winterhawks word maps 1.11o 6-1.zip">Winterhawks v1.11o .DOC Maps</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/Winterhawks PDF maps 1.11o 6-1.zip">2</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/Winterhawks PDF maps 1.11o 6-1.zip">Winterhawks v1.11o .PDF Maps</a><br/><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/Setup-MME_v1.67.exe">E</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/Setup-MME_v1.67.exe">MajorMUD Explorer v1.67 (Full)</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/mudexplr_v1.70.rar">U</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/mudexplr_v1.70.rar">MajorMUD Explorer v1.70 (Upgrade)</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/files/data-v1.11p.exe">D</a><span class="darkgrey">] .</span> <a class="menutext" href="/files/data-v1.11p.exe">MajorMUD Explorer Data Pack (v1.11p)</a><br/><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/">X</a><span class="darkgrey">] .</span> <a class="menutext" href="/">BBS Main Menu</a><br/><br/>
<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">█</span>''' % (webver, mod)
    return 0


if not __name__ == None:
    global mysql, db, sql, _mod
    cfg.populate()
    cfg.db = cfg.sql_connect()
    cfg.sql = cfg.db.cursor()

if __name__ == '__main__':
    main()
