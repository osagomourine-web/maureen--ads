from flask import Flask,request,redirect
app=Flask(__name__)
ads=[]
@app.route("/")
def home():
 h="<h2>Maureen Ads</h2><a href='/post'>Post</a><hr>"
 if not ads:
  h+="<p>No ads yet</p>"
 for a in ads[::-1]:
  h+=f"{a[0]}<br>{a[1]}<br>{a[2]}<hr>"
 return h
@app.route("/post")
def form():
 return "<form action='/save' method='POST'><input name='t' required><br><textarea name='d' required></textarea><br><input name='p' required><br><button>Save</button></form>"
@app.route("/save",methods=["POST"])
def save():
 ads.append((request.form["t"],request.form["d"],request.form["p"]))
 return redirect("/")
app.run(host="0.0.0.0",port=10000)
