# Stock-Market-prediction-using-ML-and-Deep-Learning
Using custom built ML Algorithms from scratch and combining it with the power of deep learning . This model tries to predict the stock market trend with a mean accuracy of 85% and above for a testing of over a year's data   

<b>down.py</b> - Stock market File Downloader </br>
<b>tester.py</b> - tester file for all the models and algorithm which returns a detailed report - SAVED in ./report </br>
<b>run.py</b> - module to return predictions and save it in ./report for all model </br>


<b>./testfilesNS</b> - downloaded NSE stock files. </br>
<b>./del</b> - testing and training sets.</br>
<b>./report</b> - detailed reports from model.


all the algorithms used in the project are custom built for stock market data from scratch .
Algorithms USED:

KNN - 45% - 60% accuracy,highly unreliable .</br>
SVM - 67% accuracy at best .</br>
NAIVE BAYES - 55% to 60% accuracy .</br> 

Ingestion Engine takes raw data from downloaded stock files and apply proprietary data manipulations to <b>enchance its accuracy by - 11-20%</b></br>
this data is fed as input for the model for prediction and testing .</br>
<b>MODEL 1</b> - <i>mixup()</i> - this model combines individual ML algorithms with neural net . But <i>it has a redundancy error from all the ML algorithms,</i>
accuracy of this model is <b>70%</b> which is basically a pessimistic model i.e. - NO FLEXIBLITY in decisions . 

<b>MODEL 2</b> - this model is an upgrade to model 1 , here the redundancy error is removed , gives a mean accuracy of <b>89.7 %</b>.
the model is quite flexible to predict loss and profit of the stock market . 

<b>Prediction Analysis for a stock:</b></br>
![Actual/Predicted line graph](/image/graph/ACC.png?raw=true "line Graph") </br>
![Profit/loss Area graph](/image/binary/AMBUJACEM.png?raw=true "Area Graph") </br>


PS : the implementation files for the model and algorithms are missing in this repository on purpose.For further info leave a message at chandangm33@gmail.com
<h3> Detailed report can be seen in ./report folder for differences in model and enchancments</h3>
