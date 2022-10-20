from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    with open(path, encoding="utf-8") as file:
        result = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = result
        jobs = []
        for row in data:
            new_row = {}
            for item in row:
                new_row.update({header[row.index(item)]: item})
            jobs.append(new_row)
    return jobs
