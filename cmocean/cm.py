'''
Standardized colormaps for oceanography plots.

Used tool from http://bids.github.io/colormap/ to make perceptually correct
colormaps.

Created by Kristen Thyng
2016-06-18
'''

from __future__ import absolute_import

import matplotlib
import numpy as np
import os

from . import tools

# Location of rgb files
datadir = os.path.join(os.path.split(__file__)[0], 'rgb')

# List of colormap names
cmaps = ['thermal', 'haline', 'solar', 'ice', 'gray', 'oxy', 'deep', 'dense',
         'algae', 'matter', 'turbid', 'speed', 'amp', 'tempo', 'phase',
         'balance', 'delta', 'curl']

# initialize dictionary to contain colormaps
cmap_d = dict()

# add colormaps and reversed to dictionary
for cmap in cmaps:
    # rgb = np.loadtxt(cmap + '-rgb.txt')
    rgb = np.loadtxt(os.path.join(datadir, cmap + '-rgb.txt'))
    cmap_d[cmap] = tools.cmap(rgb, N=256)
    cmap_d[cmap].name = cmap
    cmap_d[cmap + '_r'] = tools.cmap(rgb[::-1, :], N=256)
    cmap_d[cmap + '_r'].name = cmap + '_r'

# make colormaps available to call
locals().update(cmap_d)
