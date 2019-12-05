import numpy as np
import pandas as pd
from guess_language import guess_language
from google.cloud import translate
import os
import time
import random

airbnb = pd.read_csv('../data/summary-listings.csv')
reviews = pd.read_csv('../data/reviews_2019.csv')
reviews.drop(['id', ], axis=1, inplace=True)
listings = pd.read_csv('./data/listings_2019.csv')


# see if a string is english or not (simple version)
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


# drop some unused columns
airbnb.drop(['host_id','host_name','last_review', 'neighbourhood_group', 'minimum_nights', 'last_review'],
            axis=1, inplace=True)
# join two dataframe based on each of listings
new_df = pd.merge(airbnb, reviews, left_on='id', right_on='listing_id', how='left').drop('listing_id', axis=1)

# Some comments which contain "automated posting" are auto generated by Airbnb. So I need to drop these rows
indexes_to_drop = []
for i in new_df.index:
    if 'automated posting' in str(new_df.iloc[i]['comments']):
        indexes_to_drop.append(i)
new_df.drop(new_df.index[indexes_to_drop], inplace=True)

# translate the comments which are not English
credential_path = "Your own auth.json file of Google Cloud account"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

dataTranslated = []

translate_client = translate.Client()

i = 0
for index, row in new_df.iterrows():
    if index < 180000:
        continue
    if index % 100 == 0:
        print(index)
    sentence = str(row['comments'])
    if (guess_language(sentence) != 'en' and guess_language(sentence) != 'UNKNOWN') or (guess_language(sentence) == 'UNKNOWN' and not isEnglish(sentence)):
        # print(sentence)
        new_df.loc[index, 'comments'] = translate_client.translate(sentence, target_language='en')['translatedText']
        sleep = random.choice([.4, .45, .5, .55, .6, .65, .7])
        time.sleep(sleep)

# save to new file
new_df.to_csv("reviews_join_listings_translated.csv", index=False)