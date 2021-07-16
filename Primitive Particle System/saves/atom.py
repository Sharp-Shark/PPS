PPS = False
from random import randint as rng
rng = rng(0,3)
if rng == 0 :
    available_colors = ['proton',
                        'proton',
                        'neutron',
                        'eletron',
                        'eletron',
                        'eletron']
elif rng == 1 :
    available_colors = ['proton',
                        'proton',
                        'eletron',
                        'eletron',
                        'eletron']
elif rng == 2 :
    available_colors = ['proton',
                        'eletron',
                        'eletron',
                        'eletron',
                        'eletron']
elif rng == 3 :
    available_colors = ['proton',
                        'neutron']

render_colors = {'proton':'red',
                 'neutron':'orange',
                 'eletron':'royalblue'}

relations_table = {'proton':{'proton':1,
                             'neutron':-1.2,
                             'eletron':-0.8,
                             'other':[0.8, 30, 70, 6, 1]},
                   'neutron':{'proton':-1.6,
                              'neutron':0.8,
                              'eletron':0.2,
                              'other':[0.8, 30, 60, 3, 1]},
                   'eletron':{'proton':-1.5,
                              'neutron':0.4,
                              'eletron':0.4,
                              'other':[0.9, 30, 120, 5, 1]}}

world = {'dist_decay':1,
         'force_mult':100,
         'force_cont':15,
         'particles':100,
         'desired_fps':30,
         'pen_thickness':8,
         'screen_wrap':True}

'''
All Accepted Render Colors can be found at :
http://cng.seas.rochester.edu/CNG/docs/x11color.html

All Render Values have to be one of those Colors.
'''

if not PPS :
    original = 'atom'
    print('[FILE ../PPS.py]saveFile = "saves/'+original+'"#'+open('../PPS.py','r').read()+'[FILE END]')
    exec('saveFile = "saves/'+original+'.py"#'+open('../PPS.py','r').read())
