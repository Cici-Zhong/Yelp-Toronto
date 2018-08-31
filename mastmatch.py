from utils import *

from os.path import join

def mastmatch(business_path, review_path):
    print('fetching business...')
    business_list = getFileContentToListAndFilter(business_path, 'city', '==', 'Toronto')
    business_list = filter(business_list, 'stars', '>=', 4)
    print('there are {} business located in Toronto and stars greater than 4'.format(len(business_list)))
    review_dict = {}
    for business in business_list:
        review_dict[business['business_id']] = 0
    business_id_list = review_dict.keys()
    # print(len(business_id_list))
    print('fetching review...')
    review_list = getFileContentToListAndFilter(review_path, 'business_id', 'in', business_id_list)
    print('there are {} reviews relating to their business'.format(len(review_list)))
    for review in review_list:
        # if review['business_id'] in business_id_list:
        review_dict[review['business_id']] += 1
    sorted_keys = sorted(review_dict, key=review_dict.get, reverse=True)[:10]
    # print(len(sorted_keys))
    result_list = []
    for k in sorted_keys:
        result_list.append({
            'business_id': k,
            'review_count': review_dict[k]
        })
    business_ids = [r['business_id'] for r in result_list]
    print('top 10 business ids: {}'.format(business_ids))
    business_list = filter(business_list, 'business_id', 'in', business_ids)
    return business_list

if __name__ == '__main__':
    business_list = mastmatch('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json')
    print('top 10 business details: {}'.format([b['name'] for b in business_list]))
    with open('./output/mastmatch.json', 'w+') as f:
        json.dump(business_list, f)


