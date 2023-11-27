import os
import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_utilities import repeat_at
import requests

load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv("MYSQL_HOST"),
  user=os.getenv("MYSQL_USER"),
  password=os.getenv("MYSQL_PASSWORD"),
  database="btp"
)

print("Connected to Database:",mydb.is_connected())

mycursor = mydb.cursor()

try:
    mycursor.execute("\
        CREATE TABLE accidents \
        (\
        id BIGINT AUTO_INCREMENT PRIMARY KEY,\
        article_content TEXT,\
        short_descp MEDIUMTEXT,\
        date DATE,\
        place_name VARCHAR(255),\
        district VARCHAR(255),\
        state VARCHAR(255),\
        latitude DECIMAL(10, 8) NOT NULL,\
        longitude DECIMAL(11, 8) NOT NULL,\
        area_type VARCHAR(255),\
        accident_type VARCHAR(255),\
        persons_killed INT DEFAULT 0,\
        persons_grievously_injured INT DEFAULT 0,\
        persons_minor_injured INT DEFAULT 0,\
        no_motorized_vehicles INT DEFAULT 0,\
        no_non_moterized_vehicles INT DEFAULT 0,\
        no_pedestrians_involved INT DEFAULT 0,\
        collosion_type VARCHAR(255),\
        road_type VARCHAR(255)\
        )")
    print("accidents table created")
except mysql.connector.errors.DatabaseError as e:
    print("database error")
    print(e)
except Exception as e:
    print(e)

def insert_news_db(news_details):
    global mycursor
    resp = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={news_details["place_name"],news_details["district"],news_details["state"]}&key=AIzaSyCDJ28lMyK7UbSUNUN_KeMTZa-rzd0GiWU')
    
    resp=resp.json()
    
    news_details["article_content"] = news_details["article_content"].replace('"', "")
    news_details["article_content"] = news_details["article_content"].replace("'", "")
    news_details["short_descp"] = news_details["short_descp"].replace('"', "")
    news_details["short_descp"] = news_details["short_descp"].replace("'", "")
    
    print(resp["results"][0])
    print(resp["results"][0]["geometry"]["location"])
    mycursor.execute(f'''INSERT INTO accidents (article_content, short_descp, date, place_name, district, state, latitude, longitude, area_type, accident_type, persons_killed, persons_grievously_injured, persons_minor_injured, no_motorized_vehicles, no_non_moterized_vehicles, no_pedestrians_involved, collosion_type, road_type) VALUES ("{news_details["article_content"]}", "{news_details["short_descp"]}", "{news_details["date"]}","{news_details["place_name"]}", "{news_details["district"]}", "{news_details["state"]}", {resp["results"][0]["geometry"]["location"]["lat"]}, {resp["results"][0]["geometry"]["location"]["lng"]}, "{news_details["area_type"]}", "{news_details["accident_type"]}", {news_details["persons_killed"]}, {news_details["persons_grievously_injured"]}, {news_details["persons_minor_injured"]}, {news_details["no_motorized_vehicles"]}, {news_details["no_non_moterized_vehicles"]}, {news_details["no_pedestrians_involved"]}, "{news_details["collosion_type"]}", "{news_details["road_type"]}");''')
    mydb.commit()
    mycursor.execute("SELECT * FROM accidents;")
    print(mycursor.fetchall())

app = FastAPI()

@app.on_event("startup")
@repeat_at(cron="*/10 * * * * *") #every 2nd minute
async def fetch_news():
    print("hey")

@app.get("/news")
async def root():
    return {"message": "Hello World"}