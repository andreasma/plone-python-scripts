from plone import api
import csv

portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

allextreleases = catalog(portal_type=('tdf.extensionuploadcenter.euprelease',
                                      'tdf.extensionuploadcenter.eupreleaselink'))

alltempreleases = catalog(portal_type=('tdf.templateuploadcenter.tuprelease',
                                       'tdf.templateuploaccenter.tupreleaselink'))

for d in allextreleases:
     st = d.review_state
     url = ('/' .join (d.getObject().getPhysicalPath()))
     name = d.Title

     with open('extensionreleases.csv', 'ab') as et:
         pt = csv.writer(et, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
         pt.writerow([name, st, url])



for t in alltempreleases:
     st = t.review_state
     url = ('/' .join (t.getObject().getPhysicalPath()))
     name = t.Title

     with open('templatereleases.csv', 'ab') as tup:
         ptemp = csv.writer(tup, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
         ptemp.writerow([name, st, url])