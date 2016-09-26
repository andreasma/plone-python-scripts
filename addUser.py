from plone import api
import csv
import transaction

csvfilename = raw_input("Please type in the name of the csv file with the data for the new user(s): ")

outputcsvfile = raw_input("Please type the name of the output csv file, where the current user list with the"
                          "added user should be written: ")

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


# get all current users from the Plone instance
users = api.user.get_users()

# write all current users in append mode to a csv file
for f in users:
  id = f.getProperty('id')
  name = f.getProperty('fullname')
  email = f.getProperty('email')
  roles = api.user.get_roles(username = id)
  with open(outputcsvfile, 'ab') as csvfile:
    memberlist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    memberlist.writerow([name,id,email,roles])