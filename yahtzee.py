#
# Eren Kutay, 0032902490
# This program is to create a window allowing the user to
# roll dices, and play full Black-N-Goldtzee Game
# with Scorecard.
#

# set up the import statement to use graphics module.
from graphics import *

# set up the sleep import statement to use time module.
from time import sleep

# set up the randint import statement to use random module.
from random import randint

# define a function named diceWindow().
def diceWindow():

    # create a 700x400 Graphics window named "The Dice Window".
    graph_window = GraphWin('The Dice Window', 700, 400)
 
    # set background color of the window to yellow1.
    graph_window.setBackground(color_rgb(255, 212, 59))

    # create an image object in window which is the title of the game.
    title = Image(Point(350, 75), 'gameTitle.gif')

    # draw title.
    title.draw(graph_window)

    # create an italic text object below title("Your Current Dice").
    text_header = Text(Point(350, 130), 'YOUR CURRENT DICE')

    # set the size of text header.
    text_header.setSize(14)

    # set the style of text.
    text_header.setStyle('italic')

    # draw text header.
    text_header.draw(graph_window)

    # create a rectangle centered below the text object.
    rectangle_dice = Rectangle(Point(50,250), Point(650,150))

    # set rectangle color to yellow1.
    rectangle_dice.setFill(color_rgb(255, 212, 59))

    # draw score rectangle.
    rectangle_dice.draw(graph_window)

    # create rectangle for score value.
    score_rect = Rectangle(Point(200, 350), Point(500, 300))

    # set the color of score rectangle.
    score_rect.setFill(color_rgb(255, 212, 59))

    # draw score rectangle.
    score_rect.draw(graph_window)

    # get the center of the score values rectangle.
    score_center = score_rect.getCenter()

    # set a (bold) text("Score: 0") object in the center of that rectangle.
    score_text = Text(score_center, 'Want to play a game?')

    # set score text style.
    score_text.setStyle('bold')

    # draw the score text.
    score_text.draw(graph_window)
    
    # create (red-filled) rectangle object in the lower right corner("EXIT").
    exit_rect = Rectangle(Point(550, 375), Point(675, 345))

    # set the color of exit rectangle.
    exit_rect.setFill('red')

    # draw exit rectangle.
    exit_rect.draw(graph_window)

    # get the center of an exit rectangle.
    exit_center = exit_rect.getCenter()

    # create a (white) and (bold) text object("EXIT") in the center of the red rectangle.
    exit_text = Text(exit_center, 'EXIT')

    # set the size of exit text.
    exit_text.setSize(14)

    # set the color of exit text.
    exit_text.setFill('white')

    # set the size of exit text.
    exit_text.setStyle('bold')

    # draw the exit text.
    exit_text.draw(graph_window)

    # create a text object above the (red) rectangle("Click here to:").
    exit_command = Text(Point(613, 335),'Click here to:')

    # set the style of exit command.
    exit_command.setStyle('italic')

    # draw exit command.
    exit_command.draw(graph_window)

    # create (black-filled) rectangle object in the lower right corner("PLAY").
    play_rect = Rectangle(Point(25, 375), Point(150, 345))

    # set the color of play rectangle.
    play_rect.setFill('green')

    # draw play rectangle.
    play_rect.draw(graph_window)

    # get the center of play rectangle.
    play_center = play_rect.getCenter()
    
    # create a (yellow) and (bold) text object("PLAY") in the center of the red rectangle.
    play_text = Text(play_center, 'PLAY')

    # set the color of the play text.
    play_text.setFill(color_rgb(255, 212, 59))

    # set the size of play text.
    play_text.setSize(14)

    # set the style of play text.
    play_text.setStyle('bold')
    
    # draw play text.
    play_text.draw(graph_window)
    
    # create a text object above the black rectangle("Click here to:").
    roll_command = Text(Point(87, 335),'Click here to:')

    # draw roll command.
    roll_command.draw(graph_window)

    # circle initial 1 created.
    circle1 = Circle(Point(85,290), 20)

    # set the color of circle initial 1.
    circle1.setFill("green")
    
    # draw circle initial 1.
    circle1.draw(graph_window)

    # circle initial 2 created.
    circle2 = Circle(Point(610,290), 20)

    # set the color of circle initial 2.
    circle2.setFill("red")

    # draw circle initial 2.
    circle2.draw(graph_window)

    # return it to dice window, the red rectangle("EXIT"), the black rectangle("ROLL"), and Score text.
    return graph_window, exit_rect, play_rect, play_text, score_text, circle1, circle2

# create a function that creates Black-N-Goldtzee Scorecard window.
def ScorecardWindow():

    # create a graphics window for scorecard.
    scr_win = GraphWin("GAME IN PROCESS", 400, 600)

    # set background color.
    scr_win.setBackground("black")

    # create title.
    scr_title = Text(Point(200, 40), "Black-N-Goldtzee Scorecard")

    # set the color of the title.
    scr_title.setFill(color_rgb(252, 234, 0))

    # set the size of the text title.
    scr_title.setSize(21)

    # set face of text title.
    scr_title.setFace("helvetica")

    # set style of text.
    scr_title.setStyle("bold")

    # draw text title.
    scr_title.draw(scr_win)

    # create column headers.
    round_column = Text(Point(75, 90), "ROUND")

    # set face of text column.
    round_column.setFill("white")

    # set the size of the text column.
    round_column.setSize(18)

    # set face of text column.
    round_column.setFace("helvetica")

    # set style of text column.
    round_column.setStyle("bold")

    # draw text column.
    round_column.draw(scr_win)

    # create column headers.
    score_column = Text(Point(325, 90), "SCORE")

    # set face of text column.
    score_column.setFill("white")

    # set the size of the text column.
    score_column.setSize(20)

    # set face of text column.
    score_column.setFace("helvetica")

    # set style of text column.
    score_column.setStyle("bold")

    # draw text column.
    score_column.draw(scr_win)
    
    # create score entry box.
    total_entry = Entry(Point(300,565), 10)

    # set total score entry box size.
    total_entry.setSize(20)

    # set the color of total box entry
    total_entry.setFill("white")

    # draw total box entry.
    total_entry.draw(scr_win)

    # assign initial score value.
    initial = "              {0:>3}".format(0)

    # set text 0 to total entry.
    total_entry.setText(initial)

    # create score text.
    scr_txt = Text(Point(110, 565),"TOTAL SCORE:")

    # set style text score.
    scr_txt.setSize(21)

    # set the color of score txt.
    scr_txt.setFill("white")

    # set face of text score.
    scr_txt.setFace("courier")

    # set style text score.
    scr_txt.setStyle("bold")

    # draw the score text.
    scr_txt.draw(scr_win)

    # create a column line.
    border_line = Line(Point(0,120), Point(400, 120))

    # seth width of line.
    border_line.setWidth(5)

    # set the color of border_line.
    border_line.setFill(color_rgb(252, 234, 0))

    # draw border line.
    border_line.draw(scr_win)

    # create a column line.
    line1 = Line(Point(0,0), Point(400, 0))

    # seth width of line.
    line1.setWidth(5)

    # set the color of border_line.
    line1.setFill(color_rgb(252, 234, 0))

    # draw line 1.
    line1.draw(scr_win)

    # create a column line.
    line2 = Line(Point(0,0), Point(0, 600))

    # seth width of line.
    line2.setWidth(5)

    # set the color of border_line.
    line2.setFill(color_rgb(252, 234, 0))

    # draw the line.
    line2.draw(scr_win)

    # create a column line.
    line3 = Line(Point(0,600), Point(400, 600))

    # seth width of line.
    line3.setWidth(5)
    
    # set the color of border_line.
    line3.setFill(color_rgb(252, 234, 0))

    # draw line 3.
    line3.draw(scr_win)

    # create a column line.
    line4 = Line(Point(400,0), Point(400, 600))

    # seth width of line.
    line4.setWidth(5)

    # set the color of border_line.
    line4.setFill(color_rgb(252, 234, 0))

    # draw line.
    line4.draw(scr_win)

    # return it to score window and entry box objects.
    return scr_win, total_entry


# write an additional function to check if the mouse click in the (red) rectangle.
def isClickedR(mouse, rect):

    # if mouse is not clicked.
    if not mouse:
        
        # return it to False if not clicked.
        return False

    # get the points of mouse click.
    mx, my = mouse.getX(), mouse.getY()

    # get the one corner point of the exit rectangle.
    rx1, ry1 = rect.getP1().getX(), rect.getP1().getY()

    # get the other corner point of the exit rectangle.
    rx2, ry2 = rect.getP2().getX(), rect.getP2().getY()

    # return True if mouse click is in Red Rectangle False if not
    return (rx1 < mx < rx2) and (ry2 < my < ry1)

# define the rollDice() function that accepts two(2) list arguments.
def rollDice(graph_window, value_list, image_list):

    # if image and value list already contain values(True).
    if value_list and image_list:

        # remove the integers in dice value list with del function.
        del value_list[:]

        # undraw each dice image in image list with for loop.
        for dice in image_list:

            # undraw dices in image_list.
            dice.undraw()

        # delete the image list.
        del image_list[:]

    # use for loop to add 6 random values to list.
    for value in range(6):

        # generate six random integers between 1-6 and append it to value list.
        value_list.append(randint(1,6))

    # initialize x coordinage of the images.
    x = 100
        
    # for loop to create iamges based on the value list integers.
    for integer in value_list:

        # create image based on each integer.
        dice_image = Image(Point(x, 200), 'D{0}image.gif'.format(integer))

        # append each dice image to dice image list.
        image_list.append(dice_image)

        # add 100 to x coordinate for each subsequent image.
        x += 100

    # draw each dice image in image list with for loop.
    for dice in image_list:

        # draw dices in graph window.
        dice.draw(graph_window)

    # return the function to dice value and image lists.
    return value_list, image_list
            

# define ball bounce function.
def bounce(circle1, circle2, dx1, dx2):

    # point 1 defined.
    p1 = circle1.getCenter()

    # point center defined.
    p2 = circle2.getCenter()

    # if x coordinate of center is not in this range.
    if p1.getX() not in range(21, 179):

        # change the direction
        dx1 *= -1

    # if x coordinate of center is not in this range.
    if p2.getX() not in range(521, 679):

        # change the direction
        dx2 *= -1

    # return the dx.
    return dx1, dx2


# define a main() function.
def main():
    
    # initialize empty list 2.
    l1 = []

    # initialize empty list 2.
    l2 = []

    # call diceWindow() function with its returned variables.
    graph_window, exit_rect, play_rect, play_text, score_text, circle1, circle2 = diceWindow()

    # initialize Gameplay variable False.
    playmode = "Startup"

    # use checkMouse() method to see if there is a mouse click within window.
    mouse = graph_window.checkMouse()

    # nrolls initialized zero.
    nrolls = 0

    # total score initialized zero.
    tscore = 0

    # assign movement for circle 1.
    dx1 = 5

    # assign movement for circle 2.
    dx2 = 5
    
    # use while loop until the click is within red rectangle "EXIT".
    while not isClickedR(mouse, exit_rect):
        
        # use checkMouse() method to see if there is a mouse click within window.
        mouse = graph_window.checkMouse()
        
        # if playmode is in Startup.
        if playmode == "Startup":

            # play rectangle setfilled green
            play_rect.setFill('green')

            # play rect text setted to "PLAY".
            play_text.setText("PLAY")

            # score text setted to "Want to play a game?"
            score_text.setText("Want to play a game?")

            # get the center of the circles.
            c1 = circle1.getCenter()

            # get the center of the circles.
            c2 = circle2.getCenter()

            # get the x point of circles.
            x1 = c1.getX()

            # get the x point of circles.
            x2 = c2.getX()

            # if both x are not initial x.
            if x1 != 85 and x2 != 610:

                # circle initial 1 created.
                circle1 = Circle(Point(85,290), 20)

                # set the color of circle initial 1.
                circle1.setFill("green")
    
                # draw circle initial 1.
                circle1.draw(graph_window)

                # circle initial 2 created.
                circle2 = Circle(Point(610,290), 20)

                # set the color of circle initial 2.
                circle2.setFill("red")

                # draw circle initial 2.
                circle2.draw(graph_window)

            # if clicked in play rectangle in Startup mode.
            if isClickedR(mouse, play_rect)== True:

                # call scorecard function.
                scr_win, total_entry = ScorecardWindow()
                
                # playmode is converted to Gameplay.
                playmode = "GamePlay"

        # if playmode is in Gameplay.
        elif playmode == "GamePlay":

            # if nrolls is 0.
            if nrolls == 0:
                
                # update the "Want to play a game?" text object to display "Click ROLL to begin" text object.
                score_text.setText('Click ROLL to begin')

            # make circle 1 black.
            circle1.setFill("black")

            # set "ROLL" rectangle black color.
            play_rect.setFill("black")

            # play rectangle text setted to "ROLL".
            play_text.setText("ROLL")

            # move circle 1.
            circle1.move(dx1,0)

            # sleep for a while.
            sleep(0.015)

            # move circle 2.
            circle2.move(dx2,0)
    
            # sleep for a while.
            sleep(0.015)

            # dx1 and dx2 variable called with first bounce function.
            dx1, dx2 = bounce(circle1, circle2, dx1, dx2)

            # if roll button clicked and nrolls less than 5, or equal or bigger than 0.
            if isClickedR(mouse, play_rect) == True and 0 <= nrolls < 5:

                # update the "Click ROLL to begin" text object to display "Rolling dice now..." text object.
                score_text.setText('Rolling the dices...')

                # pause the program 1 second to use sleep() function.
                sleep(1)
                
                # rollDice function called.
                value_list, image_list = rollDice(graph_window,l1,l2)
  
                # use checkMouse() method to see if there is a mouse click within window.
                mouse = graph_window.checkMouse()

                # assign click to 0.
                click = 0

                # anchor_points list created.
                anchor_points = []
                
                # while click is not detected and roll is bigger than 0.
                while not isClickedR(mouse, play_rect):
                    
                    # if that click is the initial click.
                    if click == 0:

                        # update the "Score: 0" text object to display "Rolling dice now..." text object.
                        score_text.setText('Click dice to discard...')

                    # if click already clicked once.
                    if click > 0:
                        
                        # update the "Score: 0" text object to display "Rolling dice now..." text object.
                        score_text.setText('Click ROLL to replace...')


                    # dice image is assigned to its value
                    d1 = image_list[0]

                    # dice image is assigned to its value
                    d2 = image_list[1]

                    # dice image is assigned to its value
                    d3 = image_list[2]

                    # dice image is assigned to its value
                    d4 = image_list[3]

                    # dice image is assigned to its value
                    d5 = image_list[4]

                    # dice image is assigned to its value
                    d6 = image_list[5]

                    # get the center point of the image
                    c1 = d1.getAnchor()

                    # get the center point of the image
                    c2 = d2.getAnchor()

                    # get the center point of the image
                    c3 = d3.getAnchor()

                    # get the center point of the image
                    c4 = d4.getAnchor()

                    # get the center point of the image
                    c5 = d5.getAnchor()

                    # get the center point of the image
                    c6 = d6.getAnchor()

                    # get x of center.
                    x1 = c1.getX()

                    # get x of center.
                    y1 = c1.getY()

                    # get x of center.
                    x2 = c2.getX()

                    # get x of center.
                    y2 = c2.getY()

                    # get x of center.
                    x3 = c3.getX()

                    # get x of center.
                    y3 = c3.getY()

                    # get x of center.
                    x4 = c4.getX()

                    # get x of center.
                    y4 = c4.getY()
  
                    # get x of center.
                    x5 = c5.getX()

                    # get x of center.
                    y5 = c5.getY()

                    # get x of center.
                    x6 = c6.getX()

                    # get x of center.
                    y6 = c6.getY()
                    
                    # create a rectangle according to the coordinates of image
                    d_area1 = Rectangle(Point(x1-50, y1+50), Point(x1+50, y1-50))

                    # create a rectangle according to the coordinates of image
                    d_area2 = Rectangle(Point(x2-50, y2+50), Point(x2+50, y2-50))

                    # create a rectangle according to the coordinates of image
                    d_area3 = Rectangle(Point(x3-50, y3+50), Point(x3+50, y3-50))

                    # create a rectangle according to the coordinates of image
                    d_area4 = Rectangle(Point(x4-50, y4+50), Point(x4+50, y4-50))

                    # create a rectangle according to the coordinates of image
                    d_area5 = Rectangle(Point(x5-50, y5+50), Point(x5+50, y5-50))

                    # create a rectangle according to the coordinates of image
                    d_area6 = Rectangle(Point(x6-50, y6+50), Point(x6+50, y6-50))
  
                    # use checkMouse() method to see if there is a mouse click within window.
                    mouse = graph_window.checkMouse()

                    # if click is detected inside the image area.
                    if isClickedR(mouse, d_area1) and click < 6:
                        
                        # undraw that image
                        d1.undraw()

                        # pop the index value of that corresponding integer of image.
                        value_list.pop(0)
                        
                        # insert 0 in the position of deleted value.
                        value_list.insert(0, 0)

                        # anchor points appended to list.
                        anchor_points.append(c1)
                        
                        # increment click by 1.
                        click += 1

                    # if click is detected inside the image area.
                    if isClickedR(mouse, d_area2) and click < 6:

                        # undraw that image
                        d2.undraw()

                        # pop the index value of that corresponding integer of image.
                        value_list.pop(1)
                        
                        # insert 0 in the position of deleted value.
                        value_list.insert(1, 0)

                        # anchor points appended to list.
                        anchor_points.append(c2)
                        
                        # increment click by 1.
                        click += 1

                    # if click is detected inside the image area.
                    if isClickedR(mouse, d_area3) and click < 6:

                        # undraw that image
                        d3.undraw()

                        # pop the index value of that corresponding integer of image.
                        value_list.pop(2)
                        
                        # insert 0 in the position of deleted value.
                        value_list.insert(2, 0)

                        # anchor points appended to list.
                        anchor_points.append(c3)
                        
                        # increment click by 1.
                        click += 1

                    # if click is detected inside the image area.
                    if isClickedR(mouse, d_area4) and click < 6:

                        # undraw that image
                        d4.undraw()

                        # pop the index value of that corresponding integer of image.
                        value_list.pop(3)
                        
                        # insert 0 in the position of deleted value.
                        value_list.insert(3, 0)

                        # anchor points appended to list.
                        anchor_points.append(c4)
                        
                        # increment click by 1.
                        click += 1

                    # if click is detected inside the image area.
                    if isClickedR(mouse, d_area5) and click < 6:

                        # undraw that image
                        d5.undraw()

                        # pop the index value of that corresponding integer of image.
                        value_list.pop(4)
                        
                        # insert 0 in the position of deleted value.
                        value_list.insert(4, 0)

                        # anchor points appended to list.
                        anchor_points.append(c5)
                        
                        # increment click by 1.
                        click += 1

                    # if click is detected inside the image area.
                    if isClickedR(mouse, d_area6) and click < 6:

                        # undraw that image
                        d6.undraw()

                        # pop the index value of that corresponding integer of image.
                        value_list.pop(5)
                    
                        # insert 0 in the position of deleted value.
                        value_list.insert(5, 0)

                        # anchor points appended to list.
                        anchor_points.append(c6)

                        # increment click by 1.
                        click += 1

                # update the "Score: 0" text object to display "Rolling dice now..." text object.
                score_text.setText('Rolling the dices...')

                # pause the program 1 second to use sleep() function.
                sleep(1)

                # initialize zero variable as a position value.
                zero = 0
                
                # for value in value list.
                for value in value_list:

                    # if value is equal to 0.
                    if value == 0:

                        # get the index of 0 value and assign it.
                        p = value_list.index(value)

                        # remove value.
                        value_list.remove(value)

                        # insert random integers to 0 values.
                        value_list.insert(p, randint(1,6))

                        # remove the clicked value from image list.
                        image_list.pop(p)

                        # create image based on each integer.
                        dice = Image(anchor_points[zero], 'D{0}image.gif'.format(value_list[p]))

                        # append each dice image to dice image list.
                        image_list.insert(p, dice)

                        # draw the dice to graph_window.
                        dice.draw(graph_window)

                        # increment zer by 1.
                        zero += 1

                # sum of value calculated.
                SUM = sum(value_list)
                
                # duplcates counted and putted in a list
                Dups = [value_list.count(1),value_list.count(2),value_list.count(3),value_list.count(4),value_list.count(5),value_list.count(6)]

                # multiplier is equalized to maximum value of Dups
                multiplier = max(Dups)

                # n_score is assigned to sum multiplied by multiplier.
                n_score = SUM * multiplier

                # total score increased by each score in round.
                tscore += n_score

                # statements of each roll putted in list.
                statements = ["No Duplicates","Pair","3 of a kind","4 of a kind","5 of a kind","BOILER UP"]
                                
                # score text setted with sum of roll values with calculation with multiplier and solution(n_score).
                score_text.setText("{0}: {1} x {2} = {3}".format(statements[multiplier-1],SUM,multiplier,n_score))

                # text created for each roll to round, statement, and score drew in the scorecard.
                Info = Text(Point(200, 175+nrolls*30),"{0:<4} {1:<13} {2:>3}".format(str(nrolls+1)+")",statements[multiplier-1], n_score))

                # set the size of the Info text.
                Info.setSize(19)
                
                # set the face of the Info text.
                Info.setFace("courier")
                
                # set the color of the Info text.
                Info.setTextColor("gold")

                # draw Info text.
                Info.draw(scr_win)

                # set the total value to entry box
                total_entry.setText("{0:>9}".format(tscore))

                # inreace roll count by 1.
                nrolls += 1
                
            # if roll count reached to 5.
            if nrolls >= 5:

                # undraw circle 1.
                circle1.undraw()

                # undraw circle 2.
                circle2.undraw()

                # playmode turn in GameOver.
                playmode = "GameOver"

        # if playmode is Gameover.
        elif playmode == "GameOver":

            # game over rectangle created.
            game_over = Rectangle(Point(50,530), Point(350, 330))

            # game over rectangle color setted.
            game_over.setFill("gold")

            # game over rectangle drawn.
            game_over.draw(scr_win)

            # game over text created.
            txt_over = Text(Point(197,352), "GAME OVER")

            # set game over text size.
            txt_over.setSize(20)

            # set game over text size.
            txt_over.setStyle("bold")

            # draw game over text.
            txt_over.draw(scr_win)

            # game over text command created.
            click_over = Text(Point(195,381), "Enter your name")

            # game over text command stye setted to italic.
            click_over.setStyle("italic")

            # game over text command stye setted to italic drawn
            click_over.draw(scr_win)

            # entry boc for name created.
            entry_name = Entry(Point(175,430),10)

            # set the font size of entry box.
            entry_name.setSize(20)

            # set the color of entry box.
            entry_name.setFill("white")

            # draw entry box for name.
            entry_name.draw(scr_win)

            # create a black filled rectangle for "DONE" button.
            done_rect = Rectangle(Point(240,445), Point(290,415))

            # set the done rectangle color black.
            done_rect.setFill("black")

            # draw the done rectangle on score card window
            done_rect.draw(scr_win)

            # get the center point of the done rectangle.
            done_c = done_rect.getCenter()

            # create the done text and draw on the done rectangle.
            done_txt = Text(done_c, "DONE")

            # set the color of done text.
            done_txt.setFill("gold")

            # set the size of done text.
            done_txt.setSize(15)

            # draw done text lable.
            done_txt.draw(scr_win)

            # create last 5 player Rectangle.
            last5 = Rectangle(Point(135,100), Point(265,70))

            # set the color of rectangle.
            last5.setFill("green")

            # draw last 5 rectangle.
            last5.draw(scr_win)

            # get the center of last 5.
            center = last5.getCenter()

            # get the final score text in total entry.
            final_score = total_entry.getText()

            # mouse click initialized.
            mousec = Point(0,0)
            
            # define string name in entry text.
            name = entry_name.getText()

            # while done rectanle is not clicked and name entry box is empty.
            while not isClickedR(mousec, done_rect) and name != True:

                # create last 5 label.
                last5_label = Text(center, "Last 5 Player Coming...")

                # set size of the label.
                last5_label.setSize(10)

                # set the style of a label.
                last5_label.setStyle("bold")
                    
                # set the color of last 5 label.
                last5_label.setFill("white")

                # sleep for half a second.
                sleep(0.55)

                # last 5 label drawn.
                last5_label.draw(scr_win)

                # sleep for half a second.
                sleep(0.55)

                # last 5 label undrawn.
                last5_label.undraw()

                # checkMouse() to not disturp typing with sleep.
                mousec = scr_win.checkMouse()

            # undraw the rectangle last 5 statement.
            last5.undraw()

            # undraw the last 5 label.
            last5_label.undraw()

            # open data file to write and read.
            file = open('zeeScores.txt', 'r+')

            # get the final score text in total entry.
            final_score = total_entry.getText()

            # define string name in entry text again.
            name = entry_name.getText()

            # create the data that must be appended to the file.
            data = '\n{0},{1}'.format(name, final_score)

            # append the data to file.
            file.write(data)

            # replace the "Click HERE to continue" text with "Enter your name".
            click_over.setText("Click HERE to Continue...")

            # undraw entry box for name.
            entry_name.undraw()

            # undraw done rectangle.
            done_rect.undraw()

            # undraw done text label.
            done_txt.undraw()

            # initialize players list.
            players = []

            # create data list.
            data_list = file.readlines()

            # for player in range.
            for player in data_list[-5:]:

                # append last five player to players list.
                players.append(player)

            # initialize player text list
            player_text =[]

            # for name,score(ns) in players list.
            for ns in players:

                # split the name and score and put in a list for each data line.
                line = ns.split(",")

                # append the line list to player_text.
                player_text.append(line)
                    
            # initialize y point of name and score text labels.
            y = 420                
 
            # for each line in player text list.
            for ln in player_text:

                # create the text string and assign it to variable.
                txt = "{0:<10}{1:>10}".format(ln[0],ln[1])

                # create text object for each data line.
                data_line = Text(Point(195, y), txt)

                # set size of data_line text.
                data_line.setSize(14)

                # draw the text label to scorecard window.
                data_line.draw(scr_win)
                    
                # incremet y by 10.
                y += 22

            # close the f file that opened for read data.
            file.close()

            # finished circle created.
            finish_circle = Circle(Point(200, 85), 28)

            # set the clolor of the circle.
            finish_circle.setFill("red")

            # draw the finished circle.
            finish_circle.draw(scr_win)

            # center point created
            cntr = finish_circle.getCenter()

            # mouse click initialized.
            mouseclick = Point(0,0)

            # initialize the mouse click point on score card window.
            mousep = Point(0,0)
 
            # while game over button not clicked yet.
            while not isClickedR(mouseclick, game_over):

                # create text label.
                finished = Text(cntr, "FINISHED")

                # set size of finished.
                finished.setSize(10)

                # set the style of a finished.
                finished.setStyle("bold")

                # set the color of text label
                finished.setFill("white")

                # sleep for half a second
                sleep(0.55)

                # draw the text label.
                finished.draw(scr_win)

                # sleep for half a second
                sleep(0.55)

                # undraw the text label.
                finished.undraw()

                # check the mouse click point on score card window.
                mouseclick = scr_win.checkMouse()

            # rolls initialized 0 again.
            nrolls = 0

            # rolls initialized 0 again.
            tscore = 0

            # for i in range 6.
            for i in range(6):

                # all images undrawn.
                image_list[i].undraw()

            # close the scorecard window.
            scr_win.close()

            # mouse click checked.
            mousep = graph_window.checkMouse()

            # mouse click checked again.
            mousep = graph_window.checkMouse()

            # playmode  initialized to startup.
            playmode = "Startup"
                
    # try to close both window.
    try:

        # when exit button clicked, graph window closed.
        graph_window.close()

        # and scorecardwindow closed
        scr_win.close()

    # except, scr_win not opened yet...
    except:

        # just close graph window.
        graph_window.close()

# call the main function.
main()


