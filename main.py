import os
import datetime

with open("log.txt", "w") as file:
    pass

def fakeCommit(days: int):
    if days < 1:
        os.system("git push")
    else:
        commit_date = datetime.datetime.now() - datetime.timedelta(days=days)
        date_str = commit_date.strftime("%Y-%m-%d")

        with open("log.txt", "a") as file:
            file.write(f"{date_str} \n")

        os.system("git add log.txt")
        os.system(f'git commit --date="{date_str}" -m "Commit for the day {date_str}"')

        # Recursive call to create commits for the next day
        fakeCommit(days - 1)

fakeCommit(365)
