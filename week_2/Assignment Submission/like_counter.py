import csv
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
def return_raw_html(url):
    res = requests.get(url)
    return res.content.decode()
def like_return(pg_name):
    
    base_url="https://www.facebook.com/"
    test1=return_raw_html((base_url+pg_name))
    soup = BeautifulSoup(test1,'html.parser')
    temp1=soup.find('span', {'class': '_52id _50f5 _50f7'})
    temp12=soup.find('span', {'class': '_50f8 _50f4 _5kx5'})
    _=temp12.extract()
    te1=temp1.text
    return te1.replace('\u200f', '')
def final_taker(csv_path):
    data_file=Path(f"{csv_path}")
    base_url="https://www.facebook.com/"
    df = pd.read_csv(data_file)
    likes=[]
    list1=df['FB_Page_Handle'].tolist()
    for name in range(len(list1)):
        temp=like_return(df['FB_Page_Handle'][name])
        likes.append(temp)
    df['Like_Count']=likes
    df.to_csv(data_file)
link=input(r"Enter Your link:")
final_taker(link)
