from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route("/")
def main():
   return render_template('orgsDescriptions.html')
@app.route('/OrgsSummary')
def OrgsSummarymethod():
    return render_template('OrgsSummary.html')
if __name__ == "__main__":
	app.run()
	
