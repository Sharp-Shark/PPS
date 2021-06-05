saveFile = 'none'
''''''
# Imports
''''''
from random import randint as random
import turtle
import time
import math
canvas = turtle.getcanvas()
wait = time.sleep
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
else :
    print('Running from Settings')

LOOP = True #Continue Main Loop
count = 0
particles = [] #All particles are stored here
tick = 0 #How many iterations have passed
average_fpsA = 0 #P for Accuracy
average_fpsS = 0 #S for Speed
''''''
# Objects
''''''
def normPlus (x,y) : #Normalize and A Bit More
    magged = mag(x,y)
    return care_div(x, magged) - care_div(y, magged)

def norm (x,y) : #Normalize
    magged = mag(x,y)
    return [x/magged, y/magged]

def mag (x,y) : #Magnitude
    return math.sqrt(x * x + y * y)

def care_div (a,b) : # careful division
    if a==0 or b==0 :
        return 0
    else :
        return a/b

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

def distance (corA,corB) : #cor as in coords
    return math.sqrt( (corA[0]-corB[0])**2 + (corA[1]-corB[1])**2 )

def force (distance,mult,strength=50,offset=100,window=2,shape=1) :
    return world['force_cont']/(distance**2) + (mult * max(1 / distance, strength - abs(distance*window*strength - offset*window)**shape))
#GRAPH TOOL FOR TESTING
if 1==0 :
    graph_scale = 20
    graph_zoom = 100
    results = []
    for loop in range(1,math.floor(1333/graph_scale)) :
        results.append(force(loop/graph_scale, -2, 10, 30, 3, 1))
    #turtle setup
    turtle.title('PPS - Primitive Particle System')
    turtle.bgcolor('black')
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(5)
    #graph
    counter=0
    turtle.setheading(0)
    turtle.clear()
    drawTheLine()
    for r in results :
        turtle.goto(counter*graph_scale-667,0)
        if counter == 0 :
            turtle.color('limegreen')
        elif r < 0 :
            if r > results[counter-1] :
                turtle.color('orange')
            elif r < results[counter-1] :
                turtle.color('red')
            else :
                turtle.color('orangered')
        elif r > 0 :
            if r > results[counter-1] :
                turtle.color('cyan')
            elif r < results[counter-1] :
                turtle.color('blue')
            else :
                turtle.color('royalblue')
        else :
            turtle.color('purple')
        turtle.setheading(0)
        turtle.goto(counter*graph_scale-667,r*3)
        turtle.pendown()
        if counter < len(results)-1 :
            turtle.goto((counter+1)*graph_scale-667,(results[counter+1])*3)
        turtle.penup()
        if counter%5==0 :
            tPrint(range(1,math.floor(1333/graph_scale))[counter],(counter*graph_scale-657,Max(20,r*3+20)),6)
            tPrint(round(r),(counter*graph_scale-657,Max(10,r*3+10)),6)
            turtle.pensize(1)
            turtle.color('white')
            turtle.goto(counter*graph_scale-667,1000)
            turtle.pendown()
            turtle.goto(counter*graph_scale-667,-1000)
            turtle.penup()
            turtle.pensize(5)
        counter += 1
    turtle.update()
    print('DONE')
    turtle.done()
#GRAPH TOOL FOR TESTING

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
        for p in particles :
            #Calculate distance to current target
            #d = distance([self.x, p.x],[self.y, p.y])
            d = math.sqrt( (self.x - p.x)**2 + (self.y - p.y)**2 )
            #Checks if he isn't interacting with himself
            if (self.index != count) and d!=0.0 :
                #Physics ;-;
                if d>0 :
                    self.velX *= -1
                    self.velY *= -1
                    p.velX *= -1
                    p.velY *= -1
                    xForce += (normPlus(self.x, p.x) * (force(d, self.relations[p.color], other[1], other[2], other[3], other[4]))) / (d * world['dist_decay'])
                    yForce += (normPlus(self.y, p.y) * (force(d, self.relations[p.color], other[1], other[2], other[3], other[4]))) / (d * world['dist_decay'])
            count += 1
        #Adding force to velocity, and subtracting friction 
        self.velX = self.velX*other[0] + (xForce * world['force_mult'])
        self.velY = self.velY*other[0] + (yForce * world['force_mult'])
        self.x += self.velX
        self.y += self.velY
        #What to do if a particle hits the border
        if abs(self.x) > 300 :
            self.x = 300 * (self.x/abs(self.x))
            self.velX *= -1
        if abs(self.y) > 300 :
            self.y =  300 * (self.y/abs(self.y))
            self.velY *= -1
        #Calls the "render()" method
        self.render()
''''''
# Pre-Loop
''''''
turtle.title('PPS - Primitive Particle System')
turtle.bgcolor('black')
turtle.tracer(0, 0)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(10)

#generate particles
for i in range(0,50) :
    particles.append(particle(random(-150,150),random(-150,150)))
#render screen, uses particle.render, not particle.routine()
drawTheLine()
for p in particles :
    p.render()
turtle.update()
wait(1)
#Main Loop (For Testing)
for i in range(0,50000) :
    #for timing how long each cycle took
    start = time.time()
    #clear screen
    turtle.clear()
    #draws a dot at center
    drawTheLine()
    #cycles through each particle
    for P in particles :
        P.routine()
    turtle.update()
    delay = time.time()-start
    #more timing related stuff
    tPrint('FPS '+str( math.floor( 1/delay ) ) + ', or '+str(math.floor(delay*100000)/100)+'ms',(10,5))
    #print('FPS '+str( math.floor( 1/delay ) ) + ', or '+str(math.floor(delay*100000)/100)+'ms')
    average_fpsA = (average_fpsA* ( 1/(tick+1) ) ) + ((1/delay)* ( 1-(1/(tick+1)) ) )
    average_fpsS = (average_fpsS* 0.9 ) + ((1/delay)* 0.1 )
    if average_fpsS > 35 and tick>100 and tick%10==0 :
        particles.append(particle(random(-150,150),random(-150,150)))
    tick += 1
''''''
# Main Loop
''''''
while LOOP :
    LOOP = False

print('Average FPS (A) '+str( math.floor(average_fpsA) ) + ', or '+str(math.floor((1/average_fpsA)*100000)/100)+'ms')
print('Average FPS (S) '+str( math.floor(average_fpsS) ) + ', or '+str(math.floor((1/average_fpsS)*100000)/100)+'ms')

wait(1)
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
