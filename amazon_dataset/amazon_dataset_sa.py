import gzip
import json


def parse(path):
    opened_zip = gzip.open(path, 'r')
    for line in opened_zip:
        yield json.dumps(eval(line))


if __name__ == '__main__':
    i = 0
    for file_line in parse("C:\\Users\\leoca\\Desktop\\datasets_sa\\amazon_dataset_electronics.json.gz"):
        print(file_line + '\n')
        i += 1
        if i > 100:
            break
