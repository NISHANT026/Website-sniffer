# Website-sniffer
############################################
Pre-requisite

 Pandas library should be installed to run the script.Also the code was built in Python 2.7.17 so it should run in later versions.
Lastly Wireshark software is neaded to analyze the network traffic.
The URL and IPs of available websites or websites that can we visited should also be updated in web dictionary (In Python Script)
if you does not want to add URL and IP to web, you can just Erase line 35(in Python Script) and print the line that is commented out
This will give the IPs instead of website names

#############################################

#############################################
Exicution

First, perform a capture of the network traffic by loading up Wireshark
and starting a capture. After ending the capture, it can be exported
as a CSV by going into
    Files -> Export Packet Dissections -> As CSV
Or you can just use go.csv
Save the capture as 'go.csv' in the project directory. To execute
the program, one needs to enter into the project directory and execute
the command
    $ python network.py

The final output will be in the terminal with website names and IPs

###############################################

Contact no. 9685568033
