import json
import urllib


class Team:
    def __init__(self, name, record, ppg, opp, home_record, away_record, event):
        self.name = name
        self.record = record
        self.ppg = ppg
        self.opp = opp
        self.home = home_record
        self.away = away_record
        self.event = event

    def pprint(self):
        # ----------------------------
        # Team Name (record)
        # Next Game:
        # Points Per Game:
        # Opponent Point Per Game:
        # HOME:
        # AWAY:
        # ----------------------------
        print('%s (%s)' % (self.name, self.record))
        print('Next Game: %s' % self.event[0:10])
        print('Points Per Game: %.1f' % self.ppg)
        print('Opponent Point Per Game: %.1f' % self.opp)
        print('HOME: %s' % self.home)
        print('AWAY: %s' % self.away)


def load_url(url):
    return urllib.request.urlopen(url).read().decode('utf-8')


def team_data(team):  # scraping favourite team next event by json
    """
    :param team: short name (name in teamshortname.txt)
    :return: data of favourite team
    """
    url_favor_team = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/%s' % team
    json_data = json.loads(load_url(url_favor_team))
    name = json_data['team']['displayName']
    event = json_data['team']['nextEvent'][0]['date']
    record = json_data['team']['record']['items'][0]['summary']
    point_per_game = json_data['team']['record']['items'][0]['stats'][11]['value']
    opponent_point = json_data['team']['record']['items'][0]['stats'][12]['value']
    home_record = json_data['team']['record']['items'][1]['summary']
    away_record = json_data['team']['record']['items'][2]['summary']

    return Team(name, record, point_per_game, opponent_point, home_record, away_record, event)


if __name__ == '__main__':
    team_data('LAL').pprint()
