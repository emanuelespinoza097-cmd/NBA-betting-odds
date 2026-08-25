import requests
import pandas as pd
api_key = "c51da76601ca9a383cad86ea3d4c4744"
headers = {
    "x-api-key": api_key
}
url = "https://api.sportsgameodds.com/v2/markets/"
query_params = { "bookmakerID": "fanduel", "leaugeID":"NBA","isProp": "true","betTypeID": "ou",
}
response = requests.get(url, params=query_params, headers=headers)
bettingdata = response.json()
df2 = pd.DataFrame(bettingdata["data"])
print(df2["oddID"].head(20))
print(df2)
print(bettingdata)


from nba_api.stats.endpoints import playergamelogs
"Prints the dataframe with specific columns"

"Creating a class called PLayer that will store the all sorts of stats for a specif player"

class Player:
 def __init__(self, player_id, PRA, PA, PTS, REB, AST, STL, BLK,AR,PR): 
  "Rigth here we can inlude any and all stats you may think we need to make all sorts of calculations"

  self.player_id = player_id
  self.PRA = PRA
  self.PA = PA
  self.PTS = PTS
  self.REB = REB
  self.AST = AST
  self.STL = STL
  self.BLK = BLK
  self.AR = AR
  self.PR = PR

  "Function that collects the players stats"


 

def _extract_player_data(player_id):
  "Retraves the stats for specific player for a specific season"
  data = playergamelogs.PlayerGameLogs(
    season_nullable="2025-26",
    player_id_nullable=2544,
  )
  "Stores the data in a dataframe"
  df = data.get_data_frames()[0]
  return df

  
"Function that calcs the players stat that will connect with SB API"
def calc_stats():
  column = 0
  PRA_last_10_games = 0
  stats = _extract_player_data(2544)
  while column < 10:
    PRA_last_10_games += stats.iloc[column]["PTS"] + stats.iloc[column]["REB"] + stats.iloc[column]["AST"]
    column += 1
  PRA_last_10_games /= 10
  print(PRA_last_10_games)
"fit in the rest of the stats here"

calc_stats()
