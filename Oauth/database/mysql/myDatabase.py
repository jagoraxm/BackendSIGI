import pymysql


def obtener_conexion():
    #return pymysql.connect(host='127.0.0.1', user='root', password='root', db='SIGI', port=8889)
    return pymysql.connect(host='roundhouse.proxy.rlwy.net', user='root', password='FfNmAOLVGPkIpORMPZbnYROsWhQPsGNF', db='railway', port=38158)