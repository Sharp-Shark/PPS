PPS = False

available_colors = ['red',
                    'pur',
                    'cya',
                    'roy',
                    'blu',
                    'vio',
                    'nul',
                    'nul']

render_colors = {'red':'red',
                 'pur':'purple',
                 'cya':'cyan',
                 'roy':'royalblue',
                 'blu':'blue',
                 'vio':'blueviolet',
                 'nul':'white'}

relations_table = {'red':{'red':2,
                          'pur':-0.5,
                          'cya':-1,
                          'roy':-0.25,
                          'blu':-4,
                          'vio':-0.5,
                          'nul':-2.4,
                          'other':[0.8, 50, 45, 1, 1]},
                   'pur':{'red':-0.5,
                          'pur':2.5,
                          'cya':0.3,
                          'roy':-0.12,
                          'blu':0,
                          'vio':-0.8,
                          'nul':-5,
                          'other':[0.9, 30, 40, 3, 1]},
                   'cya':{'red':1,
                          'pur':0,
                          'cya':2,
                          'roy':-0.6,
                          'blu':0,
                          'vio':-0.2,
                          'nul':-2,
                          'other':[0.85, 30, 60, 3, 1]},
                   'roy':{'red':0.5,
                          'pur':0.4,
                          'cya':-1,
                          'roy':-0.1,
                          'blu':-0.3,
                          'vio':-0.8,
                          'nul':-1.2,
                          'other':[0.9, 30, 40, 3, 1]},
                   'blu':{'red':3,
                          'pur':-0.6,
                          'cya':-1,
                          'roy':-0.5,
                          'blu':1,
                          'vio':-1.2,
                          'nul':-2,
                          'other':[0.8, 30, 60, 3, 1]},
                   'vio':{'red':-0.5,
                          'pur':-0.8,
                          'cya':-0.12,
                          'roy':0.3,
                          'blu':-0.25,
                          'vio':2.5,
                          'nul':-5,
                          'other':[0.9, 30, 100, 3, 1]},
                   'nul':{'red':0.5,
                          'pur':-1.2,
                          'cya':-2,
                          'roy':-0.6,
                          'blu':1,
                          'vio':-1.2,
                          'nul':-0.5,
                          'other':[0.85, 30, 40, 3, 1]}}

world = {'dist_decay':1,
         'force_mult':100,
         'force_cont':10,
         'amount_min':50,
         'amount_max':999,
         'screen_wrap':True}

'''
All Accepted Render Colors can be found at :
http://cng.seas.rochester.edu/CNG/docs/x11color.html

All Render Values have to be one of those Colors.
'''

if not PPS :
    original = 'unstable'
    print('[FILE ../PPS.py]saveFile = "saves/'+original+'"#'+open('../PPS.py','r').read()+'[FILE END]')
    exec('saveFile = "saves/'+original+'.py"#'+open('../PPS.py','r').read())
