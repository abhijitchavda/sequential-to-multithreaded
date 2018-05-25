#python 3
# RUN THE CODE using --> python3 jsonifier_sequential.py
import json;
import re;
import time
start_time = time.time()
lines=[];
correctlinedata={};
correctlines=[];
error=[];
count=-1;
def checkszipcode(code):
	try:
		int(code)
		if len(code)==5:
			return True
		return False
	except ValueError:
		return False

def checkpnumber(number):
	if re.match("^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$",number):
		return True
	else:
		return False

def checkcolor(color):
	colors=['red','blue','green','aqua marine','yellow','gray','pink']
	if color in colors:
		return True;
	else:
		return False;



def standardnumberformat(number):
	number=str(number)
	number=number.replace(" ","-");
	number=number.replace(".","-");
	number=number.replace("(","");
	number=number.replace(")","");
	return number;


with open('data.in') as file:
	lines = [line.strip('\n') for line in file]

for line in lines:
	count=count+1;
	lineparts=line.split(',')
	if len(lineparts)==4:
		if checkszipcode(lineparts[2].strip()) and checkpnumber(lineparts[3].strip()) and checkcolor(lineparts[1].strip()):
			correctlinedata['zipcode']=lineparts[2].strip()
			correctlinedata['phonenumber']=standardnumberformat(lineparts[3].strip())
			correctlinedata['color']=lineparts[1].strip()
			try:
				lastindex=lineparts[0].strip().rindex(' ');
				correctlinedata['firstname']=lineparts[0][0:lastindex]
				correctlinedata['lastname']=lineparts[0][lastindex+1:]
				correctlines.append(json.loads(json.dumps(correctlinedata)))
				correctlinedata.clear();
				continue
			except ValueError:
				correctlinedata.clear();
				error.append(count)
				continue
		else:
			correctlinedata.clear();
			error.append(count)
			continue

	elif len(lineparts)==5:

		if checkpnumber(lineparts[2].strip()) :
			correctlinedata['phonenumber']=standardnumberformat(lineparts[2].strip())

			if checkszipcode(lineparts[4].strip()) and checkcolor(lineparts[3].strip()):
				correctlinedata['zipcode']=lineparts[4].strip()
				correctlinedata['color']=lineparts[3].strip()
				correctlinedata['firstname']=lineparts[1]
				correctlinedata['lastname']=lineparts[0]
				correctlines.append(json.loads(json.dumps(correctlinedata)))
				correctlinedata.clear();
				continue
			else:
				correctlinedata.clear();
				error.append(count)
				continue

			
		elif checkszipcode(lineparts[2].strip()) :
			correctlinedata['zipcode']=lineparts[2].strip()

			if checkpnumber(lineparts[3].strip()) and checkcolor(lineparts[4].strip()) :
				correctlinedata['phonenumber']=standardnumberformat(lineparts[3].strip())
				correctlinedata['color']=lineparts[4].strip()
				correctlinedata['firstname']=lineparts[0]
				correctlinedata['lastname']=lineparts[1]
				correctlines.append(json.loads(json.dumps(correctlinedata)))
				correctlinedata.clear();
				continue
			else:
				correctlinedata.clear();
				error.append(count)
				continue

		else:
			correctlinedata.clear();
			error.append(count)
			continue
	else :
		error.append(count)

print(json.dumps({"entries":correctlines,"errors":error},sort_keys=True, indent=2));
print("------- %s seconds --------" % (time.time() - start_time))
#reduce lines by if & & & 
#reduce time by map reduce
