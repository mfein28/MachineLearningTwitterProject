import sklearn
import numpy as np
from sklearn import preprocessing, neighbors, svm
from sklearn.metrics import accuracy_score, log_loss, recall_score, precision_recall_curve, precision_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis



import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate
import pandas as pd


class MachineLearn:
    trainTweets = pd.read_csv('/Users/mattfein/PycharmProjects/twitterpull/April14.csv')
    # bernieTweets = pd.read_csv('/Users/mattfein/PycharmProjects/twitterpull/CSVFiles/codedBernWithID.tsv', sep='\t')
    yTrain = trainTweets.iloc[:, 12]
    xTest = trainTweets.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    #Features
    xTest.columns = ['User Reported Location', 'Hashtags in Bio', 'Tags in Bio', 'Emojis in Bio', 'Account Language', 'Tweet Language', 'Hashtags in Tweet', 'URLs in Tweet', 'TaggedCount','TweetEmojiCount','Tweet Client', 'Is User Verified?']
    xTest = xTest.fillna(0)
    yTrain = yTrain.fillna(0)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(xTest, yTrain, test_size=0.3, random_state=0)

    logmodel = LogisticRegression(solver='lbfgs', max_iter=4000)
    clf = tree.DecisionTreeClassifier()
    svc = SVC(gamma='scale')
    gradient = GradientBoostingClassifier()
    rfc = RandomForestClassifier(n_estimators=50)
    gaussian = GaussianNB()
    # quadDiscri = QuadraticDiscriminantAnalysis()
    kneighbors = KNeighborsClassifier(n_neighbors=2)
    kneighbors.fit(X_train, y_train)
    svc.fit(X_train, y_train)

    gradient.fit(X_train, y_train)
    logmodel.fit(X_train, y_train)
    clf.fit(X_train, y_train)
    # quadDiscri.fit(X_train, y_train)
    rfc.fit(X_train, y_train)
    gaussian.fit(X_train, y_train)
    predictions = logmodel.predict(X_test)
    gradientPred = gradient.predict(X_test)
    kpred = kneighbors.predict(X_test)
    # quadPred = quadDiscri.predict(X_test)
    svcPred = svc.predict(X_test)
    forestpred = clf.predict(X_test)
    randomforestpred = rfc.predict(X_test)

    modelsforVis = []
    modelsforVis.append(('Logistic\nRegression', logmodel))
    modelsforVis.append(('Decision\nTree', clf))
    modelsforVis.append(('SVM', svc))
    modelsforVis.append(('Gradient\nBoost', gradient))
    modelsforVis.append(('Random\nForest', rfc))
    modelsforVis.append(('Gaussian', gaussian))
    modelsforVis.append(('K\nNeighbors', kneighbors))
    results = []
    names = []
    scoring = 'recall'
    seed = 7
    for name, model in modelsforVis:
        kfold = sklearn.model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = sklearn.model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())

    fig = plt.figure()
    plt.ylabel('Recall')
    plt.title('Algorithm Recall Comparison')
    ax = fig.add_subplot(111)
    box = plt.boxplot(results, patch_artist=True)
    color = 'cornflowerblue'
    for median in box['medians']:
        median.set(color=color)

    for face in box['boxes']:
        face.set_facecolor('white')

    ax.set_xticklabels(names)
    plt.savefig('Recall.png', format='png', dpi=500)
    plt.show()

    results = []
    names = []
    scoring = 'precision'
    seed = 7
    for name, model in modelsforVis:
        kfold = sklearn.model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = sklearn.model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())


    fig = plt.figure()
    plt.ylabel('Precision')
    plt.title('Algorithm Precision Comparison')
    ax = fig.add_subplot(111)
    box = plt.boxplot(results, patch_artist=True)
    color = 'cornflowerblue'
    for median in box['medians']:
        median.set(color=color)

    for face in box['boxes']:
        face.set_facecolor('white')

    ax.set_xticklabels(names)
    plt.savefig('Precision.png', format='png', dpi=500)
    plt.show()

    results = []
    names = []
    scoring = 'accuracy'
    seed = 7
    for name, model in modelsforVis:
        kfold = sklearn.model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = sklearn.model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())

    fig = plt.figure()
    plt.ylabel('Accuracy')
    plt.title('Algorithm Accuracy Comparison')
    ax = fig.add_subplot(111)
    box = plt.boxplot(results, patch_artist=True, )
    color = 'cornflowerblue'
    for median in box['medians']:
        median.set(color=color)

    for face in box['boxes']:
        face.set_facecolor('white')
    ax.set_xticklabels(names)
    plt.savefig('Accuracy.png', format='png', dpi=500)
    plt.show()


    importances = clf.feature_importances_
    std = np.std([tree.feature_importances_ for tree in rfc.estimators_],axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    print("Feature ranking:")

    for f in range(xTest.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
    gaussianPred = gaussian.predict(X_test)

    print("Logistic Regression Accuracy: ", accuracy_score(y_test, predictions))
    print("Logistic Regression Log Loss: ", log_loss(y_test, predictions))
    print("Logistic Regression Precision: ", precision_score(y_test, predictions))
    print("Logistic Regression Recall: ", recall_score(y_test, predictions), '\n\n')
    print("K-Neighbors Accuracy: ", accuracy_score(y_test, kpred))
    print("K-Neighbors Log Loss: ", log_loss(y_test, kpred))
    print("K-Neighbors Precision: ", precision_score(y_test, kpred))
    print("K-Neighbors Recall: ", recall_score(y_test, kpred), '\n\n')

    print("Decision Tree Accuracy: ", accuracy_score(y_test, forestpred))
    print("Decision Tree Log Loss: ", log_loss(y_test, forestpred))
    print("Decision Tree Precision: ", precision_score(y_test, forestpred))
    print("Decision Tree Recall: ", recall_score(y_test, forestpred), '\n\n')


    print("Random Forest Accuracy: ", accuracy_score(y_test, randomforestpred))
    print("Random Forest Log Loss: ", log_loss(y_test, randomforestpred))
    print("Random Forest Precision: ", precision_score(y_test, randomforestpred))
    print("Random Forest Recall: ", recall_score(y_test, randomforestpred), '\n\n')


    print("SVC Accuracy: ", accuracy_score(y_test, svcPred))
    print("SVC Log Loss: ", log_loss(y_test, svcPred))
    print("SVC Precision: ", precision_score(y_test, svcPred))
    print("SVC Recall: ", recall_score(y_test, svcPred), '\n\n')

    print("Gradient Boosting Accuracy: ", accuracy_score(y_test, gradientPred))
    print("Gradient Boost Loss: ", log_loss(y_test, gradientPred))
    print("Gradient Boost Precision: ", precision_score(y_test, gradientPred))
    print("Gradient Boost Recall: ", recall_score(y_test, gradientPred), '\n\n')

    # print("Quadratic Discriminant Accuracy: ", accuracy_score(y_test, quadPred))
    #     # print("Quadratic Discriminant Loss: ", log_loss(y_test, quadPred))
    #     # print("Quadratic Precision: ", precision_score(y_test, quadPred))
    #     # print("Quadratic Recall: ", recall_score(y_test, quadPred), '\n\n')

    print("Gaussian Accuracy: ", accuracy_score(y_test, gaussianPred))
    print("Gaussian Loss: ", log_loss(y_test, gaussianPred))
    print("Gaussian Precision: ", precision_score(y_test, gaussianPred))
    print("Gaussian Recall: ", recall_score(y_test, gaussianPred), '\n\n')



machine = MachineLearn()
machine
