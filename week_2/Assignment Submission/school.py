import csv
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json
import pandas as pd
import time
def school_return(num):
    schools= requests.get("https://directory.ntschools.net/api/System/GetAllSchools")
    base_url="https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="
    skool_dir = json.loads(schools.content)
    skool_content=requests.get(base_url+skool_dir[num]["itSchoolCode"])
    return json.loads(skool_content.content)
def data_savior():
    list123=[]
    data_file=Path(r"C:\Users\Hassam Jawed\projects\requests\schools.csv")
    df = pd.read_csv(data_file)
    for i in range(50):
        time.sleep(2)
        content=school_return(i)
        datadict={}
        name=content['name']
        address=content['physicalAddress']['displayAddress']
        
        for i in range(len(content['schoolManagement'])):
            if content['schoolManagement'][i]['position']=='Principal':
                principal=(content['schoolManagement'][i]['firstName'])+' '+(content['schoolManagement'][i]['lastName'])
                principal_no=content['schoolManagement'][i]['phone']
                principal_email=content['schoolManagement'][i]['email']
                datadict["Name"]=name
                datadict['Address']=address
                datadict['Principal/Admin Name']=principal
                datadict['Principal/Admin Position']="Principal"
                datadict['Principal/Admin Email']=principal_email
                datadict['Telephone']=principal_no
            elif content['schoolManagement'][i]['position']=='Administration Manager':
                    admin=(content['schoolManagement'][i]['firstName'])+' '+(content['schoolManagement'][i]['lastName'])
                    admin_no=content['schoolManagement'][i]['phone']
                    admin_email=content['schoolManagement'][i]['email']
                    datadict["Name"]=name
                    datadict['Address']=address
                    datadict['Principal/Admin Name']=admin
                    datadict['Principal/Admin Position']="Administration Manager"
                    datadict['Principal/Admin Email']=admin_email
                    datadict['Telephone']=admin_no
            else:
                    datadict["Name"]=name
                    datadict['Address']=address
                
        list123.append(datadict)
    print(list123)
    df=pd.json_normalize(list123)
    df.to_csv(data_file,index=False)
data_savior()