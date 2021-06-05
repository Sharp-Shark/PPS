''''''
#Imports
''''''

from random import randint as random
import turtle
import time
import math
canvas = turtle.getcanvas()
wait = time.sleep

''''''
#Needed Functions
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

''''''
#Make Graph
''''''

def makeGraph(color) :
    #color to make graph of
    try :
        other = relations_table[color]['other']
    except :
        print('Invalid Argument for makeGraph()!')
    #graph settings
    graph_scale = 20
    graph_zoom = 100
    results = []
    flip_value = relations_table[color][turtle.textinput('flip_value','Flip Value (string)\n<- ')]
    for loop in range(1,math.floor(1333/graph_scale)) :
        results.append(force(loop/graph_scale, flip_value, other[1], other[2], other[3], other[4]))
    #turtle setup
    turtle.title('Graph Maker')
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
    #turtle.done()

''''''
#Action
''''''

turtle.bgcolor('black')
turtle.tracer(0, 0)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(5)

turtle.title('Graph Maker')
tPrint('Graph Maker',(10,15))
tPrint('/quit to Close',(10,-15))

twindow = turtle.Screen()
twindow.screensize(1, 1)
twindow.setup(width=1.0, height=1.0, startx=None, starty=None)

loop = True

while loop :
    try :
        #Load Settings File
        inputed = turtle.textinput('loadFrom','File Name (string)\n<- ')
        if inputed in ('exit','quit','close','stop') :
            inputed = turtle.textinput('quit','Type in /quit to close the program.')
        if inputed == '/quit' :
            turtle.bye();loop=False
        elif inputed == '' :
            pass
        else :
            loadFrom = 'saves/'+inputed+'.py'
        exec('PPS = True\n#'+open(loadFrom,'r').read())
        print('[FILE '+loadFrom+']\n'+open(loadFrom,'r').read()+'\n[FILE END]')
        #Make Graph for Color
        try :
            makeGraph(turtle.textinput('color','Color to Graph (string)\n<- '))
        except :
            msg_content = 'Available colors :\n'
            for ac in available_colors :
                msg_content += ac+' '
            turtle.textinput('Msg', msg_content)
    except :
        turtle.textinput('Error', 'An error has occured!')
