import requests, json, datetime, re, base64, schedule, time, sys

class TimeSHIT(object):

    def isWeekend(self):
        return datetime.datetime.today().weekday() >= 5

    def fill_timeshit(self, jira_url, payload, headers):
        # Checks for weekends
        if self.isWeekend():
            print ('Today is weekend! No timeSHIT!')
            return

        response = requests.post(jira_url, data=json.dumps(payload), verify=False, headers=headers)
        print (response.status_code)
        if (response.status_code == 201):
            print ('Successfully filled timeSHIT for date {0} with {1}.'.format(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+0530")[:10], payload['timeSpent']))
        else:
            print ('Error occurred while filling timeSHIT for date {0} with {1}'.format(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+0530")[:10], payload['timeSpent']))

    def read_conf(self, file_name):

        # Read the config file
        with open (file_name, 'r+') as config_file:
            config_json = json.loads(config_file.read())
            config_json['jira_url'] = config_json['jira_url'] + ('/rest/api/latest/issue/{0}/worklog').format(config_json['timesheet_jira_id'])

        return config_json

    def get_auth_token(self, username, password):
        if sys.version_info >= (3, 0):
            return str(base64.b64encode(((username + ':' + password).encode('ascii'))))[2:-1]
        return str(base64.b64encode(((username + ':' + password).encode('ascii'))))
    
    def schedule(self):
        config = self.read_conf('config.txt')
        schedule.every().day.at('17:45').do(self.fill_timeshit, config['jira_url'], {
            "timeSpent": "{0}h {1}m".format(config['hours_to_fill'], config['minutes_to_fill']),
            "comment": None if config['comment'] == 'null' else config['comment'],
            "started": re.sub(r'\d{6}', '000', datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+0530"))
        }, {
            'Content-Type': "application/json",
            'Authorization': "Basic " + self.get_auth_token(config['username'], config['password'])
        })

        while True:
            schedule.run_pending()
            time.sleep(1)
