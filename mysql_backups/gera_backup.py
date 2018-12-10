import os
import time

db_User_Name = 'arthurbarcellos'
DB_User_Password = 'tutuskt0'
DB_Name = 'arthurbarcellos$newlojas'
backupDir = '/home/arthurbarcellos/mysite/app_proximo/mysql_backups/backup'
DB_table = 'cliente'

datetime = time.strftime('%d%m%Y')
datetimeBackupDir = backupDir + datetime

if not os.path.exists(datetimeBackupDir):
    os.makedirs(datetimeBackupDir)


#mysqldump -u [user] -p[pass] --no-create-info mydb > mydb.sql
#mysqldump_cmd = "mysqldump -u -p --no-create-info" + db_User_Name + " --password=" + DB_User_Password + "' -h caroluchoa.mysql.pythonanywhere-services.com '" '"  "'+ DB_Name" + " DB_table ' > "' + datetimeBackupDir + "/" + datetime + ".txt"
mysqldump_cmd ="mysqldump -u " + db_User_Name + " -h arthurbarcellos.mysql.pythonanywhere-services.com --no-create-info --no-create-db --no-tablespaces --no-set-names --no-autocommit --skip-set-charset --xml 'arthurbarcellos$newlojas' "+ DB_table + "> "+ datetimeBackupDir+"/"+datetime+".xml"

#mysqldump_cmd = "mysqldump -p -u " + db_User_Name + " --password='" + DB_User_Password + "' -h caroluchoa.mysql.pythonanywhere-services.com --databases '" + DB_Name + "' " DB_table +'" > "' + datetimeBackupDir + "/" + datetime + ".txt"
os.system(mysqldump_cmd)

