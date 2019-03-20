import sys
from today_parser import today
from standing_parser import standing_data
from team_parser import team_data


def main(today_url):
    url_standing = 'https://site.web.api.espn.com/apis/v2/sports/basketball/nba/standings?region=us&lang=en' \
                   '&contentorigin=espn&type=0&level=2&sort=playoffseed%3Aasc '
    today(today_url)
    print('-'*50)
    team_data('LAL').pprint()
    print('-'*50)
    standing_data(url_standing).pprint()


if __name__ == '__main__':
    # processing arguments, error checking and handling
    if len(sys.argv) > 2:
        print('Error')
        print('Please use: nba-scoreboard.py [date in YYYY-MM-DD form]')
        sys.exit(0)
    elif len(sys.argv) == 2:
        url = 'https://www.si.com/nba/scoreboard?date=%s' % sys.argv[1]
    else:
        url = 'https://www.si.com/nba/scoreboard'
    main(url)

