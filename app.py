from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/queryEanAlkomprar', methods=['GET'])
def queryEanAlkomprar():
    from scrapyManager import queryEanAlkomprar
    ean = request.args.get('ean')
    return jsonify(queryEanAlkomprar(ean))

@app.route('/queryEanMercadoLibre', methods=['GET'])
def queryEanMercadoLibre():
    from scrapyManager import queryEanMercadoLibre
    ean = request.args.get('ean')
    return jsonify(queryEanMercadoLibre(ean))

if __name__ == '__main__':
    app.run(debug=True)