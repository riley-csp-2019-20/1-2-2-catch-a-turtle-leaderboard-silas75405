# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
trtlshape = "square"
trtlcolor = "blue"
trtlsize = 5
score = 0

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
fig = trtl.Turtle(shape=trtlshape)
fig.color(trtlcolor)
fig.shapesize(trtlsize)
fig.speed(0)


dis = trtl.Turtle()
dis.shapesize(trtlsize)
dis.penup()
dis.ht()
dis.goto(-395,295)
font_setup = ("Arial",20)
dis.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(340,298)

start = trtl.Turtle()
start.penup()
start.ht()
#-----game functions--------
def fig_clicked(x,y):
    print("fig got clicked")
    change_position()
    update_score()
    


def change_position():
    fig.penup()
    fig.ht()
    if not timer_up:
      figx = random.randint(-400,400)
      figy = random.randint(-300,300)
      fig.goto(figx,figy)
      fig.st()

def update_score():
    global score
    score += 1
    dis.clear()
    dis.write(score, font=font_setup)
    print(score)
    

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global fig

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, fig, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, fig, score)






#-----events----------------




wn = trtl.Screen()
wn.bgcolor("pink")
fig.onclick(fig_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()