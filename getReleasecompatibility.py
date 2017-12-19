from plone import api
import csv


portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

results = catalog(portal_type=('tdf.templateuploadcenter.tuprelease',
                               'tdf.templateuploadcenter.tupreleaselink',
                               'tdf.extensionuploadcenter.euprelease',
                               'tdf.extensionuploadcenter.eupreleaselink'),
                  getCompatibility=('LibreOffice 5.4'))

for d in results:
    releasetitle = d.Title
    compatibility = d.compatibility_choice
    with open('releasecompatibility.csv', 'ab') as csvfile:
        complist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        complist.writerow([releasetitle, compatibility])
    
