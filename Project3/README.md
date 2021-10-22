Unit tests for project 2
-------------------------------------------------------------

API_credentials
This is a test for whether this code has the access to the twitter API.
Run the function 'API_credentials' and this function will return api if it has access to the twitter API, then the test code will print'succeed' or, 'failed'.
Getting the credential is the first step to search tweets and do the sentiment analysis.


Run time

This code can return the time of searching all tweets.
Run the whole process and count the time.
The expected time should be as small as possible.
The searching time is very important for the experiece of users. If the time is too long then it means the searching code should be imporved.


Wrong input

This code can show whether the process has output when the input word is a punctuation.
Run the code and input '!'
It should return 'does out output'
Searching a punctuation is meaningless thus the code should not return any results when the input is a '!'


Input sentence

This code can show whether the process has output when the input word is a punctuation.
Run the code and input a sentence
It should return 'does out output'
Searching a sentence is meaningless thus the code should not return any results when the input is a '!'


Tweets num

This code can compare the number of tweets searched and the tweets number user input
Run the code, get the number of the output of the function 'twitter_search' and compare it to the input of the user.
Two numbers should be equal.
This is one of the most basic function the twitter API should achieve.
