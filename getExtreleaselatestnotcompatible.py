from plone import api
import csv

portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

allreleases = catalog(portal_type=('tdf.templateuploadcenter.tuprelease',
                               'tdf.templateuploadcenter.tupreleaselink',
                               'tdf.extensionuploadcenter.euprelease',
                               'tdf.extensionuploadcenter.eupreleaselink'))

for d in allreleases:
    if not 'LibreOffice 6.0' in d.compatibility_choice:
        releasetitle = d.Title
        compatibility = d.compatibility_choice
        url = ('/' .join (d.getObject().getPhysicalPath()))
        print (compatibility)
        with open('releasecompatibility.csv', 'ab') as csvfile:
           complist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           complist.writerow([releasetitle, url, compatibility])
    else:
        print ('keine oder nur Releases ohne Kompatibiltaet zu 6.0')