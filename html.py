#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from __future__ import division
from subprocess import getoutput
from os import listdir, stat
from random import randrange
from sys import version
from time import localtime, strftime
import cgi
import config as cfg
import math

mod = strftime("%b %d %Y %H:%M:%S", localtime(stat(__file__).st_mtime))
webver = "2.2"


def main():
    return 0

def header(menu):
    """default html header"""
    ver=version.split("\n")
    quote=["attacking the shadow healer since '94.",
          "coming to a general store near you.",
          "now running 2400 baud !!"]
    rand=randrange(0, len(quote), 1)
    print("Content-type: text/html\n\n")
    print("""<!DOCTYPE html>
<html lang='en'>\n
\t<head>
\t\t<meta charset='utf-8' />
\t\t<title>VOID:  %s</title>
\t\t<link rel='icon' href='/favicon.ico' type='image/x-icon' />
\t\t<link rel='shortcut icon' href='/favicon.ico' type='image/x-icon' />
\t\t<link rel='stylesheet' href='/css/style.css' type='text/css' media='screen, projection' />
\t\t<meta name='author' content='Sean Bruen' />
\t\t<meta name='description' content='VOID is running on Worldgroup v3.30-NT with MajorMUD v1.11p!' />
\t\t<meta name='generator' content='Python %s' />
\t\t<meta name='keywords' content='void, majormud, mmud, realm of legends, bbs of legends, mud, bbs, worldgroup, tlord, t-lord, Sean Bruen, kyau, aftermud, amud' />""" % (quote[rand], ver[0].strip()))
    print("\t\t<script src='//code.jquery.com/jquery-1.10.2.min.js'></script>")
    print("\t\t<script src='/js/global.js' charset='utf-8'></script>")
    if menu == "main":
        print("\t\t<script src='/js/main.js' charset='utf-8'></script>")
    elif menu == 'files':
        print("\t\t<script src='/js/files.js' charset='utf-8'></script>")
    elif menu == "megamud" or menu == "majormud" or menu == "wgserv":
        print("\t\t<script src='/js/section.js' charset='utf-8'></script>")
    else:
        print("\t\t<script src='/js/other.js' charset='utf-8'></script>")
    print("""\t</head>\n
<body>\n
<div id='content'>
\t<div id='statusbar'><a href='https://github.com/kyau/bbs-kyau_net'><img alt='Github' src='/img/github.png' /></a></div>
\t<div id='tooltip'><span class='white'>Github:</span> kyau/bbs-kyau_net <span class='white'>(<span class='lightcyan'>%s</span>)</span></div>
\t<img alt='logo' id='logo' src='/img/aftermud-logo.png' />
\t<div id='term'>""" % cfg.git_version())
    return 0

def footer(warning):
    """ default html footer """
    sqlstr = "SELECT count(*) FROM online"
    players_online = cfg.sql_cmd(sqlstr, 1)
    print("\t\t<div id='online'><span class='lightblue'>Online: %d</span></div>" % players_online[0])
    print("\t</div>")
    if warning:
        print("\t<div id='msg'>Press <span class='darkcyan'>?</span> for help.</div>")
    else:
        print("\t<div id='msg'>Press <span class='darkcyan'>X</span> to exit to the Main Menu.</div>")
    print("""\t<div id='help'><img alt='Help!' src='/img/help.png' /></div>
\n</div>\n</body>\n
</html>\n""")
    return 0

def error(e):
    if e == 404:
        print("""\t\t<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> 404<br/>
\t\t<br/><br/><br/><br/>
\t\t<img alt='404' src='/img/404.ANS.png' style='margin-left:60px' />
\t\t<pre>                               <span class='darkcyan' style='font-weight:bold;'>404</span><span class='white' style='font-weight:bold;'>:</span> <span class='lightgrey'>File Not Found</span></pre><br/><br/><br/><br/><br/><br/>
\t\t<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> <span id='cursor'>&#x2588;</span>""")
        return 0
    else:
        return 0


def main_v2():
    """ main menu """
    print("\t\t<span class='white'>V O I D</span> <span class='lightyellow'>v%s-WEB (%s)</span><br/>" % (webver, mod))
    print("""\t\t<span class='lightgrey'>{BBS of Legends}</span><br/>
\t\t<span class='lightmagenta'>*ANSI RECOMMENDED*</span><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?enter'>E</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?enter'>Enter the Realm</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='http://kyau.net/wiki/Category:MajorMUD'>H</a><span class='darkgrey'>] .</span> <a class='menutext' href='http://kyau.net/wiki/Category:MajorMUD'>Wiki</a> <span class='darkcyan'>*WIP*</span><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?about'>A</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?about'>About the BBS</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?cap'>C</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?cap'>Captures</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?files'>D</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?files'>Downloads</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?gossip'>S</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?gossip'>Gossip Chat</a> <span class='darkcyan'>*NEW*</span><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?rules'>R</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?rules'>Realm Rules</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?notes'>N</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?notes'>Release Notes</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?top'>T</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?top'>Top Adventurers</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?topgang'>G</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?topgang'>Top Gangs</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?who'>W</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?who'>Who's in the Realm</a><br/><br/>

\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/?realm'>!</a><span class='darkgrey'>] .</span> <a class='menutext' href='/?realm'>Realm Settings</a><br/><br/>
\t\t<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> <span id='cursor'>&#x2588;</span>
\t\t<br/><br/><br/><br/><br/><br/><br/>&nbsp;""")
    return 0

def enter_v2():
    """ enter the realm """
    print("\t\t<span class='white'>V O I D</span> <span class='lightyellow'>v%s-WEB (%s)</span><br/>" % (webver, mod))
    print("""\t\t<span class='lightgrey'>{BBS of Legends}</span><br/>
\t\t<span class='darkgreen'>*Enter the Realm*</span><br/><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='telnet://bbs.majormud.org'>T</a><span class='darkgrey'>] .</span> <a class='menutext' href='telnet://bbs.majormud.org'>Telnet</a><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/term/'>H</a><span class='darkgrey'>] .</span> <a class='menutext' href='/term/'>HTML5</a><br/><br/>
\t\t<span class='darkgrey'>[</span><a class='menuitem' href='/'>X</a><span class='darkgrey'>] .</span> <a class='menutext' href='/'>BBS Main Menu</a><br/><br/>
\t\t<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> <span id='cursor'>&#x2588;</span>""")
    return 0

def flash_v2():
    """ enter the realm: flash """
    print("""\t<script type='text/javascript' src='swfobject.js'></script>
\t<script type='text/javascript'>
\t\tvar flashvars = {};
\t\tvar params = {};
\t\tparams.menu = 'false';
\t\tparams.bgcolor = '000000'
\t\tvar attributes = {};
\t\tswfobject.embedSWF('flashterm.swf', 'flash', '650', '440', '9.0.115', 'expressInstall.swf', flashvars, params, attributes);
\t\tfunction setFocusOnFlash() {
\t\t\tvar fl = document.getElementById('term');
\t\t\tfl.focus(); }
\t\tswfobject.addLoadEvent(setFocusOnFlash);
\t</script>
\t<div id='flash'></div>
\t<style><!-- #term {background:#131313;border:0px;padding:0;} --></style>""")
    return 0

def about_v2():
    """ about the bbs """
    stats = cfg.sys_stat()
    print("""<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> A<br/>\n<pre>\n
<span class='darkmagenta'>   _________________________________________________________________________</span>\n
<span class='lightblue'>                                   V O I D</span>\n
<span class='lightgrey'>      VOID is running on Worldgroup v3.30-NT inside a WindowsXP Virtual
         Machine, the stats for the system the VM is running on are:</span>\n
<span class='darkmagenta'>                  Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
                             %s
                             2 x 1TB HDD (RAID1)
                             100mbit from OVH.ca</span>\n
   <span class='darkgrey'>%s</span>\n
<span class='lightgrey'>        If you have any questions please direct them to the user Kyau
                using the Electronic Mail built into the BBS.</span>\n
<span class='darkmagenta'>   _________________________________________________________________________</span>
</pre><br/>\n<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> <span id='cursor'>&#x2588;</span>""" % (stats[1], stats[0]))
    return 0

def gos_v2():
    """ gossip log """
    print("<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> S<br/><br/>")
    sqlstr = "SELECT * FROM (SELECT * FROM gossip ORDER BY timestamp DESC LIMIT 20) AS ttbl ORDER BY ID ASC"
    tmp = cfg.sql_cmd(sqlstr, 2)
    if not tmp == None:
        for row in tmp:
            if row[1] == "***":
                print("<div id='wrap'><br/><span class='darkred'>*** %s</span><br/></div>\n" % (cgi.escape(row[2])))
            else:
                dt = cfg.tstruct(str(row[3]))
                tzone = ""
                #print("dt.hour: '" + str(dt.hour) + "'")
                if dt.hour > 12:
                    if dt.hour > 12 and dt.hour < 22:
                        timestamp = "0"+str(dt.hour-12)+":"
                    else:
                        timestamp = str(dt.hour-12)+":"
                    tzone = "p"
                else:
                    if dt.hour == 0:
                        timestamp = "0"+str(dt.hour)+':'
                    else:
                        timestamp = str(dt.hour)+':'
                    tzone = "a"
                if len(str(dt.minute)) < 2:
                    timestamp += "0"+str(dt.minute)
                else:
                    timestamp += str(dt.minute)
                timestamp += tzone
    #            timestamp = strftime('%I:%M', timestamp)
                print("<div id='wrap'><span class='darkgrey'>%s</span> <span class='lightgrey'>%s gossips:</span> <span class='darkmagenta'>%s</span></div>\n" % (timestamp, row[1], cgi.escape(row[2])))
    print("<br/>\n<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> <span id='cursor'>&#x2588;</span>")
    return 0

def who_v2():
    """ who's online """
    color = None
    exphr = None
    xphr = None
    kph = 0.0
    print("<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> W<br/>\n<pre>\n")
    sqlstr = "SELECT count(*) FROM online"
    tmp = cfg.sql_cmd(sqlstr, 1)
    if tmp[0] > 0:
        print("<span class='lightyellow'>         Current Adventurers</span>")
        print("<span class='darkgrey'>         ===================</span>")
        sqlstr = "SELECT user, busy FROM online"
        tmp = cfg.sql_cmd(sqlstr, 2)
        for row in tmp:
            sqlstr = "SELECT alignment, title, exp, expold, gang FROM users WHERE user LIKE '"+row[0]+"%'"
            tmp = cfg.sql_cmd(sqlstr, 1)
            if tmp[0] == "Criminal": color = "darkyellow"
            elif tmp[0] == "Villain": color = "lightyellow"
            elif tmp[0] == "Outlaw": color = "darkred"
            elif tmp[0] == "FIEND": color = "lightred"
            else: color = "white"
            if tmp[2] == tmp[3]:
                exphr = "<span class='idle'>idle</span>"
            else:
                xphr = (tmp[2] - tmp[3]) * 12
                kph = xphr / 1000
                if round(kph, 0) > 10:
                    xphr = "%d" % kph
                else:
                    xphr = round(kph, 1)
                exphr = "<span class='xphr'>%sk/hr</span>" % str(xphr)
            if tmp[4] == "":
                print("<span class='line'>%s<span class='%s'>%8s</span> <span class='darkgreen'>%-20s %s</span>  <span class='darkmagenta'>%s</span></span>" % (exphr, color, tmp[0], row[0][:20], row[1], tmp[1]))
            else:
                print("<span class='line'>%s<span class='%s'>%8s</span> <span class='darkgreen'>%-20s %s</span>  <span class='darkmagenta'>%s</span>  <span class='darkgreen'>of</span> <span class='darkyellow'>%s</span></span>" % (exphr, color, tmp[0], row[0][:20], row[1], tmp[1], tmp[4]))

    else:
        print("<span class='darkmagenta'>There are no users in the game at the moment.</span>")
    print("</pre><br/>\n<span class='darkgrey'>[</span><a class='menutext' href='/'>VOID</a><span class='darkgrey'>]</span><span class='lightgrey'>:</span> <span id='cursor'>&#x2588;</span>")
    return 0

def top_v2():
    """ top 100 adventurers """
    rank = 1
    print('<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> T<br/>\n<pre>\n')
    sqlstr = 'SELECT count(*) FROM users'
    tmp = cfg.sql_cmd(sqlstr, 1)
    if tmp[0] > 0:
        print('<span class="darkyellow">Top Heroes of the Realm</span>')
        print('<span class="lightgrey">-=-=-=-=-=-=-=-=-=-=-=-</span>\n')
        print('<span class="darkred">Rank</span> <span class="darkgreen">Name</span>                  <span class="darkmagenta">Class</span>      <span class="darkyellow">Gang/Guild</span>          <span class="darkgreen">Experience</span>     <span class="darkgrey">k/hr</span>')
        print('<span class="darkgrey">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>')
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
            print('<span class="line"><span class="darkred">%3d.</span> <span class="darkgreen">%-21s</span> <span class="darkmagenta">%-10s</span> <span class="darkyellow">%-19s</span> <span class="darkgreen">%-14d</span> %s</span>' % (rank, row[0][:21], row[1], row[2], row[3], exphr))
            rank = rank + 1
    else:
        print('<span class="darkmagenta">Realm recently reset.</span>')
    print('</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>')
    return 0

def topg_v2():
    """ top 100 gangs """
    rank = 1
    print('<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> G<br/>\n<pre>\n')
    sqlstr = 'SELECT count(*) FROM gangs'
    tmp = cfg.sql_cmd(sqlstr, 1)
    if tmp[0] > 0:
        print('<span class="darkyellow">Top Gangs of the Realm</span>')
        print('<span class="lightgrey">-=-==-=-=-=-=-=-=-=-=-</span>\n')
        print('<span class="darkred">Rank</span> <span class="darkgreen">Gangname</span>            <span class="darkmagenta">Leader</span>      <span class="darkyellow">Members</span> <span class="darkgreen">Created</span>      <span class="darkyellow">Exp</span>            <span class="darkgrey">xp/hr</span>')
        print('<span class="darkgrey">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>')
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
#            print('%3s. %-19s %-11s %-7s %-12s %s' % (rank, name, leader, members, creation, exp))
            print('<span class="line"><span class="darkred">%3d.</span> <span class="darkgreen">%-19s</span> <span class="darkmagenta">%-11s</span> <span class="darkyellow">%-7d</span> <span class="darkgreen">%-12s</span> <span class="darkyellow">%-13d</span> %s</span>' % (rank, row[0][:19], row[1], row[2], row[5], row[3], exphr))
            rank = rank + 1
    else:
        print('<span class="darkmagenta">There are no gangs currently established!</span>')
    print('</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>')
    return 0

def notes_v2():
    print('<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> I<br/>\n<pre>\n')
    print('''  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   AfterMUD - Eternity Awakened                                Release Notes
  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

  Version 0.1e - 08/06/16
  =========================

  1) Added a room healing spell to the NewHaven healer (minor healing).

  2) Added a room healing spell to the Silvermere healer (godheal).


  Version 0.1d - 08/04/14
  =========================

  1) Added the universal 'fast trainer' to the graveyard for training to
     level 11 without making the hike to the quest weapon / spirit. This
     trainer has an addition 100% markup and gives you no quest weapon.

  2) Added Duelist/Battlemage quest weapons (only sold no spirit):

                        Dmg: 6-18       Speed: 1375     Req Str: 30
       crimson rapier   Acc: +10        BS Acc: 15
          1H Sharp      AC/DR: 2.0/0    Enc: 25
                        Abilities: Magical+2, Quality+50, BS Min+7,
                                   BS Max+10, Crits+2
                                   Level 10+, Duelist Only

                        Dmg: 9-25       Speed: 1700     Req Str: 45
      runed greatsword  Acc: +8         BS Acc: 0
          2H Sharp      AC/DR: 2.0/0    Enc: 90
                        Abilities: Magical+2, Quality+50, S.C.+1,
                                   Max Mana+10, Mana Regen+10%
                                   Level 10+, Battlemage Only

  3) Added Duelist to the list of classes that can use main gauche's
     (these are parrying daggers).

  4) Portal Room - Alpha, Beta & Zed Wings now use signs and commands
     for teleportation. Broken portal room also added.
        Alpha Wing - Restrictions: Lv5
        Beta Wing - Restrictions: Lv15
        Zed Wing - Restrictions Lv50

  5) Access to the abandoned shop can now be had via 'inhale' as well.

  6) Dragonborn race created
        EXP: 50%
        Starting CP: 100
        HP Bonus: +2
        STR: 55 - 130       AGI: 40 - 100
        INT: 30 - 80        HEA: 55 - 125
        WIL: 20 - 60        CHA: 55 - 120
        Abilities: Dark Vision, Resist Cold +10, Resist Fire +10, Resist
                   Lightning +10, Resist Poisons +50%

  7) Shadowling race created
        EXP: 50%
        Starting CP: 100
        HP Bonus: -1
        STR: 40 - 100       AGI: 60 - 140
        INT: 50 - 120       HEA: 30 - 80
        WIL: 40 - 110       CHA: 30 - 60
        Abilities: Dark Vision, Racial Stealth, Critical Hits +2

  8) Battlemage class created, titles also added
        EXP: 220%
        Weapon: Any          Armour: Silk
        Magic: Mage-1        Combat: 5
        HP/Level: 5-9

  9) Knife removed from Newhaven weapon store, new weapon created named
     'pocket knife', will be a free version of the knife with one less min
     damage and 5 less encumbrance.

  10) Quest modifications: Added Duelist to PerStealth, Added Battlemage to
      Smash, Meditate text-block is full will need new quest

  11) Completed the Mystic Cavern, exits the other side of the mountain at
      the bottom of the Staircase to the Heavens. This is guarded by two of
      a new monster 'elite drake guard (~lv50)'.


  Version 0.1c - 07/29/14
  =========================

  1) Created an Abandoned Shop in Silvermere the back room in which leads
     to a portal room (access lv20+). Different wings in the portal room
     will open up at different levels.

  2) First portal to Blackwood Forest created, new area branched off of
     the forest called 'Mythic Caverns'. This will lead to new end-game
     areas.

  3) Added items to Newhaven Weapon Shop: knife

  4) Mythic Caverns: 3 areas branch off of entrance, one for each
     alignment. Each alignment tunnel dead ends at an NPC, all known
     at this point as 'strangers'.

  Alpha) Added developer commands in the Back Room
            - devxp: gives the user 600 million experience points
            - devmoney: gives the user 50 runic coins
            - duelist: gives you a full set of level 50 duelist gear
        Hidden universal Lv1-100 trainer in the Back Room
        * Reminder all stuff marked Alpha will not be in the release.


  Version 0.1b - 07/28/14
  =========================

  1) Removal of Silvermere & Darkwood Forest chatter (room spells)

  2) Room call change from 'cc' to 'bb'

  3) Bard songs reworked:

        Bard-0: lore, draining (dran), evasion (evas)
        Bard-1: wisdom (wisd), brilliance (bril), might (mite), agility (agil),
                beauty (beau), quickness (quik), heroism (hero),
                enlightenment (enli)
        Bard-2: valour (valr), discord (disc), misfortune (mfor),
                foolishness (fool), stupidity (dumb), weakness (weak),
                clumsiness (clum), life, traveling (trav), ugliness (ugly),
                blasting (blas), silence (mute), lethargy (dazl), pain,
                stunning (stun), shockwave (shok), sonic blast (sbla),
                knowledge (know), force (foce), swiftness (swif),
                soothing (soot), battle (batt), elements (elem),
                futility (futl), hopelessness (hopl)

  4) Duelist class created, titles also added
        EXP: 200%
        Weapon: 1H Sharp     Armour: Leather
        Magic: Bard-1        Combat: 4
        HP/Level: 5-9


  Version 0.1a - 07/26/14
  =========================

  1) Shop: Sarkhee's Jewelry now stocks gold jeweled ring.

  2) Added Shop: Limited Shop located in NE Silvermere.
        - Stocked: Lv10 Quest Weapons

  3) Removed limits from all items.''')
    print('</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>')
    return 0

def rules_v2():
    print('<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> I<br/>\n<pre>\n')
    print('<img alt="Rules Header" src="/img/rules.png" border="0" />')
    print('<span class="darkgrey">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>')
    print('''
<span class="lightgrey">     -  You are allowed to create as many characters as you like,
        however you are limited to 2 characters logged in at once.

     -  PvP (Player vs. Player) is limited to +/-5, 1v1 and both toons
        must be at the keyboard (not scripting).
        *Multi-telnet PvP is not allowed*

     -  There is no AFK limit.

     -  Once you are out of the NOOB class and into the MMUD class
        (5 days of activity required) you will have access to SYS GOTO &
        SYS MAP.

     -  Class "SYSOP" are not playing accounts and are only active
        for troubleshooting and/or greivences (re-rolls, etc.).

     -  Class "ELITE" are considered MUDOPs, and as such are only given
        SYS STATUS, SYS LIST, & SYS REPORT.
        (this class is mostly for playing Sysops)

     -  These rules apply to both MajorMUD and AfterMUD.

     -  MajorMUD is a legacy realm and as such is not majorly supported.</span>''')
    print('</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>')
    return 0

def realm_v2():
    print('''<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> !<br/>\n<pre>\n
<span class="white">MajorMUD Settings</span> <span class="lightmagenta">[<span class="darkmagenta">VOID</span>]</span>
<span class="darkgrey">-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-</span>
<span class="lightgrey">Talk Char</span>                   <span class="lightcyan">- .</span>
<span class="lightgrey">Yell Char</span>                   <span class="lightcyan">- "</span>
<span class="lightgrey">Death HP</span>                    <span class="lightcyan">- -150</span>
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
</pre><br/>\n<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>''')
    return 0

def files_v2():
    print('''<span class="white">V O I D</span> <span class="lightyellow">v%s-WEB (%s)</span><br/>
<span class="lightgrey">{BBS of Legends}</span><br/>
<span class="darkgreen">*Download Sections*</span><br/><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/?megamud">1</a><span class="darkgrey">] .</span> <a class="menutext" href="/?megamud">MegaMud</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/?majormud">2</a><span class="darkgrey">] .</span> <a class="menutext" href="/?majormud">MajorMUD</a><br/>
<span class="darkgrey">[</span><a class="menuitem" href="/?wgserv">3</a><span class="darkgrey">] .</span> <a class="menutext" href="/?wgserv">Worldgroup</a><br/><br/>
<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>''' % (webver, mod))
    return 0

def filesection(section, name):
    print('''\t\t<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> #<br/>\n
\t\t<br/><div style="text-align: center"><span class="lightyellow">%s Downloads</span></div><br/>
\t\t<table>
\t\t\t<tr>
\t\t\t\t<td class="filename">Filename</td>
\t\t\t\t<td class="size">Size</td>
\t\t\t\t<td class="diz">Description</td>
\t\t\t</tr>
\t\t\t<tr>
\t\t\t\t<td class="colspan="3" style="color: #8c8b89">=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=</td>
\t\t\t</tr>''' % name)

    files = listdir('files/'+section+'/')
    files.sort()
    for file in files:
        if file.endswith('.ZIP'):
            fileinfo = stat('files/'+section+'/'+file)
            filesize = fileinfo.st_size
            if filesize > 1024:
                if filesize > 1048476:
                    filesize = str(round((filesize / 1024 / 1024), 1))+'M'
                else:
                    filesize = str(round((filesize / 1024), 1))+'K'
            else:
                filesize = str(filesize)+'B'
            file_id = getoutput('recode -p CP437..html4 < files/'+section+'/'+file[:-4]+'.DIZ')
            if file_id[-25:] == 'No such file or directory':
                file_id = getoutput('recode -p CP437..html4 < files/NO.DIZ')
            print('''\t\t\t<tr class="file">
\t\t\t\t<td class="filename"><a href="/files/%s/%s">%s</a></td>
\t\t\t\t<td class="size">%s</td>
\t\t\t\t<td class="diz">%s</td>
\t\t\t</tr>''' % (section, file, file, filesize, file_id))

    print('''\t\t</table><br/>
\t\t<span class="darkgrey">[</span><a class="menutext" href="/">VOID</a><span class="darkgrey">]</span><span class="lightgrey">:</span> <span id="cursor">&#x2588;</span>''')
    return 0


if not __name__ == None:
    global mysql, db, sql, _mod
    cfg.populate()
    cfg.db = cfg.sql_connect()
    cfg.sql = cfg.db.cursor()

if __name__ == '__main__':
    main()
