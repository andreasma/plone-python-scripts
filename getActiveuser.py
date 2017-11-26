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

