import os
from flask import Flask, render_template, Response, request

app = Flask(__name__)

# ---------- DIGITAL BUSINESS CARD DATA ----------
CARD = {
    "name": "Dakarai Albert Mapuranga",
    "title": "Chief Executive Officer",
    "org": "Big House Construction (BHC)",
    "tagline": "Business Executive • Entrepreneur • Construction & Infrastructure • Agriculture",
    "portrait": "images/portraits/hero.jpg",
    "contacts": [
        {
            "region": "Zimbabwe",
            "flag_code": "zw",
            "email": "dakaraim@gmail.com",
            "phone": "+263775113763",
            "phone_display": "+263 77 511 3763",
        },
        {
            "region": "Mozambique",
            "flag_code": "mz",
            "email": "dakaraim@bhccmmoz.mz",
            "phone": "+258840693312",
            "phone_display": "+258 84 069 3312",
        },
    ],
    # Pending client/Neo confirmation — brief section 10
    "linkedin": None,
    "bhc_website": None,
}

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/leadership")
def leadership():
    return render_template("leadership.html")

@app.route("/bhc")
def bhc():
    return render_template("bhc.html")

@app.route("/agriculture")
def agriculture():
    return render_template("agriculture.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/media")
def media():
    return render_template("media.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/card")
def card():
    # PUBLIC_BASE_URL lets you test the QR code on your phone before
    # deploying, e.g. set it to your machine's LAN IP or an ngrok URL:
    #   set PUBLIC_BASE_URL=http://192.168.1.20:5000   (Windows)
    #   export PUBLIC_BASE_URL=http://192.168.1.20:5000  (Mac/Linux)
    # Leave it unset in production, request.url will already be correct.
    base = os.environ.get("PUBLIC_BASE_URL")
    card_url = f"{base.rstrip('/')}/card" if base else request.url
    return render_template("card.html", card=CARD, card_url=card_url)

@app.route("/dakarai-mapuranga.vcf")
def card_vcf():
    c = CARD
    lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{c['name'].split()[-1]};{' '.join(c['name'].split()[:-1])};;;",
        f"FN:{c['name']}",
        f"ORG:{c['org']}",
        f"TITLE:{c['title']}",
    ]
    for contact_entry in c["contacts"]:
        lines.append(f"TEL;TYPE=CELL,VOICE:{contact_entry['phone']}")
        lines.append(f"EMAIL;TYPE=INTERNET:{contact_entry['email']}")
    lines.append(f"URL:{request.host_url.rstrip('/')}/")
    if c.get("bhc_website"):
        lines.append(f"URL:{c['bhc_website']}")
    lines.append("END:VCARD")
    body = "\r\n".join(lines) + "\r\n"
    return Response(
        body,
        mimetype="text/vcard",
        headers={
            "Content-Disposition": "attachment; filename=Dakarai-Mapuranga.vcf"
        },
    )


if __name__ == "__main__":
    app.run(debug=True)