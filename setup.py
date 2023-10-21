import sys
import os
from cx_Freeze import setup, Executable

files = ['templates/', 'static/']

target = Executable(
    script='main.py'
)

setup(
    name = 'Telegraph Client',
    version = '0.1',
    author = 'Khudoberdi A.',
    options = {'build_exe': {'include_files' : files, 'include_msvcr': True, 'silent_level': 3}},
    executables = [target]
)