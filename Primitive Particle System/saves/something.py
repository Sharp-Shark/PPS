PPS = False

available_colors = ['red',
                    'yel',
                    'gre',
                    'blu',
                    'pur']

render_colors = {'nick':'name',
                 'red':'red',
                 'yel':'yellow',
                 'gre':'green',
                 'blu':'blue',
                 'pur':'purple'}

relations_table = {'red':{'red':0.4,
                          'yel':-0.8,
                          'gre':-1,
                          'blu':0.7,
                          'pur':-2.4,
                          'other':[0.8, 30, 40, 3, 1]},
                   'yel':{'red':-2,
                          'yel':0.4,
                          'gre':-1,
                          'blu':1,
                          'pur':0.5,
                          'other':[0.8, 30, 30, 3, 1]},
                   'gre':{'red':-1,
                          'yel':-0.5,
                          'gre':0.9,
                          'blu':-0.5,
                          'pur':-1.5,
                          'other':[0.8, 30, 20, 3, 1]},
                   'blu':{'red':0.7,
                          'yel':-1.2,
                          'gre':-0.8,
                          'blu':-0.3,
                          'pur':-1,
                          'other':[0.8, 30, 30, 3, 1]},
                   'pur':{'red':-1.6,
                          'yel':1,
                          'gre':0,
                          'blu':-0.6,
                          'pur':-0.5,
                          'other':[0.8, 30, 40, 3, 1]}}

world = {'dist_decay':1,
         'force_mult':20,
         'force_cont':5,
         'particles':100,
         'desired_fps':30,
         'pen_thickness':6,
         'screen_wrap':True}

'''
All Accepted Render Colors can be found at :
http://cng.seas.rochester.edu/CNG/docs/x11color.html

All Render Values have to be one of those Colors.
'''

if not PPS :
    original = 'something'
    print('[FILE ../PPS.py]\nsaveFile = "saves/'+original+'"\n#'+open('../PPS.py','r').read()+'\n[FILE END]')
    exec('saveFile = "saves/'+original+'.py"\n#'+open('../PPS.py','r').read())

'''
PPS = False

available_colors = ['red',
                    'yel',
                    'gre',
                    'blu',
                    'pur']

render_colors = {'nick':'name',
                 'red':'red',
                 'yel':'yellow',
                 'gre':'green',
                 'blu':'blue',
                 'pur':'purple'}

relations_table = {'red':{'red':0.5,
                          'yel':-0.8,
                          'gre':-1,
                          'blu':0.7,
                          'pur':-2.4,
                          'other':[0.9, 30, 30, 3, 1]},
                   'yel':{'red':-2,
                          'yel':0,
                          'gre':-0.5,
                          'blu':1,
                          'pur':1.5,
                          'other':[0.9, 30, 20, 3, 1]},
                   'gre':{'red':-1,
                          'yel':-0.5,
                          'gre':1,
                          'blu':-0.5,
                          'pur':-1.5,
                          'other':[0.9, 30, 10, 3, 1]},
                   'blu':{'red':0.7,
                          'yel':0.5,
                          'gre':-0.8,
                          'blu':-0.4,
                          'pur':-1.6,
                          'other':[0.9, 30, 20, 3, 1]},
                   'pur':{'red':-1.6,
                          'yel':1,
                          'gre':0,
                          'blu':-0.8,
                          'pur':-0.6,
                          'other':[0.9, 30, 30, 3, 1]}}

world = {'dist_decay':1,
         'force_mult':60,
         'force_cont':6,
         'particles':100,
         'desired_fps':30,
         'pen_thickness':6,
         'screen_wrap':False}

if not PPS :
    original = 'something'
    print('[FILE ../PPS.py]\nsaveFile = "saves/'+original+'"\n#'+open('../PPS.py','r').read()+'\n[FILE END]')
    exec('saveFile = "saves/'+original+'.py"\n#'+open('../PPS.py','r').read())
'''
