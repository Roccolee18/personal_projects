# The main program for this project

# import client from inference_sdk
from inference_sdk import InferenceHTTPClient
# import os to get the API_KEY from the environment
import os
import numpy as np
import mysql.connector
from datetime import datetime
tiles = []
counts = []
currTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Establishing connection to the MySQL database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Rl13082002!',
    database = 'mjtilekeeper'
)
mycursor = mydb.cursor()


# Establishing API connection to Roboflow, which is the machine-learning based vision system trained to identify tiles from a hand
client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="oyhttZJduhrKFlfI7p2t"
)

# Passing the input image to the model and recieving results
results = client.infer("./hands/hand1.png", model_id="majsoul-6igdu/1")
# print (results)

# print the results
for pred in results['predictions']:
    tiles.append(pred['class'])

# Matching the results to individual tiles
for i in range(len(tiles)):
    match tiles[i]:
        case '10':
            tiles[i] = 'r5m'
        case '11':
            tiles[i] = '1m'
        case '12':
            tiles[i] = '2m'
        case '13':
            tiles[i] = '3m'
        case '14':
            tiles[i] = '4m'
        case '15':
            tiles[i] = '5m'
        case '16':
            tiles[i] = '6m'
        case '17':
            tiles[i] = '7m'
        case '18':
            tiles[i] = '8m'    
        case '19':
            tiles[i] = '9m'
        case '30':
            tiles[i] = 'r5p'
        case '31':
            tiles[i] = '1p'
        case '32':
            tiles[i] = '2p'
        case '33':
            tiles[i] = '3p'
        case '34':
            tiles[i] = '4p'
        case '35':
            tiles[i] = '5p'
        case '36':
            tiles[i] = '6p'
        case '37':
            tiles[i] = '7p'
        case '38':
            tiles[i] = '8p'    
        case '39':
            tiles[i] = '9p'
        case '50':
            tiles[i] = 'r5s'
        case '51':
            tiles[i] = '1s'
        case '52':
            tiles[i] = '2s'
        case '53':
            tiles[i] = '3s'
        case '54':
            tiles[i] = '4s'
        case '55':
            tiles[i] = '5s'
        case '56':
            tiles[i] = '6s'
        case '57':
            tiles[i] = '7s'
        case '58':
            tiles[i] = '8s'    
        case '59':
            tiles[i] = '9s'
        case '74':
            tiles[i] = 'north'
        case '71':
            tiles[i] = 'east'
        case '72':
            tiles[i] = 'south'
        case '73':
            tiles[i] = 'west'
        case '76':
            tiles[i] = 'green'
        case '75':
            tiles[i] = 'white'
        case '77':
            tiles[i] = 'red'
        
tiles.sort()
# print(tiles)

# Appending the count of tiles and the current time to a list
for i in range(len(tiles)):
    currTileCount = 0
    currTile = tiles[i]
    for j in range(len(tiles)):
        if tiles[i] == tiles[j]:
            currTileCount += 1
    counts.append((tiles[i],currTileCount,currTime))

uniqueList = list(dict.fromkeys(counts))
print(uniqueList)

# Inserting the sorted list to the MySQL database
sqlInsert = "INSERT INTO tile_counter (tile, count, posting_time) VALUES (%s, %s, %s);"
mycursor.executemany(sqlInsert, uniqueList)
mydb.commit()

# From here, a PowerBI dashboard is connected to the database to act as a front end and perform analysis on the collected data in the form of various visualizations
# Once new data is imported to the MySQL database, the dashboard simply has to be refreshed for new data to be analyzed and visualized