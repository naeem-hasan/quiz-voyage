# quiz-voyage
An automated quizzing system for Facebook, that can post premade questions, check for answers and then reward later post results.

## What is it?
Quiz Voyage can conduct Q/A quizzes with Facebook pages. It posts a question, then continuously checks for correct answer among the comments. If it finds one, it will note the answerer's name, faction he's playing for and the points that are associated with the question and then move onto the next question. In the end of the quiz, it'll make a result post as well.
Demo page: [Quiz Voyage](http://facebook.com/QuizVoyage)

## Requirements:
* Python 2
* [Facebook SDK for Python](https://github.com/mobolic/facebook-sdk)
* Your page's ACCESS TOKEN. Get it from [here](https://developers.facebook.com/tools/explorer/).

## Usage:
At first define your custom QuestionSet object. Inside of it, make your Question objects. Get your page's ACCESS TOKEN, put it in the `ACCESS_TOKEN` variable of `quiz_voyage.py`. Then just pass your `QuestionSet` object as the parameter of the `run_voyage` function and run script.

## NOTE:
The source code already is supplied with Harry Potter question set. Edit it however necessary.
