from sklearn import tree 
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
#first element is weight & second is texture (0 is bumpy, 1 is smooth )
labels = [0, 0, 1, 1] 
#0 for apples 1 for oranges
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
if(clf.predict([[150, 0]]) == 0):
	print "apples"
print "oranges"