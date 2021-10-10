# EC601
----------------------------------------------------------
Project2

The code uses twitter api to realize the function of searching for tweets containing specific characters, it can return all the tweets searched and the number of searched twitter.
This code is inspired by the work "https://github.com/agalea91/twitter_search/blob/master/twitter_search.py"


----------------------------------------------------------
User Story

As a customer, I want to see people’s immediate and real review of the thing I am interested in whenever and wherever I want so that I can decide whether I will spend my and money into it.

As an owner of a business, I want to see customers' review of my product and service so that I can make improvement to my business.

As an entrepreneur, I want to see what people needs the most so that I can make my business acquire large number of users.

As an administrator of twitter, I want to search tweets that spread hate or false information.

As a politician, I want to know what people care and their review on latest policies so that I can improve my speech to get more supporters.

As a game developer, I want to know players' most recent review on new patches so that I can know how to make the game better.


-----------------------------------------------------------
MVP

The analyzer should be able to get access to tweets.
The analyzer should be able to filter tweets using the search words.
The analyzer should be able to get access to Google NLP
The analyzer should be able to do sentiment analysis and report the points to the user


-----------------------------------------------------------
Modular design

Modular1
Authorization Authentication
This module is the most basic one, it ensures this social media analyzer can work

Modular2
Marking tweets
When people send tweets, based on different types of the user of the social media analyzer, their tweets can be marked with different markers, when different types of tweets are searched, this marked tweets will be easier to be found and improve the efficiency of the whole searching porcess.

Modular3
Searching tweets
Using the twitter API and the search words the user input, search tweets.

Modular4
Analyzing tweets
Analyzing tweets sentiment using the Google NLP API and output the average score.

Modular5
Report the analyzing result to the user.
