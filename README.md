# Yelp-Toronto
## Toronto Restaturant Survey

PS:Base on the https://github.com/Yelp/dataset-examples.git for conver Json file to CSV version. 

Overview
The purpose of this data challenge is to get a sense of what it would be like to work with you
on a day-to-day basis. The completed challenge gives us a body of work to go over together
in a project review session. We will evaluate you on your implementation, design choices,
choice of technologies, etc. Please communicate a present day as soon as you can. The
deadline is 5 business days(1 week) after you get this assignment.

Backgroud:

The logic was used is the recent advanced Stanford NLP, statics and management model.  


1. Ingest and perform analytics over Yelp open dataset (Json format only NOT SQL
format) from either https://www.yelp.com/dataset or
https://s3.amazonaws.com/datachallenge.lift.co/yelp_dataset.tar​ to a data store (NoSQL
or RDBMS)

Json data is established and operationed，which could directly be called with out CSV convert.


2. Top 10 restaurants in Toronto with highest popularity. You are free to define your
‘popularity’, as long as it makes sense. 

For this case, the popularity in Yelp is defined in three ways which means there are three main methods in the yelp data to judge it is a highest popularity restaurant or not: Highest Rates of Reviews, Highest stars and Most Match, in which most match we anlysis as the all the information such as location, phone number and so on details in bussiness.json are all filled and correct, and then we search for the stars upper and equal to 4 stars and then from this new database we got the rank list of the reviews from the highest to the lowest.


 
3. How many Canadian residents reviewed the business “Mon Ami Gabi” in last 1 year?


4. Top 10 most common words in the reviews of the business “Chipotle Mexican Grill”


5. What’s the percentage of users, who reviewed “Mon Ami Gabi”, and also reviewed at
least 10 other restaurants located in Ontario?


6. Please think about 2 more analytics, which provide insights and help existing/future
Business Owners, to make important decisions regarding new business or business
expansion.


