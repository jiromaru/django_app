##############################importの設定######################################
import urllib.request
import os
import sqlite3
import sys
from mk_display import mk_display
from get_data import get_data

##############################パラメータの設定##################################
msg="正常"
stock_no_url="http://kabusapo.com/dl-file/dl-stocklist.php"
base_url="https://info.finance.yahoo.co.jp/history/?code="
stock_no_file="stock_no.csv"

if os.path.exists(stock_no_file) == False:
    urllib.request.urlretrieve(stock_no_url, stock_no_file)

param_list=mk_display(stock_no_file)

if len(param_list[2])==0:
    print("銘柄が選択されていません")
    sys.exit()

kisyu_list=param_list[0]
start_ym,fin_ym=param_list[1]
mei_no_list=param_list[2]

#MySQLの接続
conn=sqlite3.connect("db.sqlite3")
cur=conn.cursor()
try:
    for mei_no in mei_no_list:
        for period in kisyu_list:
            cur.execute("CREATE TABLE IF NOT EXISTS {0}_{1} (date varchar(10),open integer,top integer,low integer,close integer,dekidaka integer,close_adjust integer) ;".format(period,mei_no))
            cur.execute("CREATE TABLE IF NOT EXISTS {0}_{1}_temp (date varchar(10),open INTEGER,top INTEGER,low INTEGER,close INTEGER,dekidaka INTEGER,close_adjust INTEGER);".format(period,mei_no))
            get_data(mei_no,base_url,start_ym,fin_ym,period,cur)
            cur.execute("INSERT INTO {0}_{1} SELECT a.* from {0}_{1}_temp a left join {0}_{1} b on a.date=b.date where b.date IS NULL;".format(period,mei_no))
            cur.execute("DROP TABLE {0}_{1}_temp;".format(period,mei_no))
except:
    msg="異常"
finally:
    print(msg+"終了")
    conn.commit()
    cur.close()
    conn.close()
