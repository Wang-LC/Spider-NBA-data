# !/usr/bin/env python
import json
from urllib import request


class Game:
    def __init__(self, team1, team2, score1, score2, stats):
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2
        self.stats = stats

    def pprint(self):
        games = zip(self.team1, self.team2, self.score1, self.score2, self.stats)
        for team_a, team_b, score_a, score_b, stat in games:
            print('{0:25} {1:10}'.format(team_a, score_a))
            print('{0:25} {1:10}'.format(team_b, score_b))
            print(stat)
            print('-'*40)

    def write(self):
        content = ['TODAY:', '-'*10]
        games = zip(self.team1, self.team2, self.score1, self.score2, self.stats)
        for team_a, team_b, score_a, score_b, stat in games:
            if score_a > score_b:
                team_a += '*'
            elif score_b > score_a:
                team_b += '*'
            content.append('{0:30} {1:20}'.format(team_a, score_a))
            content.append('{0:30} {1:20}'.format(team_b, score_b))
            content.append(stat)
            content.append('\n')
        return content


def load_url(web_url):
    return request.urlopen(web_url).read().decode('utf-8')


def today_data(web_url):
    json_data = json.loads(load_url(web_url))
    team1 = []
    team2 = []
    score1 = []
    score2 = []
    stats = []
    for game in json_data['gs']['g']:
        team1.append('%s %s' % (game['v']['tc'], game['v']['tn']))
        team2.append('%s %s' % (game['h']['tc'], game['h']['tn']))
        score1.append(game['v']['s'])
        score2.append(game['h']['s'])
        stats.append(game['stt'])
    return Game(team1, team2, score1, score2, stats)


if __name__ == '__main__':
    url = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2018/scores/00_todays_scores.json'
    today_data(url).pprint()
