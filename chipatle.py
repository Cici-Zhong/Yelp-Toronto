from utils import *

import sys

def chipatle(business_path, review_path, business_name):
    business_list = getFileContentToListAndFilter(business_path, 'name', '==', business_name)
    if len(business_list) == 0:
        print('not find business with name {}'.format(business_name))
        sys.exit()
    else:
        business_id = business_list[0]['business_id']
        print('find business with name {} has id {}'.format(business_name, business_id))
        review_list = getFileContentToListAndFilter(review_path, 'business_id', '==', business_id)
        print('find {} reviews relating to {}'.format(len(review_list), business_id))
        review_text_dict = {}
        rep_regex = [',', '.', '?', '!', '"', "'"]
        # ignored_words = ['to', 'the', 'is', 'this', 'and', 'a', 'it', 'I', 'you']
        for review in review_list:
            words = str(review['text'])
            for regex in rep_regex:
                words = words.replace(regex, "")
            words = words.split(" ")
            for word in words:
                # if word not in ignored_words:
                if word in review_text_dict.keys():
                    review_text_dict[word] += 1
                else:
                    review_text_dict[word] = 1
        sorted_keys = sorted(review_text_dict, key=review_text_dict.get, reverse=True)[:10]
        result_list = []
        for key in sorted_keys:
            result_list.append([key, review_text_dict[key]])
        print(result_list)
        return sorted_keys

if __name__ == '__main__':
    words = chipatle('./yelp_dataset/yelp_academic_dataset_business.json', './yelp_dataset/yelp_academic_dataset_review.json', 'Chipotle Mexican Grill')
    print(words)
    # ['to', 'the', 'is', 'this', 'and', 'a', 'it', 'location', 'I', 'you']

