from utils import *

from mastmatch import *

def top10_in_lv(business_path, review_path):
    top_bis_in_on = mastmatch(business_path, review_path)
    top_bis_in_on = [b['business_id'] for b in top_bis_in_on]
    business_list = getFileContentToListAndFilter(business_path, 'business_id', 'in', top_bis_in_on)
    cat_set = set([])
    for business in business_list:
        if 'categories' in business.keys() and business['categories'] is not None:
            for cat in business['categories'].split(', '):
                cat_set.add(cat)
    cat_list = list(cat_set)
    print('get categories list: {}'.format(cat_list))
    business_list = getFileContentToListAndFilter(business_path, 'city', '==', 'Las Vegas')
    business_list = filter(business_list, 'stars', '>=', 4)
    filted_business_list = []
    for business in business_list:
        if 'categories' in business.keys() and business['categories'] is not None:
            try:
                business['categories'] = business['categories'].split(', ')
            except:
                print(business['categories'])
            filted_business_list.append(business)
    print('find {} business in Las Vegas, and stars >= 4'.format(len(business_list)))
    business_ids_list = [b['business_id'] for b in filted_business_list if len(set(b['categories']) & set(cat_list)) > 0]
    review_list = getFileContentToListAndFilter(review_path, 'business_id', 'in', business_ids_list)
    business_dict = {}
    for business_id in business_ids_list:
        business_dict[business_id] = len([r for r in review_list if r['business_id'] == business_id])
    sorted_keys = sorted(business_dict, key=business_dict.get, reverse=True)[:10]
    result_list = []
    for key in sorted_keys:
        result_list.append({
            'business_id': key,
            'review_count': business_dict[key]
        })
    return result_list

if __name__ == '__main__':
    business_list = top10_in_lv('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json')
    print(business_list)
    # business_list = [{'business_id': '4JNXUYY8wbaaDmk3BPzlWw', 'review_count': 7968}, {'business_id': 'RESDUcs7fIiihp38-d6_6g', 'review_count': 7861}, {'business_id': 'cYwJA2A6I12KNkm2rtXd5g', 'review_count': 5472}, {'business_id': 'f4x1YBxkLrZg652xt2KR5g', 'review_count': 5382}, {'business_id': 'DkYS3arLOhA8si5uUEmHOw', 'review_count': 4981}, {'business_id': 'iCQpiavjjPzJ5_3gPD5Ebg', 'review_count': 4078}, {'business_id': 'KskYqH1Bi7Z_61pH6Om8pg', 'review_count': 3976}, {'business_id': 'rcaPajgKOJC2vo_l3xa42A', 'review_count': 3742}, {'business_id': 'hihud--QRriCYZw1zZvW4g', 'review_count': 3733}, {'business_id': '7sPNbCx7vGAaH7SbNPZ6oA', 'review_count': 3249}]
    business_list = getFileContentToListAndFilter('./yelp_dataset/yelp_academic_dataset_business.json', 'business_id', 'in', [b['business_id'] for b in business_list])
    print(business_list)

    
