from sklearn import tree

features = [[300, 2], [450, 2], [200, 8], [150, 9]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

f = int(input("Enter the horsepower: "))
f2 = int(input("Enter the number of seats: "))

l = clf.predict([[f, f2]])

if (l == 0):
    print("It is a sports car")
if (l == 1):
    print("It is a minivan")
