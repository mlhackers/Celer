# coding=utf-8
from __future__ import print_function
import json
import pandas as pd
ids = [x for x in range(1,8)]
text = ['''Hey,

WhatsApp Messenger is a fast, simple and secure app that I use to message and call the people I care about.

Get it for free at https://www.whatsapp.com/download/''', '''Senior Analytics Manager - Aasaanjobs.pdf
You can even refer your friends for this role.
Sorry sent the last image by mistake''', '''Analytics Manager - Aasaanjobs.pdf''', '''Business Analyst - Campus.pdf''', '''Hi guys
There are vacancies for Business analyst, Analytics manager and Senior analytics manager at Aasaanjobs. Whosoever is interested, email your CV on anjali.arya@aasaanjobs.com''', '''Hello guys, we are students of SVNIT Surat :school: doing our first college health startup:department_store:. We are taking initiative to support patients suffering from chronic diseases:name_badge: by guiding them about the things they need to do in parallel with their preferred treatment. Please fill up this form, it would help us a lot.
Thanks!

:arrow_down::arrow_down::arrow_down:
https://goo.gl/forms/2A8opUuTE7SSZwrx2''', '''SIEMENS India has inaugurated a new " SIEMENS Technical Acadamy" at Airoli , Mumbai for those students who want to do career in Technical and Technology. This is Honorable Prime minister's "Make in India" project to make skill India. Project (Skill India- Kaushal Bharat- Kushal  Bharat) based on SIEMENS, Germany DUAL VET.
We are searching such students who are interested in Technical career and due to family’s financial problems they couldn't continue their career.
This SIEMENS Training centre is providing Technical Skills in Two trades Electrical & Fitter and also giving stipend (7500/- per month in 1st year, 8500/- per month in 2nd year) and canteen facility. Everything is totally free....

After completion of this Training studants can get direct entry to Diploma Engineering in eligible stream

:pray:my humble request to you, if you find good students with financial poor family in our society ( Eg.Our maid's childrens) please communicate below advertisement to them or give below mentioned cell no. He will definitely help them to fill the registration form. 

Age Criteria:- Students born after 1/1/2001 
Education:- presently
who are appearing 10th, 11th and 12th.


Regards,

Anil Nawale 
SIEMENS Ltd.
7506368112
''']

data = {'id':ids, 'message':text}
df = pd.DataFrame.from_dict(data)
df.to_csv('data.csv', index=False)
print(data)
with open('previous_messages.json', 'w') as outfile:  
    json.dumps(data, outfile)
