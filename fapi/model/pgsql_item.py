import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

def get_items_by_gacha_id(gacha_id):
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute(
                    "SELECT * FROM item WHERE gacha_id = %s ORDER BY item_id DESC",
                    (gacha_id,)
                )
                return cur.fetchall()
    except Exception as e:
        print("특정 가챠 아이템템 조회 오류:", e)
        return []