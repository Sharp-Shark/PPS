PPS = False

available_colors = ['thing']

render_colors = {'thing':'darkkhaki'}

relations_table = {'thing':{'thing':-0.1,
                            'other':[0.9, 30, 60, 3, 1]}}

world = {'dist_decay':1,
         'force_mult':240,
         'force_cont':6,
         'amount_min':50,
         'amount_max':999,
         'screen_wrap':False}

if not PPS :
    original = 'homogeneous'
    print('[FILE ../PPS.py]saveFile = "saves/'+original+'"#'+open('../PPS.py','r').read()+'[FILE END]')
    exec('saveFile = "saves/'+original+'.py"#'+open('../PPS.py','r').read())
