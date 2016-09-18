from plone import api
import csv

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
                               'tdf.extensionuploadcenter.eupreleaselink')

for d in results:
    with open('creators.txt', 'ab') as textfile:
        textfile.write(d.Creator)
        textfile.write('\n')
