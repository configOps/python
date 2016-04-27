import csv
def add_row(info):
    with open('document.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(info)
	return;
add_row("hello")
