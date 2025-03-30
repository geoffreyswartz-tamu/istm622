import pandas as pd
import redis

#Set connection string for Redis DB
connectionString = redis.Redis(host='localhost', port=6379, db=0)

#Declare CSV path, initialize pandas dataframe on CSV
csv_path = '/home/ubuntu/customers.csv'
df = pd.read_csv(csv_path)

#Loop to iterate through first 10 rows in the CSV and create hash in RedisDB. 
#Converts each row to a dictionary to be handled before importing to Redis as a has.
#Uses customer as key, ID as value
for _, row in df.head(10).iterrows():
    key = f"customer:{row['ID']}"
    connectionString.hset(key, mapping=row.to_dict())