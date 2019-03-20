import json
import urllib


class Standing:
    def __init__(self, east_name_list, east_stats_list, west_name_list, west_stats_list):
        self.eastName = east_name_list
        self.eastStats = east_stats_list
        self.westName = west_name_list
        self.westStats = west_stats_list

    def pprint(self):
        # ---------------------------------
        # Eastern:
        # 1 team name1        team stats
        # 2 team name2        team stats
        # ...
        # Western:
        # 1 team name1        team stats
        # 2 team name2        team stats
        # ...
        # ---------------------------------
        n = range(1, 16)
        eastern = zip(n, self.eastName, self.eastStats)
        western = zip(n, self.westName, self.westStats)

        print('Eastern:')
        for n, name, stats in eastern:
            print('{0:2} {1:40} {2:10}'.format(n, name, stats))
        print('-'*50)
        print('Western:')
        for n, name, stats in western:
            print('{0:2} {1:40} {2:10}'.format(n, name, stats))


def load_url(url):
    return urllib.request.urlopen(url).read().decode('utf-8')


def standing_data(url):  # scraping standings by json
    # url_standing = 'https://site.web.api.espn.com/apis/v2/sports/basketball/nba/standings?region=us&lang=en' \
    #                '&contentorigin=espn&type=0&level=2&sort=playoffseed%3Aasc '
    json_data = json.loads(load_url(url))

    # initializing variables
    east_name = []
    west_name = []
    east_stats = []
    west_stats = []
    for n in range(15):
        east_name.append(json_data['children'][0]['standings']['entries'][n]['team']['displayName'])
        west_name.append(json_data['children'][1]['standings']['entries'][n]['team']['displayName'])
        east_stats.append(json_data['children'][0]['standings']['entries'][n]['stats'][12]['displayValue'])
        west_stats.append(json_data['children'][1]['standings']['entries'][n]['stats'][12]['displayValue'])

    return Standing(east_name, east_stats, west_name, west_stats)


if __name__ == '__main__':
    url_standing = 'https://site.web.api.espn.com/apis/v2/sports/basketball/nba/standings?region=us&lang=en' \
                   '&contentorigin=espn&type=0&level=2&sort=playoffseed%3Aasc '
    standing_data(url_standing).pprint()
