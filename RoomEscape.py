from bangtal import *

scene1 = Scene('Room1', 'Images/RoomEscape/배경-1.png')
scene2 = Scene('Room2', 'Images/RoomEscape/배경-2.png')

key = Object('Images/RoomEscape/열쇠.png')
key.locate(scene1,400,150)
key.show()
key.setScale(0.2)

Pig = Object('Images/RoomEscape/pig.png')    #새로운 png파일을 다운로드하여 화분대신 돼지를 배치하였다.
Pig.locate(scene1,350,150)
Pig.show()
Pig.setScale(0.3)

phone = Object('Images/RoomEscape/phone.png') #phone이라는 객체를 만들어 png파일을 이용하여 scene2에 배치하였다.
phone.locate(scene2,10,10)
phone.show()
phone.setScale(0.02)

timer1 = Timer(60) #timer객체를 사용하여 60초부터 카운트합니다.
timer1.start()

def key_onMouseAction(x, y, action):
    key.pick()

key.onMouseAction = key_onMouseAction


def phone_onMouseAction(x, y, action): #phone을 누르면 JAEHYUN이라는 숨겨진 비밀번호가 나온다.
    
    showMessage('JAEHYUN')


phone.onMouseAction = phone_onMouseAction

Pig.moved = False
def Pig_onMouseAction(x, y, action):
    if Pig.moved == False:

            if action == MouseAction.DRAG_LEFT:
                  Pig.locate(scene1,200,150)
                  Pig.moved = True
            elif action == MouseAction.DRAG_RIGHT:
                Pig.locate(scene1,450,150)
                Pig.moved = True
            elif action == MouseAction.DRAG_DOWN:
                Pig.locate(scene1,350,50)
                Pig.moved = True
            elif action == MouseAction.DRAG_UP:
                Pig.locate(scene1,350,250)
                Pig.moved = True

Pig.onMouseAction = Pig_onMouseAction


door1 = Object('Images/RoomEscape/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

door2 = Object('Images/RoomEscape/문-왼쪽-닫힘.png')
door2.locate(scene2, 350, 270)
door2.show()
door2.closed = True

door2 = Object('Images/RoomEscape/문-왼쪽-열림.png')
door2.locate(scene2, 350, 270)
door2.show()
door2.closed = False

door3 = Object('Images/RoomEscape/문-오른쪽-닫힘.png')
door3.locate(scene2, 900, 270)

door3.closed = True

keypad = Object('Images/RoomEscape/키패드.png')
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object('Images/RoomEscape/스위치.png')
switch.locate(scene2, 880, 400)
switch.show()
switch.lighted = True

switch2 = Object('Images/RoomEscape/스위치.png') #switch2객체를 만들어 스위치를 추가하였다.
switch2.locate(scene2, 880, 450)
switch2.show()
switch2.lighted = True

password = Object('Images/RoomEscape/암호.png')
password.locate(scene2,400,100)

def switch2_onMouseAction(x,y,action): #스위치2를 누르면 BANGTAL은 비밀번호가 아니였음을 알려준다.
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        
    else:
        scene2.setLight(0.4)
        showMessage('BANGTAL은 비밀번호가 아니야')

switch2.onMouseAction = switch2_onMouseAction

def switch_onMouseAction(x,y,action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password.hide()
    else:
        scene2.setLight(0.25)
        password.show()

switch.onMouseAction = switch_onMouseAction

door3locked = True

def keypad_onMouseAction(x,y,action):
    global door3 #전역변수를 사용하여 door3와 door3locked가 비밀번호를 맞추면 동작하도록 하였다.
    global door3locked
    showKeypad('JAEHYUN', door3)
    


keypad.onMouseAction = keypad_onMouseAction


def door3_onKeypad():
    global door3locked
    showMessage('문열림')
    door3.show()   #패스워드를 입력하면 열린 문이 등장합니다.
    door3locked = False
    door3.setImage('Images/RoomEscape/문-오른쪽-열림.png')

    showMessage('게임 종료')
    
    showTimer(timer1) #60초부터 게임 완료시 남은 시간을 표시해 줍니다.
    
door3.onKeypad = door3_onKeypad

def door2_onMouseAction(x,y,action):
    if door2.closed == False:
        scene1.enter()
    else:
        door2.setImage('Images/RoomEscape/문-왼쪽-열림.png')
        door2.closed = False
       
       
door2.onMouseAction = door2_onMouseAction





def door1_onMouseAction(x, y, action):
    if door1.closed == True:

        if key.inHand() == False:
            showMessage('열쇠없다')
        else:
            door1.setImage('Images/RoomEscape/문-오른쪽-열림.png')    
            door1.closed = False
    else:
        scene2.enter()
door1.onMouseAction = door1_onMouseAction

def door3_onMouseAction(x, y, action):
    global door3locked
    if door3locked == True:
        showMessage('문잠겨있어')

    else:
        door3.setImage('Images/RoomEscape/문-오른쪽-열림.png')   
       
        
        
door3.onMouseAction = door3_onMouseAction



startGame(scene1) 
