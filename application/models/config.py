import web

db_host = 'localhost'
db_name = 'advihawk'
db_user = 'advihawk'
db_pw = 'advihawk.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )