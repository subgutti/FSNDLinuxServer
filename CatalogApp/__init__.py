from flask import Flask

app = Flask(__name__)

# Import the app's main configuration file
import project

if __name__ == "__main__":
	# Listen on all public IPs
    app.run(host='0.0.0.0')
