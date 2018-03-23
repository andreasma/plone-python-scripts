from plone import api
import csv

portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

allextensionreleases = catalog(portal_type=('tdf.extensionuploadcenter.euprelease',
                                            'tdf.extensionuploadcenter.eupreleaselink'))

alltemplatereleases = catalog(portal_type=('tdf.templateuploadcenter.tuprelease',
                                           'tdf.templateuploadcenter.tupreleaselink',))

for d in allextensionreleases:
    if not 'LibreOffice 6.0' in d.compatibility_choice:
        releasetitle = d.Title
        compatibility = d.compatibility_choice
        url = ('/' .join (d.getObject().getPhysicalPath()))
        with open('extensionreleasecompatibility.csv', 'ab') as csvfile:
           complist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           complist.writerow([releasetitle, url, compatibility])
    else:
        print ('no extension releases compatible with version 6.0')

for d in alltemplatereleases:
    if not 'LibreOffice 6.0' in d.compatibility_choice:
        releasetitle = d.Title
        compatibility = d.compatibility_choice
        url = ('/' .join (d.getObject().getPhysicalPath()))
        with open('templatereleasecompatibility.csv', 'ab') as csvfile:
           complist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           complist.writerow([releasetitle, url, compatibility])
    else:
        print ('no template releases compatible with version 6.0')