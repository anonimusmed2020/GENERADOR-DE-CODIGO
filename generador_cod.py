#!/usr/bin/env python

from random import SystemRandom
import time
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='crypdxzp_datauser', password='BE5zXImvh-7zi3bKOmxp', database='crypdxzp_data', host='127.0.0.1', port='3306')
cursor = mariadb_connection.cursor()

if __name__ == "__main__":
    while True:
        longitud = 7
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

        cryptogen = SystemRandom()
        p = ""
        while longitud > 0:
            p = p + cryptogen.choice(valores)
            longitud = longitud - 1
        data = 1
        cursor.execute("""UPDATE crypto_code_bot SET gen_code = %s WHERE code_id = %s""",(p, data))
        mariadb_connection.commit()
        print(p)
        time.sleep(1)
