# !/usr/bin/env python
import json
from urllib import request
import matplotlib.pyplot as plt
import numpy as np


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

    def write(self):
        content = ['FAVORITE TEAM:', '-' * 20, '%s (%s)' % (self.name, self.record),
                   'Next Game: %s' % self.event[0:10], 'Points Per Game: %.1f' % self.ppg,
                   'Opponent Point Per Game: %.1f' % self.opp, 'HOME: %s' % self.home, 'AWAY: %s' % self.away]
        return content


def load_url(url):
    return request.urlopen(url).read().decode('utf-8')


def get_json(team):
    url_favor_team = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/%s' % team
    return json.loads(load_url(url_favor_team))


def team_data(team):  # scraping favourite team next event by json
    json_data = get_json(team)
    name = json_data['team']['displayName']
    event = json_data['team']['nextEvent'][0]['date']
    record = json_data['team']['record']['items'][0]['summary']
    point_per_game = json_data['team']['record']['items'][0]['stats'][11]['value']
    opponent_point = json_data['team']['record']['items'][0]['stats'][12]['value']
    home_record = json_data['team']['record']['items'][1]['summary']
    away_record = json_data['team']['record']['items'][2]['summary']

    return Team(name, record, point_per_game, opponent_point, home_record, away_record, event)


def data_plot(team):
    json_data = get_json(team)
    team_name = json_data['team']['displayName']
    name_list = []
    win_list = [json_data['team']['record']['items'][0]['stats'][1]['value']]
    lose_list = [json_data['team']['record']['items'][0]['stats'][2]['value']]
    for item in json_data['team']['record']['items']:
        name_list.append(item['description'])

    for n in range(1, 3):
        win_list.append(json_data['team']['record']['items'][n]['stats'][0]['value'])
        lose_list.append(json_data['team']['record']['items'][n]['stats'][1]['value'])

    index = np.arange(len(win_list))
    width = 0.4

    rects1 = plt.bar(index, win_list, width=width, label='win')
    rects2 = plt.bar(index + width, lose_list, width=width, label='lose', tick_label=name_list)
    plt.xticks(index + width/2, name_list)
    plt.legend()
    plt.title('%s Win and Lose Times This Season' % team_name)
    add_labels(rects1)
    add_labels(rects2)
    plt.savefig('bar.png')


def add_labels(rects):
    for rect in rects:
        height = int(rect.get_height())
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        rect.set_edgecolor('white')


if __name__ == '__main__':
    team = 'LAL'
    team_data(team).pprint()
    data_plot(team)
    plt.show()
