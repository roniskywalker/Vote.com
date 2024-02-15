import random
import psycopg2
import requests

BASE_URL = 'https://randomuser.me/api/?nat=in'
PARTIES = ["BJP", "INC", "AAP"]
random.seed(42)

def create_tables(conn, cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            candidate_id VARCHAR(255) PRIMARY KEY,
            candidate_name VARCHAR(255),
            party_affiliation VARCHAR(255),
            biography TEXT,
            campaign_platform TEXT,
            photo_url TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS voters (
            voter_id VARCHAR(255) PRIMARY KEY,
            voter_name VARCHAR(255),
            date_of_birth VARCHAR(255),
            gender VARCHAR(255),
            nationality VARCHAR(255),
            registration_number VARCHAR(255),
            address_street VARCHAR(255),
            address_city VARCHAR(255),
            address_state VARCHAR(255),
            address_country VARCHAR(255),
            address_postcode VARCHAR(255),
            email VARCHAR(255),
            phone_number VARCHAR(255),
            cell_number VARCHAR(255),
            picture TEXT,
            registered_age INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            voter_id VARCHAR(255) UNIQUE,
            candidate_id VARCHAR(255),
            voting_time TIMESTAMP,
            vote int DEFAULT 1,
            PRIMARY KEY (voter_id, candidate_id)
        )
    """)
    conn.commit()

def generate_candidate_data(candidate_number, total_parties):
    response = requests.get(BASE_URL + '&gender=' + ('female' if candidate_number % 2 == 1 else 'male'))
    if response.status_code == 200:
        user_data = response.json()['results'][0]
        return {
            "candidate_id": user_data['login']['uuid'],
            "candidate_name": f"{user_data['name']['first']} {user_data['name']['last']}",
            "party_affiliation": PARTIES[candidate_number % total_parties],
            "biography": "A brief bio of the candidate.",
            "campaign_platform": "Key campaign promises or platform.",
            "photo_url": user_data['picture']['large']
        }
    else:
        return "Error fetching data"

if __name__=="__main__":
    try:
        conn = psycopg2.connect("host=localhost dbname=voting user=postgres password=13975")
        cur = conn.cursor()

        create_tables(conn, cur)

        cur.execute("""
            SELECT * FROM candidates
        """)
        candidates = cur.fetchall()
        print(candidates)

        if len(candidates) == 0:
            for i in range(3):
                candidate = generate_candidate_data(i, 3)
                print(candidate)
                cur.execute("""
                            INSERT INTO candidates (candidate_id, candidate_name, party_affiliation, biography, campaign_platform, photo_url)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, (
                    candidate['candidate_id'], candidate['candidate_name'], candidate['party_affiliation'], candidate['biography'], candidate['campaign_platform'], candidate['photo_url']))
                conn.commit()

    except Exception as e:
        print(e)
