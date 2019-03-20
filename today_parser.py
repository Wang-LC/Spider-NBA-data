from lxml import html
import requests


# function to remove spaces, newlines, and other undesirable characters from strings
def clean_data(raw_list, destination_list):
    for element in raw_list:
        element = element.replace('\n', '')
        element = element.replace('\x95', '')
        element = element.strip()
        destination_list.append(element)

    return destination_list


def today(website):  # today data program
    """
    :param website: si.com
    :return: games' result/games' time (today)
    """
    page = requests.get(website)

    tree = html.fromstring(page.text)

    # initializing variables
    away_city_name = []
    away_teams_record = []

    home_city_name = []
    home_teams_record = []

    game_status = []
    away_scores = []
    home_scores = []

    # scraping city, team name, and team record data
    away_city_queue = tree.xpath('//div[@class="teams"]/div[1]/div[2]/div[1]/a/text()')
    away_teams_name = tree.xpath('//div[@class="teams"]/div[1]/div[2]/a[2]/span/text()')
    away_record_queue = tree.xpath('//div[@class="teams"]/div[1]/div[2]/span/text()')

    home_city_queue = tree.xpath('//div[@class="teams"]/div[3]/div[2]/div[1]/a/text()')
    home_teams_name = tree.xpath('//div[@class="teams"]/div[3]/div[2]/a[2]/span/text()')
    home_record_queue = tree.xpath('//div[@class="teams"]/div[3]/div[2]/span/text()')

    # cleaning up city and record data
    away_city_name = clean_data(away_city_queue, away_city_name)
    home_city_name = clean_data(home_city_queue, home_city_name)
    away_teams_record = clean_data(away_record_queue, away_teams_record)
    home_teams_record = clean_data(home_record_queue, home_teams_record)

    # games not yet started
    if tree.xpath('//div[@class="float-left status-container"]/strong/text()') :

        times = tree.xpath('//div[@class="float-left status-container"]/strong/text()')
        game_status = clean_data(times, game_status)

        clean_times = []
        clean_times = clean_data(times, clean_times)
        clean_times = list(filter(None, clean_times))

        for time in clean_times:
            away_scores.append('-')
            home_scores.append('-')

    # games ended
    if tree.xpath('//div[@class="status-final"]/text()'):
        finals = tree.xpath('//div[@class="status-final"]/text()')
        game_status = clean_data(finals, game_status)

        away_scores_queue = tree.xpath('//div[@class="status-final"]/../../../div[2]/div/div[1]/div/div[1]/div['
                                     '3]/div/text()')
        away_scores = clean_data(away_scores_queue, away_scores)

        home_scores_queue = tree.xpath('//div[@class="status-final"]/../../../div[2]/div/div[1]/div/div[3]/div['
                                     '3]/div/text()')
        home_scores = clean_data(home_scores_queue, home_scores)

    game_status = list(filter(None, game_status))  # remove empty strings from list

    # prints the scoreboard
    for awayCity, homeCity, awayTeam, homeTeam, awayRecord, homeRecord, status, awayScore, homeScore in zip(
            away_city_name, home_city_name, away_teams_name, home_teams_name, away_teams_record,
            home_teams_record, game_status, away_scores, home_scores):
        print('{0:50} {1:10}'.format(awayCity + ' ' + awayTeam + ' ' + awayRecord, awayScore))
        print('{0:50} {1:10}'.format(homeCity + ' ' + homeTeam + ' ' + homeRecord, homeScore))
        print(status + '\n')


if __name__ == '__main__':
    url = 'https://www.si.com/nba/scoreboard'
    url_date = 'https://www.si.com/nba/scoreboard?date=2019/3/17'
    today(url)
