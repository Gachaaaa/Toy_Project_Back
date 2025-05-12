import psycopg
import psycopg_pool
from config import config

# 커넥션 풀 생성
pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

def draw_gacha(gacha_id, user_id):
    """
    특정 가챠(gacha_id)에서 랜덤으로 아이템 하나를 뽑고,
    수량을 1 감소시키며, 뽑기 결과를 gachadraw 테이블에 기록한다.
    """
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                
                # 1. 남은 수량이 있는 아이템 중 랜덤으로 하나 선택
                cur.execute(
                    '''
                    SELECT * FROM item
                    WHERE gacha_id = %s AND quantity > 0
                    ORDER BY random()
                    LIMIT 1
                    ''',
                    (gacha_id,)
                )
                item = cur.fetchone()

                if not item:
                    # 남은 아이템 없음
                    return None

                item_id = item["item_id"]

                # 2. 해당 아이템 수량 1 감소
                cur.execute(
                    '''
                    UPDATE item
                    SET quantity = quantity - 1
                    WHERE item_id = %s
                    ''',
                    (item_id,)
                )

                # 3. gachadraw 기록 추가
                cur.execute(
                    '''
                    INSERT INTO gachadraw (user_id, gacha_id)
                    VALUES (%s, %s)
                    RETURNING gachadraw_id
                    ''',
                    (user_id, gacha_id)
                )
                draw_record = cur.fetchone()
                conn.commit()

                return {
                    "draw_id": draw_record["gachadraw_id"],
                    "item": item
                }

    except Exception as e:
        print("가챠 뽑기 오류:", e)
        return None
