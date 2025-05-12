import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

def create_delivery(user_id, item_id, address):
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute(
                    '''
                    INSERT INTO delivery (user_id, item_id, address, status, scheduled_date)
                    VALUES (%s, %s, %s, %s, NOW())
                    RETURNING delivery_id, user_id, item_id, address, status, scheduled_date
                    ''',
                    (user_id, item_id, address, "배송 대기")
                )
                created = cur.fetchone()
                conn.commit()
                return created
    except Exception as e:
        print("배송 요청 오류:", e)
        return None
