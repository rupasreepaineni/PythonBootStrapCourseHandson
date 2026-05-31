This is the same code which we did in the DAY-17

modifications we're doing here is
1. we're fteching the data through an API and not hardcoding it in the code
Endpoint url : https://opentdb.com/api.php?amount=10&type=boolean
2. we're using the data to create the quiz app instead of hardcoding the questions and answers in the code[data.py]
3. Unescape html characters in the questions and answers[ in quiz_brain.py]
just change the question_text to the html.unescape(question_text)
4. Create the ui fields
5. Create the quiz brain and pass the data to it, pass the quiz object to the ui and start the quiz(quizui = QuizUi(quiz))
6. catch to the constructor of the ui
7. create the function to get the next question and display it on the ui- get_next_question
8. create the function to check the answer and update the score- check_answer, 
by clicking the true or false button, the answer will be checked and the score will be updated -[create separate functions for true and false button and call the check_answer function in it]
9. then give feedback to the user by changing the background color of the screen to green ,
if the answer is correct and red if the answer is wrong,
then after a short delay of 1 second change it back to white- give_feedback
10. then after the quiz is completed, display the final score to the user and disable the true and false buttons- give_feedback
