# prevents running specific websites during working hours to prevent distractions
# teaches running a python program in the background that checks files, open browser, etc.
# accesses C:\Windows\System32\drivers\etc\hosts to block websites during working hours

# packages
## allows the sleep command
import time
## gets the date and time, shortened to dt
from datetime import datetime as dt

# path to the file to be edited in the final version
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# temporary working path
hosts_temp = "hosts"
# null ip to prevent connection
redirect = "127.0.0.1"
# list of blocked websites
website_list = ["www.facebook.com", 
                "facebook.com", 
                "www.jalopnik.com", 
                "jalopnik.com"
                ]
# while loop will infinitely run until false
while True:
    #checks if the current hour falls between 8:00AM and 4:00PM
    ## if it's between working hours
    if dt(dt.now().year, dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,16):
        # open the host file and append ('r+', not write which would clean out the rest of it)
        with open(hosts_temp,'r+') as file:
            #read the file into content
            content=file.read()
            # for loop to check for websites to be blocked
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"       "+website+"\n")
    ## if it's outside  working hours
    else:
        # open the hosts file in read mode as the variable file
        with open(hosts_temp,'r') as file:
            #create a list, where each string is a line of the hosts file
            content = file.readlines()
            # place the pointer at the top of the hosts file
            file.seek(0)
            # now re-open the hosts file in write mode once the list has already been created
            with open(hosts_temp, 'w') as file:
            # iterate over every line of the hosts file stored in the list content
                for line in content:
                    # if the current iterating line does not contain a website in the website list
                    if not any(website in line for website in website_list):
                        # write that line
                        file.write(line)
        print("Fun hours...")
    # run script every 5 seconds
    time.sleep(5)