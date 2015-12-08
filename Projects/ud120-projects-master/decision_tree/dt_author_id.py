#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier(min_samples_split=40)

#train
t0 = time()
clf.fit(features_train,labels_train)

print "training time:", round(time()-t0,3), "s"

#compute the accuracy on test data set

t0 = time()
y_pred = clf.predict(features_test)
print "predicting time:", round(time()-t0,3), "s"
#compute the accuracy
acc = accuracy_score(labels_test,y_pred)

print "accuracy: ", round(acc,4)
#test_time = time.clock() - start_time
#########################################################


