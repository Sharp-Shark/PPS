PPS = False

from random import randint as rng

available_render_colors = ['purple',
                           'deeppink',
                           'red',
                           'crimson',
                           'orange',
                           'coral',
                           'yellow',
                           'khaki',
                           'lime',
                           'green',
                           'cyan',
                           'royalblue',
                           'blueviolet',
                           'blue']

def getRandomRenderColor() :
    global available_render_colors
    number = rng(0,len(available_render_colors)-1)
    toReturn = available_render_colors[number]
    del(available_render_colors[number])
    return toReturn

available_colors = ['pur',
                    'red',
                    'ora',
                    'yel',
                    'gre',
                    'blu',
                    'whi',
                    'gre',
                    'bla']
for loop in range(0,rng(0,4)) :
    del(available_colors[len(available_colors)-1])
print('Number of colors: '+str(len(available_colors))+'.')

render_colors = {'pur':getRandomRenderColor(),
                 'red':getRandomRenderColor(),
                 'ora':getRandomRenderColor(),
                 'yel':getRandomRenderColor(),
                 'gre':getRandomRenderColor(),
                 'blu':getRandomRenderColor(),
                 'whi':getRandomRenderColor(),
                 'gre':getRandomRenderColor(),
                 'bla':getRandomRenderColor()}

relations_table = {'pur':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(10,100), rng(10,40)/10, rng(10,20)/10]},
                   'red':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'ora':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'yel':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'gre':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'blu':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'whi':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'gre':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]},
                   'bla':{'pur':rng(-100,100)/100,
                          'red':rng(-100,100)/100,
                          'ora':rng(-100,100)/100,
                          'yel':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'blu':rng(-100,100)/100,
                          'whi':rng(-100,100)/100,
                          'gre':rng(-100,100)/100,
                          'bla':rng(-100,100)/100,
                          'other':[rng(50,90)/100, rng(30,50), rng(20,60), rng(20,40)/10, rng(10,20)/10]}}

world = {'dist_decay':1,
         'force_mult':rng(100,250),
         'force_cont':rng(50,100)/10,
         'amount_min':50,
         'amount_max':999,
         'screen_wrap':True}

'''
All Accepted Render Colors can be found at :
http://cng.seas.rochester.edu/CNG/docs/x11color.html

All Render Values have to be one of those Colors.
'''

if not PPS :
    original = 'randomized'
    print('[FILE ../PPS.py]saveFile = "saves/'+original+'"#'+open('../PPS.py','r').read()+'[FILE END]')
    exec('saveFile = "saves/'+original+'.py"#'+open('../PPS.py','r').read())
