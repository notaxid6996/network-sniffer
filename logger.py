
import csv

def save_log(rows):

    with open(
        "network_log.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Process", "IP", "Port", "Risk"]
        )

        for row in rows:
            writer.writerow(rows)