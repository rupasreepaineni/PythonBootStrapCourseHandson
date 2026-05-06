problem breakdown:
1. Create a turtle within a screen based on the key input, that has to move across y axis
2. design a square with more length and it has to move randomly across y cor
3. if turtle hits the car across any width of the car/square, Game over
4. add the level to left end 
5. if it reaches to the other end, the level should increase and speed as well
6. Gameover should come towards the middle


player.py:
 Intiliazer:
1. created a turtle moved the towards downwards, and added the direction upwards
2. made screen to listen the event by adding "Up" function/method
3. if it reaches towards the end , added to start from the first by returning true

car_manager:
1. create a list to hold the cars
2. (create_car method)The screen refresh every moment it gonna generate a new car and move it to the left which generates multiple cars
3. so to minimize we use the random_choice function to generate a random number, 
between 1 and 6 and if the number is 1 then only we will generate a new car.
4. move_car: here backward, movement from 300 to -300
5. increase the speed for other level - increase_speed

scoreboard:
1. Created the level towards the left corner
2. added the count
3. increase the level when it reaches to the end
4. Gameover function

main.py:
