# pcap-parser
A basic parser for dns and http requests for the Foundations of Networks and Mobile Systems class at NYU 

We are using the command line version of wireshark, which is called tshark

Here is how you run the parsing scripts for dns and http objects:
python dns-parser
python http-parser

Both of the scripts show very basic information about the dns and http objects. You can update the scripts based on what you need. 


How to run on Windows pc? 

You can run the code successfully in windows terminal by doing the following steps:

You might get an error which tells you matplotlib is not installed, please run these two commands one by one in terminal to solve that error:
python -m pip install -U pip
python -m pip install -U pip


Please add 'C:\Program Files\Wireshark' to the Path environment variable in windows settings. Just search in the control panel for "Edit the system enviroment variables". Read this for more info: https://osqa-ask.wireshark.org/questions/10087/how-do-i-run-tshark-on-windows 


