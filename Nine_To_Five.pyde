'''
Nine-To-Five
by Tiffany Liang

Nine-To-Five is an interactive story game that follows the usual (or unusual) day of an
average office worker. A blend of text and images are used to immerse players in the
pixelated world that the office worker has come to inhabit. The game explores themes of 
memory and fantasy in a modern-day context.
'''

dialogue_option = 0
f_changed = 0
item = ""

def setup():
    size(700, 700)
    pixelDensity(2)
    global pics
    pics = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
    for i in range(len(pics)):
        pics[i] = loadImage("./pics/" + str(i) + ".png")
    global title_font
    global text_font
    title_font = createFont("ka1.ttf", 60)
    text_font = createFont("advanced_pixel-7.ttf", 50)
    fill(0)
    textAlign(CENTER)
    change_scene(title)

def title():
    image(pics[0], 0, 0)
    textFont(title_font)
    text("Nine-to-Five", width/2, 200)
    textFont(text_font)
    text("Press to Start", width/2, height/2+2*pow(-1,frameCount/5))
    textSize(40)
    if click():
        change_scene(scene2)

def scene2():
    image(pics[1], 0, 0)
    if has_elapsed(10):
        change_scene(scene3)
    
def scene3():
    image(pics[2], 0, 0)
    textAlign(LEFT)
    textLeading(25)
    global dialogue_option, f_changed
    if has_elapsed(15):
        if dialogue_option == 0:
            drawTextBox(20, 200)
            text(".......", 40, 60)
        elif dialogue_option == 1:
            drawTextBox(20, 200)
            text("Meeting at 10... Finish up that progress report...\nEmail Tim... ", 40, 60)
        elif dialogue_option == 2:
            drawTextBox(20, 200)
            text("*sigh* Looks like it's going to be another great \nday.", 40, 60)
        elif dialogue_option == 3:
            image(pics[3], 0, 0)
            if (frameCount - f_changed) > 5:
                dialogue_option += 1
        elif dialogue_option == 4:
            image(pics[2], 0, 0)
            drawTextBox(20, 200)
            text("Huh? What's this?...", 40, 60)
        if click():
            dialogue_option += 1
            f_changed = frameCount
            if dialogue_option == 5:
                dialogue_option = 0
                change_scene(scene4)
       
def scene4():
    image(pics[4], 0, 0)
    global f_changed
    if has_elapsed(17):
        drawTextBox(480, 200)
        text("What should I do?", 40, 520)
        text("> open the message", 60, 580)
        text("> ignore it", 60, 620)
        yes_hotspot = 60, 550, textWidth("> open the message"), 30
        no_hotspot = 60, 590, textWidth("> ignore it"), 30
        if check_hotspot(no_hotspot):
            change_scene(scene5_office)
        if check_hotspot(yes_hotspot):
            f_changed = frameCount
            change_scene(scene5_portal)

def scene5_office():
    global dialogue_option
    image(pics[2], 0, 0)
    if click():
        dialogue_option += 1
    if dialogue_option == 0:
        drawTextBox(20, 200)
        text("It's too early to be reading emails. I'll just check \nit later.", 40, 60)
    elif dialogue_option == 1:
        drawTextBox(20, 200)
        text("Alright, guess I'll start on that report...", 40, 60)
    elif dialogue_option == 2:
        image(pics[48], 0, 0)
    elif dialogue_option == 3:
        image(pics[48], 0, 0)
        drawTextBox(480, 200)
        text("Caught up in the work day, you eventually forgot \nabout the message.", 40, 520)
    elif dialogue_option == 4:
        image(pics[48], 0, 0)
        drawTextBox(480, 200)
        text("You left work at 5 and never found out what the \nmessage said.", 40, 520)
    elif dialogue_option == 5:
        image(pics[48], 0, 0)
        drawTextBox(480, 200)
        text("You left work at 5 and never found out what the \nmessage said.", 40, 520)
        change_scene(end)

def scene5_portal():
    global dialogue_option, f_changed
    if (frameCount - f_changed) < 15:
        image(pics[5], 0, 0)
    elif 15 <= (frameCount - f_changed) < 25:
        image(pics[6], 0, 0)
        drawTextBox(480, 200)
        text("What the-", 40, 520)
    elif 25 <=(frameCount - f_changed) < 35:
        image(pics[7], 0, 0)
    elif (frameCount - f_changed) >= 35:
        image(pics[8], 0, 0)
    if (frameCount - f_changed) >= 45:
        drawTextBox(480, 200)
        text("AAAAAAAAAAAAAHHHHHHH!!!", 40, 520)
    if dialogue_option == 1:
        image(pics[9], 0, 0)
    elif dialogue_option == 2:
        image(pics[9], 0, 0)
        drawTextBox(480, 200)
        text("-AAAAAAAAAAAAAAHHHHHHHHHHHHHHH!!!!!!", 40, 520)
    elif dialogue_option == 3:
        image(pics[9], 0, 0)
        drawTextBox(480, 200)
        text(".............Woah. Where am I??", 40, 520)
    elif dialogue_option == 4:
        image(pics[9], 0, 0)
        drawTextBox(480, 200)
        text("It's so cold and dark. I wonder if this is what \nspace feels like.", 40, 520)
    elif dialogue_option == 5:
        image(pics[9], 0, 0)
        drawTextBox(480, 200)
        text("This must be some strange fever dream. How did \nI fall asleep at my desk?", 40, 520)
    elif dialogue_option == 6:
        image(pics[9], 0, 0)
        drawTextBox(480, 200)
        text("Wait, there's something in the distance!", 40, 520)
    elif dialogue_option == 7:
        image(pics[10], 0, 0)
        door_hotspot = width/2-75, height/2-110, 150, 200
    elif dialogue_option == 8:
        image(pics[11], 0, 0)
        enter_hotspot = 0, height-200, width, 200
    if click() and (frameCount - f_changed) >= 55 and dialogue_option < 7:
        dialogue_option += 1
    elif dialogue_option == 7 and check_hotspot(door_hotspot):
        dialogue_option += 1
    elif dialogue_option == 8 and check_hotspot(enter_hotspot):
        dialogue_option = 0
        f_changed = frameCount
        change_scene(scene6)
        
def scene6():
    global dialogue_option, f_changed
    image(pics[12], 0, 0)
    if dialogue_option == 0 and (frameCount - f_changed) > 20:
        dialogue_option += 1
    if dialogue_option == 1:
        drawTextBox(480, 200)
        text("Ok, I've officially lost it", 40, 520)
    elif dialogue_option == 2:
        drawTextBox(480, 200)
        text("At this rate, I'm going to miss all of my meetings!", 40, 520)
    elif dialogue_option == 3:
        drawTextBox(480, 200)
        text("The whole team's gonna think I'm a klutz!", 40, 520)
    elif dialogue_option == 4:
        drawTextBox(480, 200)
        text(".........", 40, 520)
    elif dialogue_option == 5:
        drawTextBox(480, 200)
        text("Well..... I guess they already think that.", 40, 520)
    elif dialogue_option == 6:
        drawTextBox(480, 200)
        text("And honestly, I could probably afford to skip them. \nIt's not like I pay any attention during them \nanyways.", 40, 520)
    elif dialogue_option == 7:
        drawTextBox(480, 200)
        text("Alright, enough dilly-dallying. Let's try to find a \nway out.", 40, 520)
    elif dialogue_option == 8:
        drawTextBox(480, 200)
        text("Where should I explore?", 40, 520)
        text("> continue down the path", 60, 580)
        text("> check out the mysterious pond", 60, 620)
        path_hotspot = 60, 550, textWidth("> continue down the path"), 30
        pond_hotspot = 60, 590, textWidth("> check out the mysterious pond"), 30
        if check_hotspot(path_hotspot):
            f_changed = frameCount
            dialogue_option = 0
            change_scene(scene7_path)
        if check_hotspot(pond_hotspot):
            f_changed = frameCount
            dialogue_option = 0
            change_scene(scene7_pond)
    if click() and dialogue_option > 0:
        dialogue_option += 1

def scene6_revisit():
    global dialogue_option
    image(pics[12], 0, 0)
    if click():
        dialogue_option += 1
    if dialogue_option == 1:
        drawTextBox(480, 200)
        text("That was.... interesting....", 40, 520)
    if dialogue_option == 2:
        drawTextBox(480, 200)
        text("Maybe I dodged a bullet. Who knows what could've \nhappened down there?", 40, 520)
    elif dialogue_option == 3:
        drawTextBox(480, 200)
        text("Looks like there's only one way to go now.", 40, 520)
    elif dialogue_option == 5:
        change_scene(scene7_path)
        dialogue_option = 0
        
def scene7_path():
    global dialogue_option, item
    if dialogue_option < 4 or 11 <= dialogue_option < 27:
        image(pics[22], 0, 0)
    elif dialogue_option >= 27:
        image(pics[26], 0, 0)
    elif dialogue_option >= 4:
        image(pics[23], 0, 0)
        
    if click() and dialogue_option != 24 and dialogue_option != 32 and dialogue_option != 40:
        dialogue_option += 1
    if dialogue_option == 1:
        drawTextBox(480, 200)
        text("Is that a BEAR?????", 40, 520)
    elif dialogue_option == 2:
        drawTextBox(480, 200)
        text("Oh god- IT'S GOING TO EAT ME ALIVE!", 40, 520)
    elif dialogue_option == 3:
        drawTextBox(480, 200)
        text("WHY IS IT STARING AT ME LIKE THAT???", 40, 520)
    elif dialogue_option == 5:
        drawTextBox(480, 200)
        text("Did it just react to what I was saying? It looks \nso pityful now..... It kinda reminds me of a child \nwhose candy was plucked right out of its hands.", 40, 520)
    elif dialogue_option == 6:
        drawTextBox(20, 200)
        text("???: Why are all you humans so mean?", 40, 60)
    elif dialogue_option == 7:
        drawTextBox(480, 200)
        text("......", 40, 520)
    elif dialogue_option == 8:
        drawTextBox(480, 200)
        text("DID THAT THING JUST TALK?????", 40, 520)
    elif dialogue_option == 9:
        drawTextBox(20, 200)
        text("???: I'm not a thing! I have a name you know!", 40, 60)
    elif dialogue_option == 10:
        drawTextBox(480, 200)
        text("Oh- I'm sorry. Excuse my bad manners. It's just \nthat this is my first time talking to a bear, you \nsee.", 40, 520)
    elif dialogue_option == 11:
        drawTextBox(20, 200)
        text("???: Oh! Of course, I understand it can be quite \nshocking.", 40, 60)
    elif dialogue_option == 12:
        drawTextBox(20, 200)
        text("Bella: My name is Bella! What's yours?", 40, 60)
    elif dialogue_option == 13:
        drawTextBox(480, 200)
        text("My name is xxxx.", 40, 520)
    elif dialogue_option == 14:
        drawTextBox(20, 200)
        text("Bella: Nice to meet you xxxx! So what are you \ndoing all the way out here? I haven't seen a \nhuman in ages!", 40, 60)
    elif dialogue_option == 15:
        drawTextBox(480, 200)
        text("I'm really not too sure myself.... I got sucked into \nmy computer screen and then I opened a door and \nnow I'm here. None of this makes any sense to me.", 40, 520)
    elif dialogue_option == 16:
        drawTextBox(20, 200)
        text("Bella: Nothing makes sense to me either! But if \nthere's none thing I do know, it's that gummy \nbears are pretty tasty and eating a pawful of \nthem while watching beautiful sunsets with my \nfriends makes me very happy!", 40, 60)
    elif dialogue_option == 17:
        drawTextBox(480, 200)
        text("I wish I had that kind of excitement in my life...", 40, 520)
    elif dialogue_option == 18:
        drawTextBox(20, 200)
        text("Bella: I'm sure you do! Maybe you've just forgotten.", 40, 60)
    elif dialogue_option == 19:
        drawTextBox(480, 200)
        text("Hm. Yeah.", 40, 520)
    elif dialogue_option == 20:
        drawTextBox(20, 200)
        text("Bella: But fret not! I can help get you back to \nyour computer door as long as you help me out \nwith something first.", 40, 60)
    elif dialogue_option == 21:
        drawTextBox(480, 200)
        text("I'll do anything.", 40, 520)
    elif dialogue_option == 22:
        drawTextBox(20, 200)
        text("Bella: Great! I've been having toothaches for the \npast couple of days. Could you take a look?", 40, 60)
    elif dialogue_option == 23:
        drawTextBox(480, 200)
        text("Uhh. Sure, I guess.", 40, 520)
    elif dialogue_option == 24:
        image(pics[24], 0, 0)
        tooth_hotspot = width/2+140, height/2+35, 30, 30
        if check_hotspot(tooth_hotspot):
            dialogue_option = 25
    elif dialogue_option == 25:
        image(pics[25], 0, 0)
    elif dialogue_option == 26:
        image(pics[25], 0, 0)
        drawTextBox(480, 200)
        text("*You successfully extracted the tooth! Upon further \ninspection, you realize that it's a key*", 40, 520)
        item = "key"
    elif dialogue_option == 27:
        image(pics[26], 0, 0)
        drawTextBox(20, 200)
        text("Bella: Youch! How did that get in there?", 40, 60)
    elif dialogue_option == 28:
        drawTextBox(480, 200)
        text("Do you just eat keys for fun?", 40, 520)
    elif dialogue_option == 29:
        drawTextBox(20, 200)
        text("Bella: Of course not! Maybe it was hidden in that \nbag of fruit snacks...", 40, 60)
    elif dialogue_option == 30:
        drawTextBox(20, 200)
        text("Bella: I guess that means I have to fulfill my end \nof the deal. Follow me!", 40, 60)
    elif dialogue_option == 31:
        image(pics[27], 0, 0)
        drawTextBox(480, 200)
        text("Bella: Here it is!", 40, 520)
    elif dialogue_option == 32:
        image(pics[27], 0, 0)
        door_hotspot = 140, 140, 120, 220
        if check_hotspot(door_hotspot):
            dialogue_option = 33
    elif dialogue_option == 33:
        image(pics[28], 0, 0)
    elif dialogue_option == 34:
        image(pics[28], 0, 0)
        drawTextBox(480, 200)
        text("I guess this is it.", 40, 520)
    elif dialogue_option == 35:
        image(pics[28], 0, 0)
        drawTextBox(20, 200)
        text("Bella: It's been fun, xxxx!", 40, 60)
    elif dialogue_option == 36:
        image(pics[28], 0, 0)
        drawTextBox(480, 200)
        text("Will I ever see you again?", 40, 520)
    elif dialogue_option == 37:
        image(pics[28], 0, 0)
        drawTextBox(20, 200)
        text("Bella: That's up to you.", 40, 60)
    elif dialogue_option == 38:
        image(pics[28], 0, 0)
        drawTextBox(480, 200)
        text("Maybe I will then. I'll see you around.", 40, 520)
    elif dialogue_option == 39:
        image(pics[28], 0, 0)
        drawTextBox(20, 200)
        text("Bella: Goodbye!", 40, 60)
    elif dialogue_option == 40:
        image(pics[29], 0, 0)
        door_hotspot = width/2-120, 50, 260, 500
        if check_hotspot(door_hotspot):
            change_scene(scene9_portal)
            dialogue_option = 0

def scene7_pond():
    global dialogue_option, f_changed
    if dialogue_option < 7:
        image(pics[13], 0, 0)
    elif dialogue_option >= 7:
        image(pics[15], 0, 0)
    if click() and dialogue_option != 25 and dialogue_option != 26 and dialogue_option != 6 and dialogue_option != 30:
        if dialogue_option == 5:
            f_changed = frameCount
        dialogue_option += 1
    if dialogue_option == 1:
        drawTextBox(20, 200)
        text("Wow. This pond is mysterious alright.", 40, 60)
    elif dialogue_option == 2:
        drawTextBox(20, 200)
        text("I'm filled with intrigue.", 40, 60)
    elif dialogue_option == 3:
        drawTextBox(20, 200)
        text("Oh god- did my hair look like that the entire \nmorning?", 40, 60)
    elif dialogue_option == 4:
        drawTextBox(20, 200)
        text(".........", 40, 60)
    elif dialogue_option == 5:
        drawTextBox(20, 200)
        text("Ok, that was fun. Guess I'll walk around a little \nmore.", 40, 60)
    elif dialogue_option == 6:
        if 10 < (frameCount - f_changed) <= 15:
            image(pics[14], 0, 0)
        elif 15 < (frameCount - f_changed):
            image(pics[15], 0, 0)
        if (frameCount - f_changed) >= 25:
            dialogue_option += 1
    elif dialogue_option == 7:
        drawTextBox(20, 200)
        text("Huh. What a strange looking trout. Why's it looking \nat me like that?", 40, 60)
    elif dialogue_option == 8:
        drawTextBox(480, 200)
        text("???: Well that's not very nice. blub.", 40, 520)
    elif dialogue_option == 9:
        drawTextBox(20, 200)
        text("AAAAGH! YOU TALK?", 40, 60)
    elif dialogue_option == 10:
        drawTextBox(480, 200)
        text("???: Why wouldn't I? blub. How else am I supposed \nto communicate? blub.", 40, 520)
    elif dialogue_option == 11:
        drawTextBox(20, 200)
        text(".......You make a fair point, trout.", 40, 60)
    elif dialogue_option == 12:
        drawTextBox(480, 200)
        text("Henry: Thanks, but I'm not a trout. I'm a carp. \nYou can call me Henry. blub.", 40, 520)
    elif dialogue_option == 13:
        drawTextBox(20, 200)
        text("Ok, nice to meet you Henry.", 40, 60)
    elif dialogue_option == 14:
        drawTextBox(480, 200)
        text("Henry: Likewise! Anyways, what brings you here? \nWe don't get a lot of foot traffic these days. \nblub.", 40, 520)
    elif dialogue_option == 15:
        drawTextBox(20, 200)
        text("Well..... That's the problem. I got sucked into my \ncomputer screen and then I opened a door and now \nI'm here. None of this makes any sense. And where \neven is \"here\"?", 40, 60)
    elif dialogue_option == 16:
        drawTextBox(480, 200)
        text("Henry: You really don't recognize it? blub.", 40, 520)
    elif dialogue_option == 17:
        drawTextBox(20, 200)
        text("Am I supposed to?", 40, 60)
    elif dialogue_option == 18:
        drawTextBox(480, 200)
        text("Henry: I guess not, blub. People change and \nmemories fade whether we like it or not. So I \ndon't blame you. blub.", 40, 520)
    elif dialogue_option == 19:
        drawTextBox(20, 200)
        text("I don't think I'm that different from who I used \nto be though.", 40, 60)
    elif dialogue_option == 20:
        drawTextBox(480, 200)
        text("Henry: You'd be surprised. blub.", 40, 520)
    elif dialogue_option == 21:
        drawTextBox(20, 200)
        text("Can you atleast get me out of here? I have a lot \nof things I need to do today. I can't spend my \nentire lunch break talking to a trout.", 40, 60)
    elif dialogue_option == 22:
        drawTextBox(480, 200)
        text("Henry: Sure thing! You just have to jump in here \nwith me. blub.", 40, 520)
    elif dialogue_option == 23:
        drawTextBox(20, 200)
        text("Are you crazy? I'll drown!", 40, 60)
    elif dialogue_option == 24:
        drawTextBox(480, 200)
        text("Henry: You'll be fine, trust me! blub!", 40, 520)
    elif dialogue_option == 25:
        drawTextBox(20, 200)
        text("Is he being serious? I can't even swim!", 40, 60)
        text("> I trust him", 60, 120)
        text("> I don't trust him", 60, 160)
        yes_hotspot = 60, 90, textWidth("> I trust him"), 30
        no_hotspot = 60, 130, textWidth("> I don't trust him"), 30
        if check_hotspot(yes_hotspot):
            dialogue_option = 26
        if check_hotspot(no_hotspot):
            dialogue_option = 28
    elif dialogue_option == 26:
        drawTextBox(20, 200)
        text("Fine. Here goes nothing...", 40, 60)
        continue_hotspot = 0, 0, width, height
        if check_hotspot(continue_hotspot):
            change_scene(scene8_pond)
            dialogue_option = 0
    elif dialogue_option == 28:
        drawTextBox(20, 200)
        text("I'm sorry Henry, but I can't do it. You're a talking \nfish for crying out loud!", 40, 60)
    elif dialogue_option == 29:
        drawTextBox(480, 200)
        text("Henry: I expected as much. blub. What's your plan \nnow?", 40, 520)
    elif dialogue_option == 30:
        drawTextBox(20, 200)
        text("Uhhh....", 40, 60)
        text("> Actually I change my mind", 60, 120)
        text("> I'll find another way out", 60, 160)
        yes_hotspot = 60, 90, textWidth("> Actually I change my mind"), 30
        no_hotspot = 60, 130, textWidth("> I'll find another way out"), 30
        if check_hotspot(yes_hotspot):
            dialogue_option = 26
        if check_hotspot(no_hotspot):
            dialogue_option = 31
    elif dialogue_option == 31:
        drawTextBox(20, 200)
        text("I'll find another way out. I hate to leave you \nhanging, but I'm starting to get sick of this place.", 40, 60)
    elif dialogue_option == 32:
        drawTextBox(20, 200)
        text("I hope you live a long and meaningful life Henry.", 40, 60)
    elif dialogue_option == 33:
        drawTextBox(480, 200)
        text("Henry: Thank you! Don't worry about me though, I'm \nas content as a little ol' carp can be. blub.", 40, 520)
    elif dialogue_option == 34:
        drawTextBox(20, 200)
        text("Must be nice..... Well, I'll see you around.", 40, 60)
    elif dialogue_option == 35:
        drawTextBox(480, 200)
        text("Henry: So long! blub.", 40, 520)
    elif dialogue_option == 36:
        drawTextBox(480, 200)
        text("Henry: So long! blub.", 40, 520)
        change_scene(scene6_revisit)
        dialogue_option = 0
        
def scene8_pond():
    textAlign(LEFT)
    textLeading(25)
    global dialogue_option, item
    if click() and dialogue_option != 5 and dialogue_option != 9 and dialogue_option != 22:
        dialogue_option += 1
    if dialogue_option >= 14:
        image(pics[20], 0, 0)
    elif dialogue_option >= 12:
        image(pics[19], 0, 0)
    elif dialogue_option >= 6:
        image(pics[18], 0, 0)
    else:
        image(pics[16], 0, 0)
    if dialogue_option == 1:
        drawTextBox(20, 200)
        text("Woah! How is this possible??", 40, 60)
    elif dialogue_option == 2:
        drawTextBox(480, 200)
        text("Henry: It's the power of imagination. blub.", 40, 520)
    elif dialogue_option == 3:
        drawTextBox(20, 200)
        text("Now what's that supposed to mean?", 40, 60)
    elif dialogue_option == 4:
        drawTextBox(480, 200)
        text("Henry: Nothing... Ok now that you're down here, let \nme show you something. blub.", 40, 520)
    elif dialogue_option == 5:
        image(pics[17], 0, 0)
        chest_hotspot = width/2-50, height/2-100, 175, 140
        if check_hotspot(chest_hotspot):
            dialogue_option += 1
    elif dialogue_option == 7:
        drawTextBox(20, 200)
        text("Aw man. This is some lame pirate's booty.", 40, 60)
    elif dialogue_option == 8:
        drawTextBox(480, 200)
        text("Henry: You should take one! You never know when \nyou're gonna need a tool like this", 40, 520)
    elif dialogue_option == 9:
        pencil_hotspot = width/2-120, height/2, 100, 210
        brush_hotspot = width/2+20, height/2, 100, 220
        if check_hotspot(pencil_hotspot):
            dialogue_option += 1
            item = "pencil"
        if check_hotspot(brush_hotspot):
            dialogue_option += 1
            item = "brush"
    elif dialogue_option == 10:
        drawTextBox(20, 200)
        text("I think I'll take this " + item + ". It's been a while \nsince I've made any art though.", 40, 60)
    elif dialogue_option == 11:
        drawTextBox(480, 200)
        text("Henry: Perfect. blub. Even more of a reason to \nhold onto it!", 40, 520)
    elif dialogue_option == 12:
        drawTextBox(480, 200)
        text("Thanks, I guess. I don't know why or when I would \nneed this but I'll keep it for now.", 40, 520)
    elif dialogue_option == 13:
        drawTextBox(480, 200)
        text("Henry: You do that. Let me show you the way out. \nblub.", 40, 520)
    elif dialogue_option == 15:
        drawTextBox(480, 200)
        text("Henry: Voila. blub.", 40, 520)
    elif dialogue_option == 16:
        drawTextBox(20, 200)
        text("I guess this is it then.", 40, 60)
    elif dialogue_option == 17:
        drawTextBox(480, 200)
        text("Henry: It's been a pleasure. blub.", 40, 520)
    elif dialogue_option == 18:
        drawTextBox(20, 200)
        text("Will I ever see you again?", 40, 60)
    elif dialogue_option == 19:
        drawTextBox(480, 200)
        text("Henry: That's up to you. blub.", 40, 520)
    elif dialogue_option == 20:
        drawTextBox(20, 200)
        text("Maybe I will then. I'll see you around.", 40, 60)
    elif dialogue_option == 21:
        drawTextBox(20, 200)
        text("Henry: Goodbye! blub!", 40, 60)
    elif dialogue_option == 22:
        image(pics[21], 0, 0)
        door_hotspot = width/2-110, 140, 260, 380
        if check_hotspot(door_hotspot):
            change_scene(scene9_portal)
            dialogue_option = 0
    
def scene9_portal():
    global dialogue_option
    image(pics[9], 0, 0)
    if click() and dialogue_option != 4:
        dialogue_option += 1
    if dialogue_option == 1:
        drawTextBox(480, 200)
        text("Yeesh. Not this again.", 40, 520)
    elif dialogue_option == 2:
        drawTextBox(480, 200)
        text("Looks like I'm finally going back home though.", 40, 520)
    elif dialogue_option == 3:
        drawTextBox(480, 200)
        text("Why do I feel weirdly bittersweet about that?....", 40, 520)
    elif dialogue_option == 4:
        image(pics[10], 0, 0)
        door_hotspot = width/2-75, height/2-110, 150, 200
        if check_hotspot(door_hotspot):
            change_scene(scene10)
            dialogue_option = 0
            
def scene10():
    global dialogue_option, item, f_changed
    image(pics[30], 0, 0)
    if has_elapsed(15):
        image(pics[35], 0, 0)
    elif has_elapsed(10):
        image(pics[31], 0, 0)
    if has_elapsed(15) and click():
        if dialogue_option == 12:
            dialogue_option = 10
        else:
            dialogue_option += 1
        print(dialogue_option)
    if dialogue_option == 1:
        drawTextBox(20, 200)
        text("So it really was a dream.....", 40, 60)
    elif dialogue_option == 3:
        drawTextBox(20, 200)
        text("There's something in my hand.", 40, 60)
    elif dialogue_option == 4:
        if item == "key":
            image(pics[32], 0, 0)
        elif item == "pencil":
            image(pics[33], 0, 0)
        elif item == "brush":
            image(pics[34], 0, 0)
    elif dialogue_option == 5:
        if item == "key":
            image(pics[36], 0, 0)
        elif item == "pencil":
            image(pics[37], 0, 0)
        elif item == "brush":
            image(pics[38], 0, 0)
    elif dialogue_option == 6:
        if item == "key":
            image(pics[39], 0, 0)
        elif item == "pencil":
            image(pics[40], 0, 0)
        elif item == "brush":
            image(pics[41], 0, 0)
    elif dialogue_option == 7:
        image(pics[42], 0, 0)
    elif dialogue_option == 8:
        image(pics[43], 0, 0)
        f_changed = frameCount
    elif dialogue_option == 9:
        if item == "key":
            image(pics[46], 0, 0)
            if frameCount-f_changed == 4:
                dialogue_option = 12
        elif item == "pencil":
            image(pics[44], 0, 0)
        elif item == "brush":
            image(pics[45], 0, 0)
    elif dialogue_option == 10:
        image(pics[35], 0, 0)
    elif dialogue_option == 11:
        change_scene(good_end)
    elif dialogue_option == 12:
        image(pics[47], 0, 0)

def good_end():
    if has_elapsed(15):
        image(pics[50], 0, 0)
        if click():
            change_scene(end)
    elif has_elapsed(10):
        image(pics[49], 0, 0)
    elif has_elapsed(5):
        image(pics[48], 0, 0)

def end():
    textAlign(CENTER)
    image(pics[51], 0, 0)
    textFont(title_font)
    text("The End", width/2, height/2 + 200)
        
        
def drawTextBox(y, h):
    strokeWeight(5)
    stroke(0)
    fill(255)
    rect(20, y, width-40, h)
    fill(0)
    
from nonlinearity_helper import *
