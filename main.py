import turtle
import pandas
import os.path

screen = turtle.Screen()

screen.title("Name the parts of a face Game")

image = "face_image.gif"
screen.addshape(image)
turtle.shape(image)
coorx = []
coory = []
parts = ["eye", "nose", "mouth", "cheeks", "forehead", "chin", "eyebrows"]
parts_labelled = 0

def position_coordinates_generation(x, y):
    global parts_labelled
    coorx.append(x)
    coory.append(y)
    parts_labelled += 1

    if len(coorx) == 7:
        face_dict = {
            "parts": parts,
            "x": coorx,
            "y": coory
        }

        data = pandas.DataFrame(face_dict)
        print(data)

        data.to_csv("facial_features.csv")


# Now that I have created the csv file of coordinates I can comment out the code that calls the function
if os.path.isfile("facial_features.csv") is False:
    screen.onscreenclick(position_coordinates_generation)
score = 0
correct_guesses = []


def game_play():
    global score
    global correct_guesses
    name = screen.textinput(title=f"{score}/7 named", prompt="Name the parts!")

    data = pandas.read_csv("facial_features.csv")
    parts_list = data.parts.to_list()

    for part in parts_list:
        if name == part and part not in correct_guesses:
                correct_guesses.append(part)
                score += 1
                part_info = data[data.parts == f"{part}"]
                pos_x = int(part_info.x)
                pos_y = int(part_info.y)
                part_turtle = turtle.Turtle()
                part_turtle.penup()
                part_turtle.goto(pos_x, pos_y)
                part_turtle.write(f"{part}")

    if score < 7:
        game_play()


if score < 7 and os.path.isfile("facial_features.csv"):
    game_play()


turtle.mainloop()
