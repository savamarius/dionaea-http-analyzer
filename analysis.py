import sys
import glob
from termcolor import colored

path = sys.argv[1] + '/httpd*'
files = glob.glob(path)

for f in files:
        data = open(f,'r')
        line = data.readlines()
        
        s = line[0].lstrip("stream = [('in',b'").rstrip("'),\n").replace('\\x0d\\x0a','\n')
        print colored('[FILE] '+f,'green')
        print s
        data.close()
