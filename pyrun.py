import json
import csv

from os import listdir
from os.path import isfile, join

import sys, getopt

def isJson(filename):
    return True if filename.endswith('.json') else False

def getJsonList(path):
    return [f for f in listdir(path) if (isfile(join(path, f)) and isJson(f))]

def convert_json_to_csv(json_dir, csv_dir):
    files = getJsonList(json_dir)
    for file in files:
        csv_file = "{}.csv".format(file.split('.json')[0])
        csv_path = join(csv_dir, csv_file)
        print('converting {} to {}'.format(file, csv_path))
        lines = [line.rstrip('\n') for line in open(join(json_dir, file))]
        keys = list(json.loads(lines[0]).keys())
        
        with open(csv_path, 'a+') as f:
            f.write(','.join(keys))
            f.write('\n')
            for line in lines:
                line_dic = json.loads(line)
                values = []
                for key in keys:
                    line_dic[key] = '"{}"'.format(str(line_dic[key]).replace('"', '""'))
                    values.append(line_dic[key])
                f.write(','.join(values))
                f.write('\n')
        print('converting ')
    
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hj:c:",["jsondir=","cvsdir="])
    except getopt.GetoptError:
        print('python3 convert_json_to_csv.js -j <json dir> -c <cvs dir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python3 convert_json_to_csv.js -j <json dir> -c <cvs dir>')
            sys.exit()
        elif opt in ('-j', '--jsondir'):
            jsondir = arg
        elif opt in ('-c', '--csvdir'):
            csvdir = arg
    convert_json_to_csv(jsondir, csvdir)
