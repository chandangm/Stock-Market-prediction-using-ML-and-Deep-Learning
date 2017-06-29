import glob,os,sys
import NeuralNet
import SVM
import bayes
import KNN
import mix
import pandas as pd
from optparse import OptionParser
import standardinput
import numpy as np
import time
import progressbar

def acc_neuralnet():
	"""basic neural net to check how good it can build a model , and as a comparsion to hybrid model"""
	ind=0
	report=pd.DataFrame(index=range(0),columns=['Stock Name','accuracy','profit count','loss count','total no of rise','total number of loss'])
	for i in bar(xrange(len(x))):
		p_count,total_count_p,l_count,total_count_l,accuracy=NeuralNet.neuralnet(x[i])
		report.loc[ind]=[x[i],accuracy,p_count,l_count,total_count_p,total_count_l]
		ind=ind+1
	print "Mean accuracy----------",report['accuracy'].mean()
	report.to_csv("./report/neuralnet_results.csv")

def svm():
	"""custom created from scratch specifically designed to enchance the prediction accuracy of stock market data"""
	ind=0
	report=pd.DataFrame(index=range(0),columns=['Stock Name','accuracy','profit count','loss count','total no of rise','total number of loss'])
	for i in bar(xrange(len(x))):
		try:
			p_count,total_count_p,l_count,total_count_l,accuracy=SVM.svm_model(x[i])
			report.loc[ind]=[x[i],accuracy,p_count,l_count,total_count_p,total_count_l]
			ind=ind+1
			print "",
			sys.stdout.flush()
		except: pass
	print "Mean accuracy----------",report['accuracy'].mean()
	report.to_csv("./report/svm_results.csv")

def naive_bayes():
	"""custom created from scratch specifically designed to enchance the prediction accuracy of stock market data"""
	ind=0
	report=pd.DataFrame(index=range(0),columns=['Stock Name','accuracy','profit count','loss count','total no of rise','total number of loss'])
	for i in bar(xrange(len(x))):
		try:
			p_count,total_count_p,l_count,total_count_l,accuracy=bayes.naive_bayes_model(x[i])
			report.loc[ind]=[x[i],accuracy,p_count,l_count,total_count_p,total_count_l]
			ind=ind+1
		except: pass
	print "Mean accuracy----------",report['accuracy'].mean()
	report.to_csv("./report/bayes_results.csv")

def knn():
	"""custom created KNN algorithm from scratch specifically designed to enchance the prediction accuracy of stock market data 
	new distance measure is used to find the nearest neighbors,which gives an boost of 8% on average in prediction 
	accuracy """
	ind=0
	report=pd.DataFrame(index=range(0),columns=['Stock Name','accuracy','profit count','loss count','total no of rise','total number of loss'])
	for i in bar(xrange(len(x))):
		p_count,total_count_p,l_count,total_count_l,accuracy=KNN.knn_algo_model(x[i])
		report.loc[ind]=[x[i],accuracy,p_count,l_count,total_count_p,total_count_l]
		ind=ind+1
	print "Mean accuracy----------",report['accuracy'].mean()
	report.to_csv("./report/KNN_results.csv")

def mix_up():
	"""creating a hybrid model mixing ML algorithms and neural net , it accumulates the errors from individual algorithms 
	and it increases the error in neural net so much that the model is not flexible enough to decide the trend in market
	or find patterns in data , model2 removes that redundant error ."""
	ind=0
	for i in bar(xrange(len(x))):
		b_pred,b_y=bayes.naive_bayes_model(x[i],net=True)
		s_pred,s_y=SVM.svm_model(x[i],net=True)
		k_pred,k_y=KNN.knn_algo_model(x[i],net=True)
		print b_pred,b_y
		mix.new_net(s_pred,b_pred,k_pred,s_y,x[i])
	ind=0
	report=pd.DataFrame(index=range(0),columns=['Stock Name','accuracy','profit count','loss count','total no of rise','total number of loss'])
	for i in bar(xrange(len(x))):
		b_pred,b_y=bayes.naive_bayes_model(x[i],net=True,actual=True)
		s_pred,s_y=SVM.svm_model(x[i],net=True,actual=True)
		k_pred,k_y=KNN.knn_algo_model(x[i],net=True,actual=True)
		p_count,total_count_p,l_count,total_count_l,accuracy=mix.new_net(s_pred,b_pred,k_pred,s_y,x[i],create=False) 
		report.loc[ind]=[x[i],accuracy,p_count,l_count,total_count_p,total_count_l]
		ind=ind+1
	print "Mean accuracy----------",report['accuracy'].mean()
	report.to_csv("./report/mix_result.csv")

def test_model2():
	"""A Sort of noise is introduced to remove redundancy error from all the ML algorithms,
	this makes the model more flexible and in turn increases the accuracy ."""
	ind=0
	pred=[]
	report=pd.DataFrame(index=range(0),columns=['Stock Name','accuracy','profit count','loss count','total no of rise','total number of loss'])
	for i in bar(xrange(len(x))):
		try:
			k_pred,k_y=KNN.knn_algo_model(x[i],net=True)
			b_pred,b_y=bayes.naive_bayes_model(x[i],net=True)
			s_pred,s_y=SVM.svm_model(x[i],net=True)
			p_count,total_count_p,l_count,total_count_l,accuracy=mix.model1(s_pred,b_pred,k_pred,s_y,x[i])
			report.loc[ind]=[x[i],accuracy,p_count,l_count,total_count_p,total_count_l]
			ind=ind+1
		except: 
			print "!!!!!############ error"	
	print "Mean accuracy----------",report['accuracy'].mean()
	report.to_csv("./report/mix_model2_result.csv")


listoffiles=glob.glob("./ns/*.csv")
x=[x.split('/')[::-1][0] for x in listoffiles]
bar = progressbar.ProgressBar(redirect_stdout=True)
def PF():
	"""proprietary data processing to build patterns in stock market data.
	which increased the accuracy of the all the model/algorithms by 11-20%"""
	print "------------------Processing files for model-----------------------"
	for i in xrange(len(x)):
		try:
			standardinput.process_file(listoffiles[i],x[i])
		except:
			print "ERROR"+x[i]
	print "-----------------Completed---------------------"

parser=OptionParser()
parser.add_option("-t","--type",type="string",help="type of function you want to run",dest="type")
options,arguments = parser.parse_args()

if options.type == "neuralnet":
	print "--------------RUNNING NEURAL NET----------------"
	acc_neuralnet() #Runs a normal Neuralnet
	print "-------------Computations Completed-------------"
if options.type == "svm":
	print "-----------------RUNNING SVM-------------------"
	svm() # enchanced for stock market prediction 
	print "-------------Computations Completed-------------"
if options.type == "naivebayes":
	print "-----------------RUNNING NAIVE BAYES-------------------"
	naive_bayes() # enchanced for stock market prediction 
	print "-------------Computations Completed-------------"
if options.type == "KNN":
	print "-----------------RUNNING KNN-------------------"
	knn() # enchanced for stock market prediction 
	print "-------------Computations Completed-------------"
if options.type == "mix":
	print "-----------------RUNNING MIX-------------------"
	mix_up() # mixes multiple ML algorithms with neural net to increase accuracy of the model  
	print "-------------Computations Completed-------------"
if options.type == "model2_test":
	print "-----------------RUNNING MODEL 1 test-------------------"
	test_model2() # enhanced model from previous step by removing the redundancy error accumulated by mixing ML algo 
	print "-------------Computations Completed-------------"
if options.type == "PF":
	print "-----------------RUNNING FIles-------------------"
	PF() #proprietary data processing 
	print "-------------Computations Completed-------------"


def no_opt():
    print "Usage - python [FILENAME] [-t or --type] [neuralnet or svm]"