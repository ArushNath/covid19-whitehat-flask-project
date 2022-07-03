#import flask library
from flask import render_template, Flask, request

#initialize flask
webpage = Flask(__name__)

#route your webpage
@webpage.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	# Render HTML with count variable
	return render_template("index.html", readerCount=visitors_count)

@webpage.route("/", methods=["POST"])
#route your webpage
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	#complete the code
	countryInput = request.form["countryInput"]
	coutnryInput = "https://covid-api-262.herokuapp.com/?country="+countryInput
	return render_template("index.html", readerCount=visitors_count, pieChart=countryInput)

#add code for executing flask
if __name__ == "__main__":
	webpage.run(host='127.0.0.1', port=1800)