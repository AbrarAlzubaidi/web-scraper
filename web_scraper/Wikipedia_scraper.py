import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

# class="noprint Inline-Template Template-Fact"
def get_citations_needed_count(URL):
    page= requests.get(URL)

    soup=BeautifulSoup(page.content,'html.parser')

    a_results=soup.find(class_='mw-parser-output')

    citations=a_results.findAll('a',title='Wikipedia:Citation needed')

    return (len(citations))


def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    a_results = soup.find(class_="mw-parser-output")
    p_results = a_results.findAll('p')
    citation_p=[]
    for i in p_results:
        citation_result=i.findAll('a',title='Wikipedia:Citation needed')
        for j in citation_result:
            citation_p.append(i.text.strip()) 
    return "\n".join(citation_p)

print('number of citations is = ',get_citations_needed_count(URL))
print('report:\n',get_citations_needed_report(URL))