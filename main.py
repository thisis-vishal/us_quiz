import turtle
import pandas as pd
from pandas._libs import missing
screen=turtle.Screen()
screen.title("U.S.-States-Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score=0
states=pd.read_csv("50_states.csv")
all_states=states.state.to_list()
guessed_states=[]
while (score<51):   
    answer_state=screen.textinput(title=f"score={score}/50",prompt="guess another state")
    answer_state=answer_state.title()
    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states to learn")        
        h=pd.read_csv("states to learn")
        print(h)
        break    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=states[states.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state,align="center")
        score+=1 
    else:
        pass
screen.mainloop()