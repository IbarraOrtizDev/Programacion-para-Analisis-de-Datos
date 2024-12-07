from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def queryTogether():
    from src.scrapyManager import queryEan
    ean = request.args.get('ean')
    return jsonify(queryEan(ean))

@app.route('/queryEanAlkomprar', methods=['GET'])
def queryEanAlkomprar():
    from src.scrapyManager import queryEanAlkomprar
    ean = request.args.get('ean')
    return jsonify(queryEanAlkomprar(ean))

@app.route('/queryEanMercadoLibre', methods=['GET'])
def queryEanMercadoLibre():
    from src.scrapyManager import queryEanMercadoLibre
    ean = request.args.get('ean')
    return jsonify(queryEanMercadoLibre(ean))

if __name__ == '__main__':
    app.run(debug=True)