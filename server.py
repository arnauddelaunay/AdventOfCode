from flask import Flask
from flask import jsonify

app = Flask(__name__)

test_neighbors = [
	{
		'label' : 'dog',
		'similarity' : .92
	},
	{
		'label' : 'cat',
		'similarity' : .51
	}
]

@app.route('/')
def index():
  return 'Hello world'

@app.route('/find/<str:request>')
def get_neighbors(request):
  return jsonify(
  	request=request,
  	neighbors=test_neighbors
  )

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')