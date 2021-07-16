PPS = False

available_colors = ['pur', 'red', 'ora', 'yel', 'gre', 'blu', 'whi', 'gre', 'bla']

render_colors = {'pur': 'blue', 'red': 'orange', 'ora': 'khaki', 'yel': 'red', 'gre': 'royalblue', 'blu': 'crimson', 'whi': 'purple', 'bla': 'lime'}

relations_table = {'pur': {'pur': -0.47, 'red': -0.9, 'ora': 0.44, 'yel': -0.45, 'gre': -0.7, 'blu': 0.86, 'whi': -0.91, 'bla': -0.14, 'other': [0.69, 43, 58, 2.2, 1.4]}, 'red': {'pur': 0.63, 'red': 0.55, 'ora': 0.65, 'yel': -0.7, 'gre': -0.78, 'blu': -0.58, 'whi': -0.32, 'bla': 0.42, 'other': [0.55, 39, 30, 3.8, 1.5]}, 'ora': {'pur': -0.79, 'red': -0.7, 'ora': -0.86, 'yel': 0.47, 'gre': 0.31, 'blu': -0.4, 'whi': 0.77, 'bla': 0.3, 'other': [0.8, 37, 59, 3.1, 1.5]}, 'yel': {'pur': -0.21, 'red': 0.21, 'ora': -0.74, 'yel': -0.29, 'gre': -0.18, 'blu': 0.74, 'whi': -0.29, 'bla': 0.79, 'other': [0.85, 45, 47, 3.6, 2.0]}, 'gre': {'pur': 0.44, 'red': -0.64, 'ora': -0.95, 'yel': -0.7, 'gre': -0.02, 'blu': -0.85, 'whi': 0.57, 'bla': -0.38, 'other': [0.73, 47, 45, 2.5, 2.0]}, 'blu': {'pur': -0.9, 'red': 0.82, 'ora': 0.73, 'yel': 0.56, 'gre': 0.14, 'blu': -0.74, 'whi': -0.94, 'bla': 0.85, 'other': [0.58, 49, 57, 3.8, 1.8]}, 'whi': {'pur': -0.73, 'red': 0.1, 'ora': -0.78, 'yel': -0.89, 'gre': -0.2, 'blu': -0.05, 'whi': -0.34, 'bla': -0.72, 'other': [0.83, 39, 21, 2.9, 1.4]}, 'bla': {'pur': 0.65, 'red': -0.77, 'ora': -0.41, 'yel': 0.18, 'gre': 0.37, 'blu': 0.36, 'whi': -0.17, 'bla': -0.84, 'other': [0.85, 47, 26, 2.0, 1.1]}}

world = {'dist_decay': 1, 'force_mult': 238, 'force_cont': 8.5, 'particles': 148, 'desired_fps': 35, 'pen_thickness': 6, 'screen_wrap': 1}

'''
All Accepted Render Colors can be found at :
http://cng.seas.rochester.edu/CNG/docs/x11color.html

All Render Values have to be one of those Colors.
'''

if not PPS :
    original = 'random#1'
    print('[FILE ../PPS.py]saveFile = "saves/'+original+'"#'+open('../PPS.py','r').read()+'[FILE END]')
    exec('saveFile = "saves/'+original+'.py"#'+open('../PPS.py','r').read())
