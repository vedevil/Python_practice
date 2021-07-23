#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 16:26:55 2021

@author: ved
"""

import instaloader 
L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, 'crica2z')
print(type(profile))
print(profile.mediacount)
print(profile.followers)
followers = [follower.username for follower in profile.get_followers()]