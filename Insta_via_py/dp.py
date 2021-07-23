#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:17:05 2021

@author: ved
"""

import instaloader
ig=instaloader.Instaloader()
usr_name=input("Enter user-name: ")
ig.download_profile(usr_name,profile_pic_only=True)