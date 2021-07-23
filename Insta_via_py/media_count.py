#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:14:38 2021

@author: ved
"""

import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, 'python_scripts')

print(profile.mediacount)


