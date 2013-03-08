import urllib2
import string
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print data

proxy = urllib2.ProxyHandler({"http":"http://120.203.215.6:80"})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

html = urllib2.urlopen("http://www.whatismyip.com").read()
start = string.find(html, "<div id=\"greenip\">")
finish = start + string.find(html[start:], "</div>")

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
relevant = HTMLParser.unescape.__func__(MyHTMLParser, html[start:finish])
parser.feed(relevant)

