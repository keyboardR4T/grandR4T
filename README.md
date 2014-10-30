You need to have OLA installed with it's python API libs to run this program
OLA website : http://www.openlighting.org/ola/
Python API doc : http://www.openlighting.org/ola/developer-documentation/python-api/

OLA and the python API help the program communicate with your DMX/USB Box

to start the program run :
	python2.7 grandR4T.py 

You could also run the program without installing OLA or the Python API
by commenting the OLA import libraries[...]
But then it would be just for interface debugging since you won't be able to 
send any DMX :)
