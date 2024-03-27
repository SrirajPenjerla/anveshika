from bs4 import BeautifulSoup
import requests
import lxml
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Accept-Language": "en-US,en;q=0.5"}

def amazon_find(query):
    url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    results = soup.findAll("div", {'data-component-type':'s-search-result'})
    lis=[]
    print(lis)
    for result in results:
        price= result.find("span", {"class":"a-price-whole"})
        # title=query.upper()
        # title = soup.find("span", attrs={"id":'productTitle'})
        # title=title.string.strip()
        title = result.find("span", {"class":"a-size-medium a-color-base a-text-normal"}).text.strip()
        # result.find("span", title = re.compile(query).text.strip())
        if price:
            price = price.text.strip()
        else:
            price = "N/A"
        
        lis.append(f"{title} - ₹{price}.")
    return(lis)
# class="a-size-medium a-color-base a-text-normal"
# def amazon_find(query):
#     url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, "lxml")
#     results = soup.findAll("div", {'data-component-type':'s-search-result'})
#     lis=[]
#     for result in results:
#         price= result.find("span", {"class":"a-price-whole"})
#         # title = result.find("span", {"class":"a-size-medium a-color-base a-text-normal"}).text.strip()
#         # if title is NULL:
#         #     title=query
        
#         title=query
        
#         if price:
#             price = price.text.strip()
#         else:
#             price = "N/A"
        
#         lis.append(f"{title} - ₹{price}.")
#     return(lis)



def flipkart_find(query):
    url = "https://www.flipkart.com/search?q=" + query.replace(" ", "%20")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    results = soup.findAll("div", {'class':"_13oc-S" or "_4ddWXP"})
    lis=[]
    for result in results:
        price= result.find("div", {"class":"_30jeq3 _1_WHN1" })
        title = result.find("div", {'class':"_4rR01T" or "s1Q9rs"}).text.strip()
    #print(title)
        if price:
            price = price.text.strip()
        else:
            price = "N/A"
        
        lis.append(f" {title} - {price}.")
    return(lis)

#if __name__=='__main__':
#     while(1):
#         query = input("enter item you want to search ").lower()
#         num=int(input("press    1 ------> amazon    2-------> flipkart  \n"))
#         if num==1:
#             results=amazon_find(query)
#             print('\n'.join(results))
#         elif num==2:
#             results=flipkart_find(query)
#             print('\n'.join(results))
#         else:
#             print("no such number")
    
