from __future__ import print_function
import json
import logging


from google.appengine.api import urlfetch


class ForecastApp(object):
    def __init__(self, account_id, protocol="https",
                 host="api.forecastapp.com"):
        self.protocol = protocol
        self.host = host
        self.account_id = account_id

        self.auth_token = None

    def projects(self):
        return self._call('/projects')['projects']

    def people(self):
        return self._call('/people')['people']

    def clients(self):
        return self._call('/clients')['clients']

    def assignments(self):
        return self._call('/assignments')['assignments']

    def milestones(self):
        return self._call('/milestones')['milestones']

    def _call(self, url):
        headers = {'Authorization': 'Bearer %s' % self.auth_token,
                   'Forecast-Account-ID': '%s' % self.account_id}

        url = '%s://%s%s' % (self.protocol, self.host, url)
        res = urlfetch.fetch(
            url,
            headers=headers,
        )

        logging.debug("URL: {}".format(url))
        logging.debug("Status Code: {}".format(res.status_code))

        return json.loads(res.content)
