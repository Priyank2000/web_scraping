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
school = []
address = []
state = []
zip = []

for website in webpages:
    result = requests.get(website)
    soup = BeautifulSoup(result.text, 'lxml')

    school_name = soup.title.string.split("|")[-1].strip()
    full_address = [a.text.strip() for a in soup.select("p[class='address']")]
    full_address_new = full_address[-1].split("\n")
    add = full_address_new[0].strip()
    state_name = full_address_new[1].split(",")[0].strip()
    zip_Code = full_address_new[1].split(",")[-1].strip()
    
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

    for l in soup.select('.field .phone a'):
        phone = l.get_text()
        phone_no.append(phone)

    for m in soup.select('.field .email a'):
        email = m.get_text()
        email_id.append(email)

for s in range(len(job)):
    school.append(school_name)
    address.append(add)
    state.append(state_name)
    zip.append(zip_Code)

dic = {'First Name': first_name, 'Last Name': last_name, 'Job Title': job, 'Phone No': phone_no, 'Email Id': email_id, 'School Name': school, 'Address': address, 'State': state, 'zip': zip}
df = pd.DataFrame(dic)
df.to_csv('output.csv', index = False)

