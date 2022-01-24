# import mysql.connector
from numpy import hstack
from Model.Connection import querySQL

from Config.Settings import DATABASE_NAME


def getDaftarTabel():
    return hstack(querySQL(f"SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_TYPE LIKE 'VIEW' AND TABLE_SCHEMA LIKE '{DATABASE_NAME}'"))


def getDaftarKolom():
    return hstack(querySQL(
        f"SELECT col.column_name FROM information_schema.columns col JOIN information_schema.views vie ON vie.table_schema=col.table_schema AND vie.table_name=col.table_name where col.table_schema not in ('sys', 'information_schema','mysql', 'performance_schema') AND vie.table_schema='{DATABASE_NAME}'"))


def getDaftarRelasi():
    return querySQL(
        "SELECT `TABLE_NAME`, `COLUMN_NAME`, `REFERENCED_TABLE_SCHEMA`,`REFERENCED_TABLE_NAME`,`REFERENCED_COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`KEY_COLUMN_USAGE` WHERE`TABLE_SCHEMA`=SCHEMA() AND `REFERENCED_TABLE_NAME` IS NOT NULL")
