#!usr/bin/python
htmlContent=open("index.html","r").read()
while re.search(__import__("re").compile("src=(?:\"|\")(.*?js)"),htmlContent):htmlContent=htmlContent[:htmlContent.find(">",htmlContent.find(re.search(__import__("re").compile("src=(?:\"|\")(.*?js)"),htmlContent).groups()[0]))]+open(re.search(__import__("re").compile("src=(?:\"|\")(.*?js)"),htmlContent).groups()[0],"r").read()+htmlContent[htmlContent.find(">",htmlContent.find(re.search(__import__("re").compile("src=(?:\"|\")(.*?js)"),htmlContent).groups()[0])):]
open(f"{\"index.html\"[:-5]}_compiled.html","w").write(htmlContent)
