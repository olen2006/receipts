
import random # for generating receipts numbers
import json #receiptsd in json format
import os #adding a little bit of customizibility to the script using env vars

#how many receipts we want to generate for account testing purposes
count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000) #between $1 and $1000
    #creating a dictionary
    content = {
            'topic': random.choice(words),
            'value': "%.2f" %amount
            }
    #choice returns random words from list
    #https://docs.python.org/3/library/random.html#random.choice
    # 2 numbers after . and make it type = float
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        #dumping dictionary content into the file
        json.dump(content, f)
        #https://docs.python.org/3/library/json.html#basic-usage

