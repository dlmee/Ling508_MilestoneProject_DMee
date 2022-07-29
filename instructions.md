NOTE: In order to successfully run this docker file you will have to do the following. 

docker build -t [name] [directory (presumably .)]
I was running the html page through the built in python server. 
python -m http.server
Make sure that you run that terminal command in the proper directory.

docker run --network="host" [Whatever you have named the container].

Finally, please note that I do not yet understand how to have test_sensedist.py import within the docker file. 

The original code (which works locally) is from app.sensedist import *

I will amend that as soon as I understand what I'm missing. 