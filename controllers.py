import feedparser
from flask import Flask
from flask import render_template
from flask import request
from flask import render_template_string
from flask_menu import Menu, register_menu

class Controller:
    def __init__(self, host='localhost:8090', un='aaron.jacobs', pw='rr4CWs7f', account_name='customer1', https_enabled='f', bus_app_dict=''):
        self.update(host, un, pw, account_name, https_enabled, bus_app_dict)

    def update(self, host, un, pw, account_name, https_enabled, bus_app_dict):
        self.host = host
        self.un = un
        self.pw = pw
        self.account_name = account_name
        self.user_at_account_name = self.un + "@" + self.account_name
        self.https_enabled = https_enabled
        self.bus_app_dict = bus_app_dict
        if self.https_enabled == 't':
            self.url = 'https://' + host
        elif self.https_enabled == 'f':
            self.url = 'http://' + host
        else:
            print('t or f not entered so default chosen, default - SSL=True')

    def reset(self):
        self.update('', '', '', '', '', '')

app = Flask(__name__)
Menu(app=app)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za.library.collin.edu/cmlink/1.640'}
             
MAIN_MENU = {'0': 'enter-source-controller',
			 '1': 'app-model-api',
			 '2': 'metric-and-snapshot-api',
			 '3': '',
			 '4': '',
			 '5': '',
			 '6': '',
			 '7': ''}
			 
def tmpl_show_menu():
	#for key, value in MAIN_MENU.items():
	#	print('key: ', key)
	#	print('value: ', value)
    return render_template("home.html")
        
@app.route('/')
@register_menu(app, '.', 'Home')
def index():
    return tmpl_show_menu()

@app.route('/configure-source-controller')
@register_menu(app, '.first', 'Configure Source Controller', order=0)
def configure_source_controller():
    return render_template("input_source_controller.html")

#Application Model API
@app.route('/list-all-apps')
@register_menu(app, '.second', 'Retrieve All Business Applications', order=1)
def list_all_apps():
    return render_template("list_all_apps.html")

@app.route('/metric-snapshot-api')
@register_menu(app, '.third', 'Retrieve All Business Transactions in a Business Application', order=2)
def metric_snapshot_api_menu():
    return tmpl_show_menu()

#########################################################


if __name__ == "__main__":
    app.run(port=5000, debug=True)