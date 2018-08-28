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
    # 78
