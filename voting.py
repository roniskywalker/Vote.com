import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect("host=localhost dbname=voting user=postgres password=postgres") #start connection to postgres
    cur = conn.cursor() #connect to postgres, create table, get queries, run, get result

    candidates_query = cur.execute(
    """
        SELECT row_to_json(t)
        FROM (
            SELECT * FROM candidates
        ) t;
    """
    )
    candidates = cur.fetchall()
    candidates = [candidate[0] for candidate in candidates]
    if len(candidates) == 0:
        raise Exception("No candidates found in database")
    else:
        print(candidates)