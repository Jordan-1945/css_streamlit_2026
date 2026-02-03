# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:08:57 2026

@author: sphum
"""

import subprocess

file = "Jordan Streamlit.py"


subprocess.Popen(
    ["streamlit", "run", file], shell=True)