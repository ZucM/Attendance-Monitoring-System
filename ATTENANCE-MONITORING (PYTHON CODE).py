def retstr(r):
    l=[]
    for i in r:
        for j in i:
            for k in j:
              if (ord(k)>=48 and ord(k)<=57) or (ord(k)== 65 or ord(k)==75):
                l.append(k)
    s=[]
    for i in l:
        s+=str(i)

    new = "" 
  
    for x in s: 
        new += x        
    return new


def retstrday(day):
    l=[]
    for i in day:
        for j in i:
            for k in j:
              if (ord(k)>=48 and ord(k)<=57):
              	l.append(k)
    s=[]
    for i in l:
	s+=str(i)

    new=""

    for  x in s:
	new+=x
    return int(new)



import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Attendance_Database").sheet1

import urllib 
from firebase import firebase
firebase=firebase.FirebaseApplication('https://fire-37781.firebaseio.com/ATTENDANCE_SYSTEM_/')

#INSERTION OF NEW DATA
#row=[]
#index=22
#sheet.insert_row(row, index)

id=[]
for i in range(2,21):
    id.append(sheet.cell(i,1).value)


counter=0
present=[]
while True:
	while True:
    		r=firebase.get('barcode',None)
    		day=firebase.get('day',None)
    		if(counter!=0):
        		if(r!=r1):
	    			f=1
            			r1=r
            			while(f!=0):
					c=0
					barcode=retstr(r)
					d=retstrday(day)
					strdb=str(barcode)+str(d)
					for c in range(0,19):
						if(id[c]==barcode):
							print(c)
							break
					if (barcode in id):
						if (strdb not in present):
							present.append(strdb)
							sheet.update_cell(c+2,d+2,"1")
							print("\n")
							print("ID: ",barcode,"   Day: ",d,"     ~Done")
							break
						else:
							print("\n--- Marked ---")
							break                
					else:
						print("\nNot Registered")
						f=0
    		elif(counter==0):
		        counter=1
			r1=r
			f=1
		        while(f!=0):
        			c=0
				barcode=retstr(r)
				print(barcode)
				d=retstrday(day)
				print(d)
				strdb=str(barcode)+str(d)
				for c in range(0,19):
					if(id[c]==barcode):
						print(c)
						break
				if (barcode in id):
					if (strdb not in present):
        			       		present.append(strdb)
						sheet.update_cell(c+2,d+2,"1")
						print("\n")
						print("ID: ",barcode,"   Day: ",d,"  ~Done")
             	               			break
					else:
        			     		print("\n\n--- Marked ---")
						break
            			else:
		                	print("\nNot Registered")
                			f=0
		else:
        		print("Not Registered")
	        	break
