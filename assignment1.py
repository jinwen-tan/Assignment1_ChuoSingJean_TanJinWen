#Name: CHUO SING JEAN / TAN JIN WEN 
#MATRICS NO: A19MJ0026 / A19MJ0128 

import csv
import smtplib


# function to extract data from source csv file 
def source_data(filename):
    data = []
    with open (filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# function to load the data from source file to a destination csv file 
def load_destination(data_transfer, filename):
    with open(filename,'w',newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_transfer)

# function to generate new csv through automation 
def csv_automation(filename,new_file):
    data = source_data(filename)
    load_destination(data,new_file)

# calling function for the source file and destination file     
csv_automation("country_wise_latest.csv","Copy of Covid data.csv")

# Send notification to email once complete 
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls() 
server.login("csjyui0827@gmail.com", "ypfavzjvrbtikshl")

from_email = "csjyui0827@gmail.com"
to_email = "chuosingjean@graduate.utm.my"
subject = "Notification: CSV file copy COMPLETED!"
body = "Your CSV file had successfully copied. Thank You. "

message = f"Subject: {subject}\n\n{body}"

server.sendmail(from_email, to_email, message)
server.quit()