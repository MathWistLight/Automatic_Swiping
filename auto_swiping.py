# -*- coding: utf-8 -*-

# modules
import numpy as np
import pynder
import time

# FB user ID & FB token
usrid = "your_facebook_id" # Facebook ID
token = "your_facebook_token" # Facebook access token

# latitude & longitude(In this example, these lat&lon show Kyoto St.)
LAT = 34.985193
LON = 135.758595

session = pynder.Session(facebook_id = usrid, facebook_token = token) # logging in to Tinder account
session.matches()
session.update_location(latitude=LAT, longitude=LON)
users = session.nearby_users() # getting information of neaby users

print "You can swipe",session.likes_remaining,"times."

for usr in users:
    rest = session.likes_remaining
    print "===swipe counter：",counter,"======================="
    if rest==0:
        print "Finished!!"
        break

    usr.like() # swiping right
    time.sleep(np.abs(2.+np.random.normal()*3.))