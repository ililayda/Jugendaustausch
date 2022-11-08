import schedule
import time
import Neue_Tabellen as nt
import loeschung as l
import Automatische_Loeschung as al

def job():
    al.main()
    l.main()
    nt.main()

schedule.every().day.at("11:07").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)