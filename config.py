import web

db_host = 'fnx6frzmhxw45qcb.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'p2mgkxpzrul8p1ke'
db_user = 'fyfu0p8gkw1dp31x'
db_pw = 'spb9bbyb0dsqqyfn'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )