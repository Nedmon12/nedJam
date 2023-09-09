#import redis
#r = redis.Redis(host='localhost',port=6379,decode_responses=True)
# Sorry Redis not now atleast :(

# r.hset('yotubeId','file path')

import sqlite3

connection = sqlite3.connect("test.db")

cur = connection.cursor()

# cur.execute("CREATE TABLE songs (id, songTitle, path)")

cur.execute("""
    INSERT INTO songs VALUES
            ('The Weekend - Heartless (Official Video)', 'The Weekend - Heartless (Official Video)-1DpH-icPpl0'),
            ('Glass Animals - Heat Waves (Official Video)','Glass Animals - Heat Waves (Official Video)-mRD0-GxqHVo'),
            ('Gotye - Somebody That I Used to Know (feat. Kimbra) [Official Music Video]','Gotye - Somebody That I Used to Know (feat. Kimbra) [Official Music Video]-8UVNT4wvIGY.mp3'),
""")
            
connection.commit()





