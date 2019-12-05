# CS506 Final Project - Boston Airbnb Open Data Analysis

***Note: The [project report](https://github.com/feiyue33/cs506-final-project/blob/master/result/proj_report.pdf) is attacted in [result](https://github.com/feiyue33/cs506-final-project/tree/master/result) folder. ***

## Introduction
Airbnb has successfully disrupted the traditional hospitality industry as more and more travelers decide to use Airbnb as their primary accommodation provider. Since its beginning in 2008, Airbnb has seen an enormous growth, with the number of rentals listed on its website growing exponentially each year.We want to explore how Airbnb is really being used in Boston.

## Prerequisite
To successfully run this project, please make sure you already installed these packages:
```sh
pip install nltk
```
```sh
pip install wordcloud
```
```sh
$ pip install google-cloud-translate
```
```sh
$ pip install guess_language-spirit
```
```sh
$ pip install vaderSentiment
```
```sh
$ pip install folium
```

## How to run
1. Clone the whole project to your desktop.
```sh
git clone git@github.com:feiyue33/cs506-final-project.git
```
2. Run .ipynb or .py file in [src](https://github.com/feiyue33/cs506-final-project/tree/master/src) folder.
	- preprocessing_eda.ipynb: preprocessing and exploraotory data analysis.
	- price_trend.ipynb: analysis of price trend by month or week
	- neighborhood_vibe.ipynb: analysis and description of vibe of each neighborhood in Boston
	- translate.py: translation using [Google Cloud Translation API](https://cloud.google.com/translate/docs/apis). The [translation result](https://github.com/feiyue33/cs506-final-project/blob/master/data/reviews_join_listings_translated.csv) is included in [data](https://github.com/feiyue33/cs506-final-project/tree/master/data) folder so running this file is not required.
	- sentimental_analysis.ipynb: sentimenntal analysis for user's review and final visualization. You can find the result web application [here](https://github.com/feiyue33/cs506-final-project/tree/master/result).
3. Feel free to explore more!

## Reference
- https://cloud.google.com/translate/docs/apis
- https://github.com/cjhutto/vaderSentiment
- https://pypi.org/project/guess_language-spirit/
- https://python-visualization.github.io/folium/
