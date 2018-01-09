from plone import api
import csv
import os
import shutil
import datetime

# Create a backup directory and move all text/csv files from the former run to that directory

if not os.path.exists('backup'):
    os.makedirs('backup')

if os.path.exists('users.csv'):    
    shutil.move("users.csv", "backup/users.csv")
if os.path.exists('currentusers.txt'):
    shutil.move("currentusers.txt", "backup/currentusers.txt")
if os.path.exists('creators.txt'):
    shutil.move("creators.txt", "backup/creators.txt")
if os.path.exists('activeusers.txt'):
    shutil.move("activeusers.txt", "backup/activeusers.txt")
if os.path.exists('notactive.txt'):
    shutil.move("notactive.txt", "backup/notactive.txt")
if os.path.exists('extensionsiteadminstrators.txt'):
    shutil.move("extensionsiteadminstrators.txt", "backup/extensionsiteadminstrators.txt")

# Rename the backup directory with a the current date

dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

os.rename('backup', 'backup' + '-' + dt)

portal = api.portal.get()

users = api.user.get_users()

# write all current users in append mode to a csv-file
for f in users:
    id = f.getProperty('id')
    name = f.getProperty('fullname')
    email = f.getProperty('email')
    roles = api.user.get_roles(username=id)
    with open('users.csv', 'ab') as csvfile:
        memberlist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        memberlist.writerow([name, id, email, roles])
        
for f in users:
    id = f.getProperty('id')
    with open('currentusers.txt', 'a+') as textfile:
        textfile.write(id)
        textfile.write('\n')

admins = api.user.get_users(groupname='Administrators')

for f in admins:
    id=f.getProperty('id')
    with open('extensionsiteadminstrators.txt',  'a+' ) as textfile:
        textfile.write(id)
        textfile.write('\n')
        

catalog = api.portal.get_tool(name='portal_catalog')

results = catalog(portal_type=('tdf.templateuploadcenter.tupcenter',
                               'tdf.templateuploadcenter.tupproject',
                               'tdf.templateuploadcenter.tuprelease',
                               'tdf.templateuploadcenter.tupreleaselink',
                               'tdf.extensionuploadcenter.eupcenter',
                               'tdf.extensionuploadcenter.eupproject',
                               'tdf.extensionuploadcenter.euprelease',
                               'tdf.extensionuploadcenter.eupreleaselink'))

for d in results:
    with open('creators.txt', 'ab') as textfile:
        textfile.write(d.Creator)
        textfile.write('\n')


# Create two sets from the listed items of the two text files and intersect them.
# Make a list of the matching items and write the items of this list to a text file.
# The list contains the active users of the site.

data = [line.strip() for line in open("creators.txt", 'r')]

data2 = [line.strip() for line in open("currentusers.txt", 'r')]

data3 = [line.strip() for line in open("extensionsiteadminstrators.txt", 'r')]

set1 = set(data)
set2 = set(data2)
set3 = set1.intersection(set2)
found = []
for match in set3:
    found.append(match)

with open('activeusers.txt', 'ab') as activeusers:
    for item in found:
        activeusers.write("%s\n" % item)
        

# And here another list with the inactive users

set4 = set2.difference(set1)
set5 = set(data3)

set6 = set4.difference(set5)

difference = []
for match in set6:
    difference.append(match)
    
with open('notactive.txt', 'ab') as nonactive:
    for item in difference:
        nonactive.write("%s \n" % item)
 

# move all created text and csv files to a subdirectory with an appropriate time stamp.

if not os.path.exists('backup'):
    os.makedirs('backup')

if os.path.exists('users.csv'):    
    shutil.move("users.csv", "backup/users.csv")
if os.path.exists('currentusers.txt'):
    shutil.move("currentusers.txt", "backup/currentusers.txt")
if os.path.exists('creators.txt'):
    shutil.move("creators.txt", "backup/creators.txt")
if os.path.exists('activeusers.txt'):
    shutil.move("activeusers.txt", "backup/activeusers.txt")
if os.path.exists('notactive.txt'):
    shutil.move("notactive.txt", "backup/notactive.txt")
if os.path.exists('extensionsiteadminstrators.txt'):
    shutil.move("extensionsiteadminstrators.txt", "backup/extensionsiteadminstrators.txt")

# Rename the backup directory with a the current date

dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

os.rename('backup', 'backup' + '-' + dt)
