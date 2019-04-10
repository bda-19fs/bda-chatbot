# How to use app.py
python .\app.py "let's see some italian restaurants"

# Or flask
$env:FLASK_APP = "app.py"
flask run
python -m flask run (alternative)

curl localhost:5000/query?msg=Im%20interested%20in%20italian%20restaurants