import csv
import datetime
import re


class File_Reader:

    def load_csv_file(self):
        with open('work_log.csv', newline='') as csvfile:
            work_loads = csv.DictReader(csvfile)
            rows = list(work_loads)
        return rows


class FileWriter:

    def write_entry_first_time(self, task, time_spent, notes, date):
        real_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        with open('work_log.csv', 'a+', newline='') as csvfile:
            fieldnames = ['task', 'time_spent', 'notes', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {'task': task, 'time_spent': time_spent, 'notes': notes,
                 'date': real_date.strftime("%d/%m/%Y")})

    def write_entry_append(self, task, time_spent, notes, date):
        real_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        with open('work_log.csv', 'a+', newline='') as csvfile:
            fieldnames = ['task', 'time_spent', 'notes', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'task': task, 'time_spent': time_spent, 'notes': notes,
                 'date': real_date.strftime("%d/%m/%Y")})


class DataSearch:
    def find_by_date(self, date):
        file_ob = File_Reader()
        data = file_ob.load_csv_file()
        return_list = []
        real_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        for entries in data:
            if entries.get("date") == real_date.strftime("%d/%m/%Y"):
                return_list.append(entries)

        return return_list

    def find_by_time_spent(self, time):
        realtime = int(time)
        file_ob = File_Reader()
        data = file_ob.load_csv_file()
        return_list = []
        for entries in data:
            if int(entries.get("time_spent")) == realtime:
                return_list.append(entries)

        return return_list

    def find_by_name(self, name):
        file_ob = File_Reader()
        data = file_ob.load_csv_file()
        return_list = []
        for entries in data:
            if name in entries.get("task") or name in entries.get("notes"):
                return_list.append(entries)

        return return_list

    def find_by_regex(self, pattern):
        file_ob = File_Reader()
        data = file_ob.load_csv_file()
        return_list = []
        search_pattern = re.compile(pattern)
        for entries in data:
            if search_pattern.search(
                    entries.get("task")) or search_pattern.search(
                    entries.get("notes")) is not None:
                return_list.append(entries)
            else:
                pass

        return return_list
