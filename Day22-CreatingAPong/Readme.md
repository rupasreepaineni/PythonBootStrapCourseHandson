This mainly concentrates on creating 
1. Create a screen with the name of the game and a background color
2.Create those two paddles which has to move in the user input direction,and a ball
3. A ball with a certain speed and direction, if it hits the y axis it should bounce back 
, if it hits the x axis it should reset to the center of the screen and start moving in a random direction
4. A scoring system that keeps track of the points for each player,
and displays the score on the screen.



paddle.py

1. Here we're creating a class called Paddle.
2. In this case, we're creating a blueprint for a paddle in our Pong game.
3. in init method, we initialize the paddle's position and size.
4. We also have a method called move that allows us to change the paddle's position based on user input.
5. The move method takes a direction as an argument and updates the paddle's position

ball.py
1. Here we're creating a class called Ball, setting ball coordinates, size, and speed.(__init_ method)
2. if it hits on the y axis, it should bounce back (bounce_Y)
3. if it hits on the x axis
,it should reset to the center of the screen and start moving in a random direction.(bounce_X)
4. if it hits the paddle, it should bounce back in the opposite direction with double speed 
5. if the paddle misses the ball,
,the score should be updated and the ball should reset to the center of the screen and start moving in a random direction (reset_position)

scoreboard.py
1. Here we're creating a class called Scoreboard, 
which is responsible for keeping track of the scores of the players and displaying them on the screen.
2. In the init method, we initialize the scores for both players and set up the turtle to display the scores on the screen.
3. update_score: We just kept a column for each player and update the score when a player scores a point.
4. l_score,r_score: whoever misses the ball, the other player gets a point, and we update the score accordingly.

main.py
1. Here we're creating the main game loop for our Pong game.
2. We set up the screen, create the paddles, ball, and scoreboard.
3. tracer: to avoid animation movements, and after refresh/update the screen, we can see the movement of the ball and paddles.
4. We listen for user input to move the paddles up and down.
5. We have a while loop that continuously updates the game state, checks for collisions, and updates the screen.
6. Inside the loop, we check for collisions between the ball and the paddles, as well as the ball and the walls of the screen.
7. If the ball hits the left or right wall, we update the score and reset the ball's position.
8. If the ball hits the top or bottom wall, we make it bounce back by changing its direction.
9