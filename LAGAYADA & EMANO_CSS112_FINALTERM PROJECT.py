import turtle
import random

# setting up the game
def setup_game():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Egg Catcher by Lagayada & Emano")
    screen.bgcolor("deep sky blue")
    screen.setup(width=900, height=600)

    # Create rectangle
    rectangle = turtle.Turtle()
    rectangle.speed(0)
    rectangle.penup()
    rectangle.goto(100, -250)
    rectangle.shape("square")
    rectangle.shapesize(stretch_wid=10, stretch_len=130)
    rectangle.color("forest green")

    # Create sun
    oval = turtle.Turtle()
    oval.speed(0)
    oval.penup()
    oval.goto(-400, 260)
    oval.shape("circle")
    oval.shapesize(stretch_wid=10, stretch_len=10)
    oval.color("orange")

    # Create the basket turtle or hole
    basket = turtle.Turtle()
    basket.shape("circle")
    basket.color("sienna")
    basket.shapesize(stretch_wid=1, stretch_len=5)
    basket.penup()
    basket.speed(0)
    basket.goto(0, -250)

    # Initialize score and lives
    score, lives = 0, 3

    # List to store eggs
    eggs = []

    # List to store clouds
    clouds = []

    # Difficulty settings
    difficulty = screen.textinput("Difficulty", "Choose difficulty (easy/hard): ")

    if difficulty == "easy":
        egg_speed = 7
        egg_interval = 5000  # 5 seconds
    elif difficulty == "hard":
        egg_speed = 10
        egg_interval = 3000  # 3 seconds
    else:
        print("Invalid difficulty level. Defaulting to easy.")
        egg_speed = 7
        egg_interval = 5000  # 5 seconds

    # Create initial clouds
    for _ in range(3):
        x = random.randint(-400, 400)
        y = random.randint(100, 200)
        cloud = create_cloud(x, y)
        clouds.append(cloud)

    # Keyboard bindings
    screen.listen()
    screen.onkeypress(lambda: basket.setx(basket.xcor() - 30), "Left")
    screen.onkeypress(lambda: basket.setx(basket.xcor() + 30), "Right")

    # Schedule the creation of a new egg every 5 seconds
    screen.ontimer(create_egg, 10000)

    return screen, basket, eggs, clouds, egg_speed, egg_interval, score, lives

# Function to create a new egg
def create_egg():
    x = random.randint(-290, 290)
    y = 250
    new_egg = turtle.Turtle()
    new_egg.shape("circle")
    new_egg.color("light pink")
    new_egg.shapesize(stretch_wid=3, stretch_len=2)
    new_egg.penup()
    new_egg.speed(0)
    new_egg.goto(x, y)
    eggs.append(new_egg)

# Function to create a cloud turtle
def create_cloud(x, y):
    cloud = turtle.Turtle()
    cloud.speed(0)
    cloud.penup()
    cloud.goto(x, y)
    cloud.shape("circle")
    cloud.color("white")
    cloud.shapesize(stretch_wid=2, stretch_len=6)
    return cloud

# Function to move a cloud
def move_cloud(cloud, speed):
    x = cloud.xcor()
    x -= speed
    cloud.setx(x)

# Function to check if a cloud is out of the screen
def is_cloud_out_of_screen(cloud):
    return cloud.xcor() < -450

# looping the game
def game_loop(screen, basket, eggs, clouds, egg_speed, egg_interval, score, lives):
    while lives > 0:
        # Check if there are no eggs on the screen
        if not eggs:
            x = random.randint(-290, 290)
            y = 250
            new_egg = turtle.Turtle()
            new_egg.shape("circle")
            new_egg.color("light pink")
            new_egg.shapesize(stretch_wid=3, stretch_len=2)
            new_egg.penup()
            new_egg.speed(0)
            new_egg.goto(x, y)
            eggs.append(new_egg)

        # Move and check clouds
        for cloud in clouds:
            move_cloud(cloud, 2)  # Adjust the speed of the clouds
            if is_cloud_out_of_screen(cloud):
                new_x = random.randint(400, 600)
                new_y = random.randint(100, 200)
                cloud.goto(new_x, new_y)

        for egg in eggs:
            egg.sety(egg.ycor() - egg_speed)  # Adjust the speed of the eggs

            # Check if the basket caught the egg
            if basket.distance(egg) < 30:
                egg.goto(random.randint(-290, 290), 250)
                score += 10
                screen.title("Egg Catcher - Score: {} Lives: {}".format(score, lives))

            # Check if the egg reached the bottom
            if egg.ycor() < -290:
                egg.goto(random.randint(-290, 290), 250)
                lives -= 1
                screen.title("Egg Catcher - Score: {} Lives: {}".format(score, lives))
                if lives == 0:
                    turtle.penup()
                    turtle.goto(0, 0)
                    turtle.color("maroon")
                    turtle.write("Game Over! Final Score: {}".format(score), align="center", font=("Times", 45, "bold"))
                    turtle.hideturtle()
                    turtle.done()

        # Update the screen
        screen.update()


# Initial game setup
game_running = True
screen, basket, eggs, clouds, egg_speed, egg_interval, score, lives = setup_game()
game_running = game_loop(screen, basket, eggs, clouds, egg_speed, egg_interval, score, lives)

# Start the turtle main loop
turtle.mainloop()
