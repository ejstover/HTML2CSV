from bs4 import BeautifulSoup
import csv
import time
import os
import sys

row_text_array = []
#read the html
path = sys.argv[1]
output = sys.argv[2]
for filename in os.listdir(path):
	print (filename)
	html = open(path+filename).read()
	soup = BeautifulSoup(html, 'html.parser')

	# get the table from html
	table = soup.find(text="Status").find_parent("table")

	# find all rows
	rows = table.findAll('tr')

	# loop through rows and add row text to array
	for row in rows[1:]:
	    row_text = []
	    # loop through the elements
	    for row_element in row.findAll(['td']):
	        # append the array with the elements inner text
	        row_text.append(row_element.text.replace('\r', '').strip())
	    # append the text array to the row text array
	    row_text_array.append(row_text)

	# output csv
with open(output, "w") as f:
    wr = csv.writer(f)
    # loop through each row array
    for row_text_single in row_text_array:
        wr.writerow(row_text_single)