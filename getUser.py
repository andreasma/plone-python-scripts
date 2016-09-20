from plone import api
import csv
import os
import shutil

# Create a backup directory and move all text/csv files from the former run to that directory

if not os.path.exists('backup'):
    os.makedirs('backup')

shutil.move("users.csv", "backup/users.csv")
shutil.move("currentusers.txt", "backup/currentusers.txt")
shutil.move("creators.txt", "backup/creators.txt")
shutil.move("activeusers.txt", "backup/activeusers.txt")
shutil.move("notactive.txt", "backup/notactive.txt")

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

    with open('currentusers.txt', 'ab') as userlist:
        userlist.write(f.id)
        userlist.write('\n')

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

set4 = set1.symmetric_difference(set2)

different = []
for match in set4:
    different.append(match)

with open('noactive.txt', 'ab') as noactive:
    for item in different:
        noactive.write("%s \n" % item)