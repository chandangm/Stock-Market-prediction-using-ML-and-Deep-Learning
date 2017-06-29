from optparse import OptionParser
import glob,os
import standardinput
import model as m
def files():
	listoffiles=glob.glob("./ns/*.csv")
	x=[x.split('/')[::-1][0] for x in listoffiles]
	for i in xrange(len(x)):
		standardinput.process_file(listoffiles[i],x[i],run=True)

def run_model_1():
	"""Model with redundancy errors from combining ML algorithms
	check report for detailed info"""
	print "running model 1"
	listoffiles=glob.glob("./actual/*.csv")
	x=[x.split('/')[::-1][0] for x in listoffiles]
	m.model_1(listoffiles,x)

def run_model_2():
	"""enchanced model which removes the redundancy errors,gives an acccuracy of 80-90%,
	check report for detailed info"""
	print "running model 2"
	listoffiles=glob.glob("./actual/*.csv")
	x=[x.split('/')[::-1][0] for x in listoffiles]
	m.model_2(listoffiles,x)


	

parser=OptionParser()
parser.add_option("-t","--type",type="string",help="type of function you want to run",dest="type")
options,arguments = parser.parse_args()

if options.type == "PF":
	print "--------------Processing files----------------"
	files()
	print "-------------Completed-------------"

if options.type == "model_1":
	print "----------------Running MODEL 1--------------"
	run_model_1()
	print "----------------COMPLETED--------------------"

if options.type == "model_2":
	print "----------------Running MODEL 2--------------"
	run_model_2()
	print "----------------COMPLETED--------------------"