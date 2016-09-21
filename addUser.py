from plone import api
import csv
import transaction

csvfilename = raw_input("Please type in the name of the csv file with the data for the new user(s): ")

portal = api.portal.get()

# import new member from a new csv-file into Plone. The user provides
# the name of the file by input on command line.
# The csv-file has to be comma separated with the order: fullname,email,username

with open(csvfilename, 'rb') as f:
    f.seek(0)
    reader = csv.reader(f)
    for row in reader:
        api.user.create(username=row[2], email=row[1], properties ={'fullname':row[0]})

transaction.commit()