# IMDB reviews Sentiment Analysis

The point of this analysis is to classify reviews based on the writer's sentiment. The reviews are classified as either positive or negative, using Bag-of-Words.

The models tested are:

+ SVM
+ KNN
+ Decision Trees
+ Random Forest
+ AdaBoost
+ Naive Bayes

## Requirements

The file 'requirements.txt' contains a full list of the requirements to run the jupyter notebook that contains the code, and the file 'demo.py' that contains the demonstration code.

In summary, the entire project was created in Python 3.11, and the libraries used were Pandas, NumPy, Sklearn and Matplotlib among others.

## How to run the models

The models and the preparation of the data are contained in the 'IMDB-reviews-sentiment-analisi.ipynb' notebook located in the 'src' folder. This notebook contains the code for the hyperparameter tuning and the training of each model.

## How to test your own reviews

The code 'demo.py' contains a code that lets the user test a review of his choice and get a sentiment classification. The current iteration reads the model from the folder 'models', the review from the file 'demo' and gives a prediction based on that. At this point, the model used is svm classifier.

'demo.py' reads from the file 'review.txt' located in the 'demo' file, so the review has to be entered as a string in that file.