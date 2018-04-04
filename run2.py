#!flask/bin/python
from locare import app
import config2

app.run(debug=True,host='0.0.0.0',port=8000)
