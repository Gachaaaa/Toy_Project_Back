import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

def insert_review(gacha_id, user_id, review_text):
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute(
                    '''
                    INSERT INTO gachareview (gacha_id, user_id, review)
                    VALUES (%s, %s, %s)
                    RETURNING gachareview_id, gacha_id, user_id, review
                    ''',
                    (gacha_id, user_id, review_text)
                )
                created = cur.fetchone()
                conn.commit()
                return created
    except Exception as e:
        print("리뷰 삽입 오류:", e)
        return None

    
def get_reviews_by_gacha_id(gacha_id):
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute(
                    "SELECT * FROM gachareview WHERE gacha_id = %s ORDER BY gachareview_id DESC",
                    (gacha_id,)
                )
                return cur.fetchall()
    except Exception as e:
        print("특정 가챠 리뷰 조회 오류:", e)
        return []

