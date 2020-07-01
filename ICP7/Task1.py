from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.svm import SVC

categories = ['rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics']
#Reading the data
twenty_train = fetch_20newsgroups(subset='train', shuffle=True, categories=categories)

#raw text data will be transformed into feature vectors
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

#Training the model
svc = SVC()
svc.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True, categories=categories)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = svc.predict(X_test_tfidf)
#Evaluating the model
score = metrics.accuracy_score(twenty_test.target, predicted)
print('SVC score : ', round(score*100,2))

#Bigram
tfidf_Vect1 = TfidfVectorizer(ngram_range=(1,2))
X_train_tfidf1 = tfidf_Vect1.fit_transform(twenty_train.data)
svc1 = SVC()
svc1.fit(X_train_tfidf1, twenty_train.target)
X_test_tfidf1 = tfidf_Vect1.transform(twenty_test.data)
predicted1 = svc1.predict(X_test_tfidf1)
score1 = metrics.accuracy_score(twenty_test.target, predicted1)
print('using npgram score : ', round(score1*100,2))

#Setting argument stop_words='english'
tfidf_Vect2 = TfidfVectorizer(stop_words='english')
X_train_tfidf2 = tfidf_Vect2.fit_transform(twenty_train.data)
# print(tfidf_Vect.vocabulary_)
svc2 = SVC()
svc2.fit(X_train_tfidf2, twenty_train.target)
X_test_tfidf2 = tfidf_Vect2.transform(twenty_test.data)
predicted2 = svc2.predict(X_test_tfidf2)
score2 = metrics.accuracy_score(twenty_test.target, predicted2)
print('using stop words score :  ' , round(score2*100,2))

# Observation : Accuracy increases
print("Observation : Accuracy increases by removing stop words")