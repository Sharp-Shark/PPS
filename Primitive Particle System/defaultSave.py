PPS = False

available_colors = ['red',
                    'pur',
                    'blu']

render_colors = {'red':'red',
                 'pur':'purple',
                 'blu':'blue'}

relations_table = {'red':{'red':0,
                          'pur':0,
                          'blu':0,
                          'other':[0.9, 30, 30, 3, 1]},
                   'pur':{'red':0,
                          'pur':0,
                          'blu':0,
                          'other':[0.9, 30, 30, 3, 1]},
                   'blu':{'red':0,
                          'pur':0,
                          'blu':0,
                          'other':[0.9, 30, 30, 3, 1]}}

world = {'dist_decay':1,
         'force_mult':60,
         'force_cont':6,
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
    original = 'new'
    print('[FILE ../PPS.py]saveFile = "saves/'+original+'"#'+open('../PPS.py','r').read()+'[FILE END]')
    exec('saveFile = "saves/'+original+'.py"#'+open('../PPS.py','r').read())
