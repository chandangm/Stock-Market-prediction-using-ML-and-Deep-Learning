"""Since there are no APIs to get stock market data , and recent changes in the yahoo finance api calls. This is a custom
built downloader which downloads the stock market files , by default downloads NIFTY50 data of a year """
import re
import urllib2
import calendar
import datetime
import getopt
import sys
import time
import progressbar

crumble_link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
crumble_regex = r'CrumbStore":{"crumb":"(.*?)"}'
cookie_regex = r'Set-Cookie: (.*?); '
quote_link = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&crumb={}'

def converttostockindices():
    """returns stock names"""
	f=open("result.csv","r")
	readchar=f.read()
	listval =[]
	listval=readchar.split()[3:]
	print listval
	return listval

def getdates():
    """returns start and end dates for the stock market file"""
	today = datetime.datetime.now()
	s_d=today.strftime("%Y-%m-%d")
	print "Start Date--  "+s_d
	DD = datetime.timedelta(days=365)
	earlier = today - DD
	e_d= earlier.strftime("%Y-%m-%d")
	print "End Date--  "+e_d
	print s_d,e_d
	return str(e_d),str(s_d)

def get_crumble_and_cookie(symbol):
    """gets auth keys for the url i.e. crumble and coookie"""
    link = crumble_link.format(symbol)
    response = urllib2.urlopen(link)
    match = re.search(cookie_regex, str(response.info()))
    cookie_str = match.group(1)
    text = response.read()
    match = re.search(crumble_regex, text)
    crumble_str = match.group(1)
    return crumble_str, cookie_str


def download_quote(symbol, date_from, date_to):
    """downloads the stock file"""
    time_stamp_from = calendar.timegm(datetime.datetime.strptime(date_from, "%Y-%m-%d").timetuple())
    time_stamp_to = calendar.timegm(datetime.datetime.strptime(date_to, "%Y-%m-%d").timetuple())

    attempts = 0
    while attempts < 5:
        #crumble_str, cookie_str = get_crumble_and_cookie(symbol)
        link = quote_link.format(symbol, time_stamp_from, time_stamp_to, crumble_str)
        #print link
        r = urllib2.Request(link, headers={'Cookie': cookie_str})

        try:
            response = urllib2.urlopen(r)
            text = response.read()
            #print "{} downloaded".format(symbol)
            return text
        except urllib2.URLError:
            print "{} failed at attempt # {}".format(symbol, attempts)
            attempts += 1
            time.sleep(2*attempts)
    return ""

if __name__ == '__main__':
    crumble_str, cookie_str =get_crumble_and_cookie('KO')
    bar = progressbar.ProgressBar(redirect_stdout=True)
    from_val,to_val=getdates()
    stock=converttostockindices()
    for i in bar(xrange(len(stock))):
    	s=stock[i]+".NS"
        #print "downloading {}".format(s)
        text = download_quote(s,from_val,to_val)
        #print text
        with open("./testfilesNS/"+stock[i]+".csv", 'wb') as f:
            f.write(text)
        f.close()
        print "------ {} ----".format(stock[i])




    





