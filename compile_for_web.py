#!usr/bin/python
import os
import re

scriptRegex=re.compile('src=(?:\"|\')(.*?js)')

def getScript(scriptName):
	f=open(scriptName,"r")
	scriptContent=f.read()
	f.close()
	return scriptContent

def compile(sourceFile="index.html"):
	f=open(sourceFile,"r")
	htmlContent=f.read()
	f.close()
	print(htmlContent)
	while re.search(scriptRegex,htmlContent):
		scripts = re.search(scriptRegex,htmlContent)
		scriptName = scripts.groups()[0]
		print(scriptName)
		scriptPos = htmlContent.find(scriptName)
		print (scriptPos)
		insertPos = htmlContent.find(">",scriptPos)
		htmlContent = htmlContent[:insertPos]+getScript(scriptName)+htmlContent[insertPos:]
	saveFile=open(sourceFile[:-5]+"_compiled.html","w")
	saveFile.write(htmlContent)
	saveFile.close()



def main():
	compile()

if __name__ == '__main__':
	main()
