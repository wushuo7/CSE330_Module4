import sys
import re
from player import Person

input = sys.argv[1] #get the path of the file

all = []
players_name = []
regex = re.compile(r"^([A-Za-z0-9_]+\s[A-Za-z0-9_]+)\s(?:\w+)\s(\d{1})\stimes\swith\s(\d{1})\b")


try:
    file = open(input,'r')
except IOError:
    print('cannot open', file)
else:
    #add all players' name in to a list
    for line in file:
        right = regex.match(line)
        if right:
            name = right.group(1)
            #bat = right.group(2)
            #hit = right.group(3)
            if name not in players_name:
                players_name.append(name)

    # create a list with all the player, every item inside it is player object
    for i in players_name:
        new = Person(i)
        all.append(new)
    file.close()
    # insert hit, bat, avg values into each Person item
    file1 = open(input, 'r')
    for line in file1:
        match1 = regex.match(line)
        if match1:
            name = match1.group(1)
            bat = match1.group(2)
            hit = match1.group(3)
            for someone in all:
                if someone.getname() == name:
                    someone.updateHit(hit)
                    someone.updateBat(bat)

    #calculate the average
    for i in all:
        bat_now = i.getBat()
        hit_now = i.getHit()
        avg = float(hit_now) / float(bat_now)
        new_avg = round(avg,3)
        i.updateAve(new_avg)
    # sort by player's avg
    all = sorted(all, key=lambda player: player.avg, reverse=True)

    # prints name: batting avg in decending order
    for a in all:
        print (a.getname()+":"+str(a.avg))

    file.close()






