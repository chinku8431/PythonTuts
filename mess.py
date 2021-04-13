import schedule

def job():
    print("hello python students")

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()