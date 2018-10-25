from bs4 import BeautifulSoup
import urllib

def nikkei():
    url = "http://www.nikkei.com/markets/kabu/"

    #urlにアクセスし、htmlが帰ってくる
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, "lxml")

    
    nikkei_ave = soup.find("span", class_="mkc-stock_prices").contents[0]

    print(nikkei_ave)
    
if __name__ == "__main__":
    nikkei()