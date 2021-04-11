from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
@app.route("/<file>")
@app.route("/<file>/<first>")
@app.route("/<file>/<first>/<last>")

def home(file="Readme.txt",first=0,last=-1):
    
	try:    
		first=int(first)
		last=int(last)

		with open(file,"r",encoding="cp437") as file1:
			data_file=file1.readlines()

		if last==-1:
			last=len(data_file)
        
		return render_template("Navbar.html",data=data_file[first:last+1])
    #Exception Handling
	except (FileNotFoundError,TypeError,ValueError):
		return "Error Raised You  Passed Wrong Arguments Check Your Arguments Once"
    
	


# last lines
if __name__ =="__main__":
	app.run(debug=True)


