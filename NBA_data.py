# !/usr/bin/env python
from today_game import today_data
from standing_parser import standing_data
from team_parser import team_data
import datetime
from EmailSender import mailsender
from team_parser import data_plot
import sys


def main(team):
    url_today = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2018/scores/00_todays_scores.json'
    url_standing = 'https://site.web.api.espn.com/apis/v2/sports/basketball/nba/standings?region=us&lang=en' \
                   '&contentorigin=espn&type=0&level=2&sort=playoffseed%3Aasc '
    data_plot(team)
    today = datetime.date.today()
    sender = mailsender()
    today_content = str('\n'.join(today_data(url_today).write()))
    layer = '\n'+'*'*44+'\n'
    team_content = str('\n'.join(team_data(team).write()))
    standing_content = str('\n'.join(standing_data(url_standing).write()))
    content = today_content + layer + team_content + layer + standing_content

    sender.sendMsg(content, 'bar.png', "NBA News for " + str(today))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please use short name (in teamshortname.txt)')
        exit()
    else:
        main(sys.argv[1])

