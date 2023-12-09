# Some common utilities functions

import Scrap

def printConsole(text = ''):
	debugBkg = Scrap.Get('debug')
	Scrap.Set('debug',2)
	print text
	Scrap.Set('debug',debugBkg)


def ev(code = "1+1"):
	if Scrap.Get('debug') < 2:
		Scrap.Set('debug',2)
	print "Called: "+code+":"
	try:
		print eval(code)
	except:
		try:
			exec(code)
			print "executed"
		except:
			print "that didn't work"

