saveFile = 'none'; original='pps'
''''''
# Imports
''''''
from random import randint as random
from math import sqrt
import turtle
import time
import math
canvas = turtle.getcanvas()
wait = time.sleep
turtle.title('PPS - Primitive Particle System')
''''''
# Variables
''''''
#Check link below to find more colors
WANT_MORE_COLORS = "http://cng.seas.rochester.edu/CNG/docs/x11color.html"

#Determines where to load "save" files from.
#Set to 'null' to just use the ones defined
#in the file. Save files are colors, relations,
#names...
if saveFile == 'none' :
    loadFrom = 'saves/'+turtle.textinput('loadFrom','File Name(string)\n<- ')+'.py'
    exec('PPS = True\n#'+open(loadFrom,'r').read())
    print('[FILE '+loadFrom+']\n'+'PPS = True\n#'+open(loadFrom,'r').read()+'\n[FILE END]')
    print('Running from Simulator')
    saveFile = 'pps'
else :
    print('Running from Settings')

LOOP = True #Continue Main Loop
count = 0
particles = [] #All particles are stored here
tick = 0 #How many iterations have passed
average_fps = 0 #Average FPS
''''''
# Objects
''''''
def writeToLog (txt, logName='') :
    if original == 'pps' :
        logFile = open('log.txt','a')
    else :
        logFile = open(original+'_log.txt','a')
    logFile.write('\n'+txt)
    logFile.close()

def numTo0 (x) :
    if x > 0 :
        return 1
    elif x < 0 :
        return -1
    else :
        return 0

def normPlus (x,y) : #Normalize and A Bit More
    magged = mag(x,y)
    return care_div(x, magged) - care_div(y, magged)

def norm (x,y) : #Normalize
    magged = mag(x,y)
    return [care_div(x, magged), care_div(y, magged)]

def mag (x,y) : #Magnitude
    return sqrt(x * x + y * y)

def care_div (a,b) : # careful division
    if a==0 or b==0 :
        return 1
    else :
        return a/b

def care_abs (n) :
    return n * numTo0(n)

def Max (n,m) :
    if n>m :
        return n
    else :
       return m

def Min (n,m) :
    if n<m :
        return n
    else :
        return m
#Cap = min

def tPrint (txt='',pos=(0,0),size=21) : #Prints to screen
    turtle.color('lightgray')
    turtle.goto(pos)
    turtle.write(txt,font=("IBM Plex Mono Medium",size,"bold"))

def drawTheLine () : 
    turtle.goto(0,0)
    turtle.color("#0F0F0F")
    turtle.pendown()
    turtle.fd(1000);turtle.bk(2000)
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(90)
    turtle.pendown()
    turtle.fd(1000);turtle.bk(2000)
    turtle.penup()

def root (n,r=2) :
    return n**(1/r)

def fWrap (cor) : #cor as in coord, screen-wraps a Float (or Int)
    return (300 * numTo0(cor) * -1) + min((300 - abs(cor)), 300) * numTo0(cor) * -1

def vWrap (cor) : #cor as in coords, screen-wraps a Vector
    return [ (300 * numTo0(cor[0]) * -1) + min((300 - abs(cor[0])), 300) * numTo0(cor[0]) * -1 , (300 * numTo0(cor[0]) * -1) + min((300 - abs(cor[1])), 300) * numTo0(cor[1]) * -1 ]
    #return [ min((300 - abs(cor[0])), 300) * numTo0(cor[0]) * -1 , min((300 - abs(cor[1])), 300) * numTo0(cor[1]) * -1 ]
    #return [(cor[0] + 450) % 300 - 150, (cor[1] + 450)% 300 - 150]
    #return [((((cor[0] + 150) % 300) + 150) % 300) - 150, ((((cor[1] + 150) % 300) + 150) % 300) - 150]

def distance (corA,corB,wrap=world['screen_wrap']) : #cor as in coords
    #Screen Wrapping
    howWrap = [1,1]
    if wrap :
        if distance(corA, vWrap(corB), False) < distance(corA, corB, False) :
            corA_ = corA
            corB_ = vWrap(corB)
            howWrap = [-1,-1]
        elif False and distance(corA, [fWrap(corB[0]), corB[1]], False) < distance(corA, corB, False) :
            corA_ = corA
            corB_ = [fWrap(corB[0]), corB[1]]
            howWrap = [-1,1]
        elif False and distance(corA, [corB[0], fWrap(corB[1])], False) < distance(corA, corB, False) :
            corA_ = corA
            corB_ = [corB[0], fWrap(corB[1])]
            howWrap = [1,-1]
        else :
            corA_ = corA
            corB_ = corB
    else :
        corA_ = corA
        corB_ = corB
    #Actual Distance Formula
    return (sqrt( (corA_[0]-corB_[0])**2 + (corA_[1]-corB_[1])**2 ), howWrap)

def force (distance,mult,strength=50,offset=100,window=2,shape=1) :
    return world['force_cont']/(distance**2) + (mult * max(1 / distance, strength - abs(distance*window*strength - offset*window)**shape))
class particle (object) : #particle object
    def __init__ (self,x=0,y=0,color=available_colors,index = 0) :
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        #Color determines appearence, and behaviour
        if color in available_colors :
            self.color = color
        else :
            self.color = color[random(0,len(color)-1)]
        #Determines how each color interacts with eachother
        self.relations = relations_table[self.color]
        #Position in "particles", since particles don't die, doesn't
        #eed to update
        self.index = len(particles)
    def render (self) :
        #Rendering, how it "renders" itself on screen
        #only graphical (duh?)
        turtle.goto(self.x,self.y)
        turtle.color(render_colors[self.color])
        turtle.pendown()
        turtle.fd(1);turtle.bk(1)
        turtle.penup()
    def routine (self) :
        #All of a particle's (important) behaviour
        other = self.relations['other']
        #Force that will be applied to velocity
        xForce, yForce = 0, 0
        count = 0
        #Loop over each particle to interact
        for p in old_particles :
            #Calculate distance to current target
            distanceToIt = distance([self.x, self.y],[p.x, p.y])
            d = distanceToIt[0]
            #Checks if he isn't interacting with himself
            if (self.index != count) and d>0 :
                #Physics ;-;
                xForce += distanceToIt[1][0] * (normPlus(self.x, p.x) * (force(d, self.relations[p.color], other[1], other[2], other[3], other[4]))) / (d * world['dist_decay'])
                yForce += distanceToIt[1][1] * (normPlus(self.y, p.y) * (force(d, self.relations[p.color], other[1], other[2], other[3], other[4]))) / (d * world['dist_decay'])
            count += 1
        #Adding force to velocity, and subtracting friction
        self.velX = self.velX*other[0] + (xForce * world['force_mult'])
        self.velY = self.velY*other[0] + (yForce * world['force_mult'])
        #What to do if a particle hits the border
        if not world['screen_wrap'] : #Just Collide
            self.x += self.velX
            self.y += self.velY
            if abs(self.x) > 300 :
                self.x = 300 * (self.x/abs(self.x))
                self.velX *= -1
            if abs(self.y) > 300 :
                self.y =  300 * (self.y/abs(self.y))
                self.velY *= -1
        else : #Wrap Around Screen
            self.x += self.velX
            self.y += self.velY
            if abs(self.x) > 300 :
                if (self.x//300)%2 == 1 :
                    self.x -= (600 * ( self.x//300 ))
                else :
                    self.x -= (600 * ( self.x//450 ))
                #self.x -= (300*( (self.x * numTo0(self.x)) // 300 )) * numTo0(self.x)
            if abs(self.y) > 300 :
                if (self.y//300)%2 == 1 :
                    self.y -= (600 * ( self.y//300 ))
                else :
                    self.y -= (600 * ( self.y//450 ))
                #self.y -= (300*( (self.y * numTo0(self.y)) // 300 )) * numTo0(self.y)
        #Calls the "render()" method
        self.render()
''''''
# Simulation
''''''
if saveFile == 'pps' :
    turtle.title('PPS/'+loadFrom)
else :
    turtle.title('PPS/'+saveFile)
turtle.bgcolor('black')
turtle.tracer(0, 0)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(world['pen_thickness'])

#generate particles
particles = []
for i in range(0,world['particles']) :
    particles.append(particle(random(-299,299),random(-299,299)))
#render screen, uses particle.render, not particle.routine()
drawTheLine()
for p in particles :
    p.render()
turtle.update()
wait(1)
desired_fps = world['desired_fps']
#desired_fps = int(turtle.textinput('Target FPS', 'Enter Target FPS.'))
#Main Loop (For Testing)
while LOOP :
    #for timing how long each cycle took
    start = time.time()
    #clear screen
    turtle.clear()
    #draws a dot at center
    drawTheLine()
    #cycles through each particle
    old_particles = particles
    for step in range(0,max(1,round(average_fps* (1/desired_fps) ))) :
        for P in particles :
            P.routine()
    turtle.update()
    delay = time.time()-start
    #more timing related stuff
    tPrint('FPS '+str( round(average_fps*100)/100 ) + ', or '+str(math.floor(delay*100000)/100)+'ms',(10,5))
    average_fps = (average_fps* ( 1/(tick+1) ) ) + ((1/delay)* ( 1-(1/(tick+1)) ) )
    tick += 1

writeToLog('Log Entry :\n   Average FPS '+str( round(average_fpsA*100)/100 ))
print(len(particles))
print('Average FPS '+str( math.floor(average_fps) ) + ', or '+str(math.floor((1/average_fps)*100000)/100)+'ms')

wait(1)
turtle.textinput('Simulation Done','Press [Enter] to Close.')
''''''
# Dev Comments
''''''
#Developed by
'''
The only, the real, the Sharp-Shark.
'''
#Currently in Development
'''
Save System.
'''
#Settings File Example Below
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
                          'yel':-2,
                          'gre':-1,
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
                          'blu':-1,
                          'pur':0,
                          'other':[0.9, 30, 10, 3, 1]},
                   'blu':{'red':1,
                          'yel':0,
                          'gre':1,
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
         'force_cont':6}

if not PPS :
    original = 'default'
    print('[FILE ../PPS.py]\nsaveFile = "saves/'+original+'_clone.py"\n#'+open('../PPS.py','r').read()+'\n[FILE END]')
    exec('saveFile = "saves/'+original+'_clone.py"\n#'+open('../PPS.py','r').read())

'''
