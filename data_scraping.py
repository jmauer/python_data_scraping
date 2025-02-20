from bs4 import BeautifulSoup
import pandas as pd
import requests 


## Scraping the data from the Bundesliga website

def get_buli_stats(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tablelist = []
    buli_table = soup.find('table')


    for team in buli_table.find_all('tbody'):
        rows = team.find_all('tr')
        for row in rows:
            buli_rank = row.find('td', class_='rank').text.strip()
            buli_team = row.find('td', class_='team').find('div')['title'].strip()
            buli_matches = row.find('td', class_='matches').text.strip()
            buli_wins = row.find('td', class_='wins').text.strip()
            buli_draws = row.find('td', class_='draws').text.strip()
            buli_losses = row.find('td', class_='losses').text.strip()
            buli_goals = row.find('td', class_='goals').text.strip()
            buli_difference = row.find('td', class_='difference').text.strip()
            buli_points = row.find('td', class_='pts').text.strip()

            all_teams = {
                'rank': buli_rank,
                'name': buli_team,
                'matches': buli_matches,
                'wins': buli_wins,
                'draws': buli_draws,
                'losses': buli_losses,
                'goals': buli_goals,
                'difference': buli_difference,
                'points': buli_points
            }
            tablelist.append(all_teams)

    buli = pd.DataFrame(tablelist)
    buli.to_csv("stats.csv") ## importing to csv

    return tablelist
    
data = get_buli_stats('https://www.bundesliga.com/de/bundesliga/tabelle') ##getting the data from the website

