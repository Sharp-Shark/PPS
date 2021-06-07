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
                          'yel':-2,
                          'gre':-1.5,
                          'blu':1,
                          'pur':-2,
                          'other':[0.9, 30, 30, 3, 1]},
                   'yel':{'red':-2,
                          'yel':-0.5,
                          'gre':1,
                          'blu':2,
                          'pur':0,
                          'other':[0.8, 30, 20, 3, 1]},
                   'gre':{'red':-1,
                          'yel':0,
                          'gre':1,
                          'blu':-1.5,
                          'pur':0,
                          'other':[0.9, 30, 10, 3, 1]},
                   'blu':{'red':1,
                          'yel':0.5,
                          'gre':-0.5,
                          'blu':-0.5,
                          'pur':-2,
                          'other':[0.9, 30, 20, 3, 1]},
                   'pur':{'red':-1,
                          'yel':1,
                          'gre':1,
                          'blu':-1,
                          'pur':-1,
                          'other':[0.9, 30, 30, 3, 1]}}

world = {'dist_decay':1,
         'force_mult':60,
         'force_cont':6,
         'amount_min':50,
         'amount_max':999,
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
