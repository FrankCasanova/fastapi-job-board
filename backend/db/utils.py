import databases
from db.session import SQLALCHEMY_DATABASE_URL


async def check_db_connected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("Database is connected (^_^)")
    except Exception as e:
        print("Looks like there is some problem in connection,see below traceback")
        raise e


# Note for sqlite it might not work, reason:
# For newer version of sqlalchemy (1.3.24 +), We might get 'RowProxy ImportError', It is not recommended to move backward as sqlalchemy newer versions are supporting async while 1.3.* versions are not async compatible.
