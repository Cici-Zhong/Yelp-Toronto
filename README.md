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

Logic of this question: most match-City-Toronto;
Bussiness.Json-Details all in ; Stars>=4;List from high to low review-chech the count number;

Code in Mostmatch.py
Result :The 10 restaurants ID and then know the detials: def mastmatch(business_path, review_path):
    business_list = getFileContentToListAndFilter(business_path, 'city', '==', 'Toronto')
    business_list = filter(business_list, 'stars', '>=', 4)
    print(len(business_list))
    review_dict = {}
    for business in business_list:
        review_dict[business['business_id']] = 0
    business_id_list = review_dict.keys()
    print(len(business_id_list))
    review_list = getFileContentToListAndFilter(review_path, 'business_id', 'in', business_id_list)
    print(len(review_list))
    for review in review_list:
        # if review['business_id'] in business_id_list:
        review_dict[review['business_id']] += 1
    sorted_keys = sorted(review_dict, key=review_dict.get, reverse=True)[:10]
    print(len(sorted_keys))
    result_list = []
    for k in sorted_keys:
        result_list.append({
            'business_id': k,
            'review_count': review_dict[k]
        })
    return result_list

if __name__ == '__main__':
    business_list = mastmatch('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json')
    print(business_list)
    
 
 Results examples list:1. Pai Northern Thai Kitchen;2. Khao San Road; KINKA IZAKAYA ORIGINAL;Seven Lives Tacos Y Mariscos; Banh Mi Boys;Momofuku Noodle Bar;Salad King Restaurant8. Gusto 101 Sansotei Ramen; Insomnia Restaurant & Lounge

 
3. How many Canadian residents reviewed the business “Mon Ami Gabi” in last 1 year?
From the MonAmiGabi.py code
from utils import *

import sys

def monamigabi_bids(business_path, review_path, business_name):
    business_list = getFileContentToListAndFilter(business_path, 'name', '==', business_name)
    if len(business_list) == 0:
        print('not find business with name {}'.format(business_name))
        sys.exit()
    else:
        business_id = business_list[0]['business_id']
        print('find business with name {} has id {}'.format(business_name, business_id))
        review_list = getFileContentToListAndFilter(review_path, 'business_id', '==', business_id)
        print('find {} reviews relating to {}'.format(len(review_list), business_id))
        user_set = set([])
        for review in review_list:
            user_set.add(review['user_id'])
        print('find {} users relating to business {}'.format(len(user_set), business_id))
        businesses_in_on = getFileContentToListAndFilter(business_path, 'state', '==', 'ON')
        business_ids_in_on = [b['business_id'] for b in businesses_in_on if b['business_id'] != business_id]
        print('find {} businesses in ON'.format(len(business_ids_in_on)))
        user_list = []
        review_list = getFileContentToListAndFilter(review_path, 'user_id', 'in', list(user_set))
        for user_id in user_set:
            user_review_list = filter(review_list, 'user_id', '==', user_id)
            user = {
                'id': user_id,
                'businesses': len({r['business_id'] for r in user_review_list if r['business_id'] in business_ids_in_on})
            }
            if user['businesses'] >= 10:
                user_list.append(user)
        return user_list

if __name__ == '__main__':
    users = monamigabi_bids('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json', 'Mon Ami Gabi')
    print(len(users))
    print(users)
    # find business with name Mon Ami Gabi has id 4JNXUYY8wbaaDmk3BPzlWw
    # find 7968 reviews relating to 4JNXUYY8wbaaDmk3BPzlWw
    # find 7968 users relating to business 4JNXUYY8wbaaDmk3BPzlWw
    # find 32393 businesses in ON
   



4. Top 10 most common words in the reviews of the business “Chipotle Mexican Grill”
From the Chipatle.py

if __name__ == '__main__':
    words = chipatle('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json', 'Chipotle Mexican Grill')
    print(words)
    # ['to', 'the', 'is', 'this', 'and', 'a', 'it', 'location', 'I', 'you']
    
5. What’s the percentage of users, who reviewed “Mon Ami Gabi”, and also reviewed at
least 10 other restaurants located in Ontario?
Bussiness Id-Review-users

Dictionary: Key=user-id;Value=unique(business_id)
From the MonAmiGabi-bids.py
which based on the number2questions, results is 78


6. Please think about 2 more analytics, which provide insights and help existing/future
Business Owners, to make important decisions regarding new business or business
expansion.

The best analytics are fist list the location of the most popularity restaruants which are  // float, latitude
    "latitude": xx.xxxx,// float, longitude"longitude": xxx.xxxx,such as x1,y1,x2,y2,x3,y3... and then maping it in one cloud map and then find the GIS best area and advised the area and location for the new restaurants. Which use the three point methods to high it.
    
Anthor method: Top 10 popular categories to advice for the best categories to open in Toronto and the avid to open it in the same categories highlight in the GIS and not choose the loaction same area.

The Question2 

Top10.py 
the top10 popular categories in Toronto which the people's favior here and advise and recommend the restarant same categries in Las Vegas, such as the information:

if __name__ == '__main__':
    business_list = top10_in_lv('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json')
    print(business_list)
    # business_list = [{'business_id': '4JNXUYY8wbaaDmk3BPzlWw', 'review_count': 7968}, {'business_id': 'RESDUcs7fIiihp38-d6_6g', 'review_count': 7861}, {'business_id': 'cYwJA2A6I12KNkm2rtXd5g', 'review_count': 5472}, {'business_id': 'f4x1YBxkLrZg652xt2KR5g', 'review_count': 5382}, {'business_id': 'DkYS3arLOhA8si5uUEmHOw', 'review_count': 4981}, {'business_id': 'iCQpiavjjPzJ5_3gPD5Ebg', 'review_count': 4078}, {'business_id': 'KskYqH1Bi7Z_61pH6Om8pg', 'review_count': 3976}, {'business_id': 'rcaPajgKOJC2vo_l3xa42A', 'review_count': 3742}, {'business_id': 'hihud--QRriCYZw1zZvW4g', 'review_count': 3733}, {'business_id': '7sPNbCx7vGAaH7SbNPZ6oA', 'review_count': 3249}]
    business_list = getFileContentToListAndFilter('./yelp_dataset/yelp_academic_dataset_business.json', 'business_id', 'in', [b['business_id'] for b in business_list])
    print(business_list)
    
    For exmaple details:
    In Las Vegas:\'name': 'Lotus of Siam', 'Gordon Ramsay BurGR', 'Gangnam Asian BBQ Dining', Earl of Sandwich''Bachi Burger', 'Hash House A Go Go', 'Secret Pizza', Bacchanal Buffet'and so on



