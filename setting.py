pip install dj-database-url
import dj-database-url
import os
DATABASES = {
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_dw78_user:Qv3uJ0FvIb55tgTFQZrbIu1ypTkG6rx6@dpg-d0epgk95pdvs73au8udg-a.oregon-postgres.render.com/test_db_dw78"))
}
