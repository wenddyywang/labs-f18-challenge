from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<var>')
def pokemon(var):
	url = "http://pokeapi.co/api/v2/pokemon/" + var + "/"
	payload = ""
	response = requests.request("GET", url, data=payload)

	data = response.json()
	if var.isdigit():
		name = data['name']
		search_val = 'id'
		return render_template('pokemon.html', searchVal=search_val, name=name, idNum=var)
		# return name
	else:
		id_num = data['id']
		search_val = 'name'
		# return id_num
		return render_template('pokemon.html', searchVal=search_val, name=var, idNum=id_num)

if __name__ == '__main__':
    app.run()
