import urllib
import newspaper

articles=[]
cnn=newspaper.build('http://cnn.com')
mashable=newspaper.build('http://mashable.com')
bbc=newspaper.build('http://www.bbc.com')
theguardian=newspaper.build('http://www.theguardian.com/world')
cbc=newspaper.build('http://www.cbc.ca/')
aljazeera=newspaper.build('http://america.aljazeera.com/topics/topic/categories/international.html')
africa=newspaper.build('http://allafrica.com/')
rgazette=newspaper.build('http://www.royalgazette.com/')
bernews=newspaper.build('http://bernews.com/')
'''
for article in rgazette.articles:
    articles.append(article)
    break
'''
# for article in bernews.articles:
#	articles.append(article)


count = 0
'''
for article in cnn.articles:
    articles.append(article)
    count += 1
    if count == 1: 
        count = 0 
        break
'''
'''
for article in mashable.articles:
    articles.append(article)
    count +=1 
    if count == 5: break
'''

for article in bbc.articles:
    articles.append(article)
    count += 1
    if count == 50: 
        count = 0 
        break 

'''
for article in theguardian.articles:
    articles.append(article)
    count += 1
    if count == 1: 
        count = 0
        break 
'''
'''
for article in cbc.articles:
    articles.append(article)
    count += 1
    if count == 6: break
'''
'''
for article in aljazeera.articles:
    articles.append(article)
    count += 1
    if count == 1: 
        count = 0 
        break
'''
print articles

for a in articles:
    a.download()
    a.parse()
    print "URL: " + str(a.url)
    print "PUBLISH DATE: " + str(a.publish_date)
    print "this is an IMAGE URL: " + str(a.top_image)
    print "\n"
