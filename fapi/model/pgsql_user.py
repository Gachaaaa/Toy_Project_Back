import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

def insert_user(user):
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute(
                    '''
                    INSERT INTO users (login_id, password, phone_number, name, email)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING user_id, login_id, phone_number, name, email
                    ''',
                    (user.login_id, user.password, user.phone_number, user.name, user.email)
                )
                created = cur.fetchone()
                conn.commit()
                return created
    except Exception as e:
        print("Error inserting user:", e)
        return None
    

def verify_user_login(login_id: str, password: str):
    try:
        with pool_default.connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute(
                    '''
                    SELECT user_id, login_id, phone_number, name, email
                    FROM users
                    WHERE login_id = %s AND password = %s
                    ''',
                    (login_id, password)
                )
                return cur.fetchone()  # 일치하는 유저 반환
    except Exception as e:
        print("Login error:", e)
        return None