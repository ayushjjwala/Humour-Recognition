import get_feature
from sklearn.svm import SVC
from random import shuffle
import numpy as np

data = []

def get_data():
	fo = open('author-quote.txt','r+')
	a = fo.readlines()
	a = [x for x in a if x!='\n']
	for line in a:
		data.append(line[:-1] + '\t' +'0')
	fo.close()

	fo = open('Jokes16000.txt','r+')
	a = fo.readlines()
	a = [x for x in a if x!='\n']
	for line in a:
		data.append(line[:-1] + '\t' + '1')
	fo.close()
	shuffle(data)
	# print len(data)

def separate_data(test_start,test_end):
	train_feature_matrix = []
	test_feature_matrix = []
	train_data_matrix = []
	test_data_matrix = []
	for j in xrange(len(data)):
		basic_matrix = [get_feature.check_alliteration(data[j][:-1]), get_feature.check_antonyms(data[j][:-1]), get_feature.check_slang(data[j][:-1])]
		if j>= test_start and j<= test_end:
			test_data_matrix.append(data[j])
			test_feature_matrix.append(basic_matrix)
		else:
			train_data_matrix.append(int(data[j][-1]))
			train_feature_matrix.append(basic_matrix)
	return [train_data_matrix,train_feature_matrix,test_data_matrix,test_feature_matrix]

def main():
	get_data()
	for i in xrange(10):
		print "Fold:",i+1
		accuracy = 0
		test_count = 0
		test_start = (9-i)*(52165/10) 
		test_end =  (10-i)*(52165/10) - 1
		temp = separate_data(test_start,test_end)
		train_data_matrix = temp[0]
		train_feature_matrix = temp[1]
		test_data_matrix = temp[2]
		test_feature_matrix = temp[3]

		x = np.array(train_feature_matrix)
		y = train_data_matrix
		clf = SVC()
		clf.fit(x,y)

		for j in xrange(len(test_data_matrix)):
			train_reg_pred = clf.predict([test_feature_matrix[j]])
			if int(test_data_matrix[j][-1]) == train_reg_pred[0]:
				accuracy += 1.0
			test_count += 1.0

		print "Accuracy: + " + str(accuracy) + " Total: " + str(test_count)
		print "Percent:",(accuracy/test_count)*100

main()