from plone import api
import csv
import os
import shutil

portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

results = catalog(portal_type=('tdf.templateuploadcenter.tupproject',
                               ))
for d in results:
    with open('templateprojects.csv', 'ab') as csvfile:
        tprojectlist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        tprojectlist.writerow([d["Title"], d.getURL()])


results2 = catalog(portal_type=('tdf.extensionuploadcenter.eupproject',
                               ))
for d in results2:
    with open('extensionprojects.csv', 'ab') as csvfile:
        eprojectlist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        eprojectlist.writerow([d["Title"], d.getURL()])