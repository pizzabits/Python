
import urllib2
import string
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
print HTMLParser.unescape.__func__(HTMLParser, "&#49;")

#parser.feed("<label id=\"e644571\">michael</label><label id=\"e319889\">&#49;</label><span id=\"g687448\">.</span><span id=\"f803526\">1</span>")
