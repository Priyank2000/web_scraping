from bs4 import BeautifulSoup
import requests
import pandas as pd  

webpages = ['https://isd110.org/our-schools/laketown-elementary/staff-directory','https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=1',
'https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=2','https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=3',
'https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=4','https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=5',
'https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=6','https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=7',
'https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page=8']

first_name = []
last_name = []
job = []
address = []
phone_no = []
email_id = []


for website in webpages:
    result = requests.get(website)
    soup = BeautifulSoup(result.text, 'lxml')

    for i in soup.select('.title'):
        name = i.get_text()
        a = name.split(',')
        if len(a) == 2:
            first_name.append(a[0])
            last_name.append(a[1])
        else:
            continue

    for j in soup.select('.field .job-title'):
        job_title = j.get_text()
        c = job_title.replace('\n','')
        job.append(c) 

    # for k in soup.select('.field-content span'):
    #     loc = k.get_text()
    #     b = loc.replace('\n',' ')
    #     address.append(b)

    for l in soup.select('.field .phone a'):
        phone = l.get_text()
        phone_no.append(phone)

    for m in soup.select('.field .email a'):
        email = m.get_text()
        email_id.append(email)


dic = {'First Name': first_name, 'Last Name': last_name, 'Job Title': job, 'Phone No': phone_no, 'Email Id': email_id}
df = pd.DataFrame(dic)
df.to_csv('output.csv', index = False)
