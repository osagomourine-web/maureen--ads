from flask import Flask, request, redirect
app = Flask(__name__)
ads = []
MY_PIC = "https://cdn-icons-png.flaticon.com/512/149/149071.png"
MY_NAME = "Maureen - Eldoret"
# maureen 
@app.route("/")
def home():
    html = f"""<meta name="viewport" content="width=device-width"><style>body{{margin:0;font-family:sans-serif;background:#f0f2f5}}.top{{background:#25D366;color:white;padding:25px;text-align:center}}.top img{{width:90px;height:90px;border-radius:50%;border:3px solid white}}.content{{padding:15px}}.ad{{background:white;padding:15px;margin:10px 0;border-radius:10px;box-shadow:0 2px 5px #0001}}.btn{{background:#25D366;color:white;padding:12px 18px;text-decoration:none;border-radius:8px;display:inline-block}}</style><div class=top><img src="{MY_PIC}"><h2>{MY_NAME}</h2><p>Buy & Sell in Eldoret</p></div><div class=content><a class=btn href=/post>+ Post Your Ad</a><hr>"""
    if not ads: html += "<p>No ads yet. Be first!</p>"
    for a in reversed(ads):
        html += f"<div class=ad><h3>{a['title']}</h3><p>{a['desc']}</p><b>KES {a['price']}</b><br><br><a class=btn href='https://wa.me/{a['phone']}'>WhatsApp Seller</a></div>"
    return html + "</div>"

@app.route("/post")
def form():
    return '<meta name="viewport" content="width=device-width"><h2>Post Ad</h2><form action=/save method=post><input name=title placeholder="What are you selling?" style="width:90%;padding:10px"><br><br><textarea name=desc placeholder="Description" style="width:90%;padding:10px"></textarea><br><br><input name=price placeholder="Price" style="width:90%;padding:10px"><br><br><input name=phone placeholder="WhatsApp 2547..." style="width:90%;padding:10px"><br><br><button style="background:#25D366;color:white;padding:12px 20px;border:0;border-radius:8px">Publish</button></form>'

@app.route("/save", methods=["POST"])
def save():
    ads.append({"title":request.form["title"],"desc":request.form["desc"],"price":request.form["price"],"phone":request.form["phone"]})
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
