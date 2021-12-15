import urllib.request, urllib.error, urllib.parse, json, webbrowser
from flask import Flask, render_template, request

baseurl = "http://store.steampowered.com/api/"

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def safe_get(url):
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request." )
        print("Error code: ", e.code)
    except urllib.error.URLError as e:
        print("We failed to reach a server")
        print("Reason: ", e.reason)
    return None

def appdetails(appid, filters = ''):
    params = {"appids": appid, "filters": filters}
    url = baseurl + "appdetails?" + urllib.parse.urlencode(params)
    data = json.loads(safe_get(url))
    return data

def featuredcategories(genre) {
    url = baseurl + "featuredcategories"
    

}

app = Flask(__name__)


@app.route('/')
def main_handler():
    return render_template('mainpage.html', page_title='Game Manager')

@app.route('/homepage')
def homepage_handler():
    username = request.args.get('username')
    if(get_games(username) == None) {
        return render_template("homepage.html", page_title='honepage'， name=username)
    } else {
        return render_template("mainpage.html", page_title="mainpage - Error", prompt = "The steam ID is either invalid or private")
    }


if __name__ == '__main__':
    app.run(host="georges-MacBook-Pro.local", port=8080, debug=True)

print(pretty(appdetails("1506440","")))
