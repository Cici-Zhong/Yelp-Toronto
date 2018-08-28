from utils import *

import sys

def monamigabi(business_path, review_path, business_name):
    business_list = getFileContentToListAndFilter(business_path, 'name', '==', business_name)
    if len(business_list) == 0:
        print('not find business with name {}'.format(business_name))
        sys.exit()
    else:
        business_id = business_list[0]['business_id']
        print('find business with name {} has id {}'.format(business_name, business_id))
        review_list = getFileContentToListAndFilter(review_path, 'business_id', '==', business_id)
        print('find {} reviews relating to {}'.format(len(review_list), business_id))
        review_list = filter(review_list, 'date', '>=', '2017-01-01')
        review_list = filter(review_list, 'date', '<=', '2018-01-01')
        print('find {} reviews relating to {} between 2017-01-01 to 2018-01-01'.format(len(review_list), business_id))
        user_dict = {}
        for review in review_list:
            if review['user_id'] in user_dict.keys():
                user_dict[review['user_id']] += 1
            else:
                user_dict[review['user_id']] = 1
        return user_dict

if __name__ == '__main__':
    users = monamigabi('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json', 'Mon Ami Gabi')
    print('there are {} users reviewing business with id {}'.format(len(users.keys()), 'Mon Ami Gabi'))
