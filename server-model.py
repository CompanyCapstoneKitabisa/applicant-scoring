from flask import Flask, jsonify, request
from scoring_new_form import scoring_process

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    ##scoring
    data = {
        "Provinsi": request.get_json(force=True)['data']['Provinsi'],
        "Kota/Kabupaten": request.get_json(force=True)['data']['Kota/Kabupaten'],
        "Medsos": request.get_json(force=True)['data']['Medsos'],
        "Status Rumah":  request.get_json(force=True)['data']['Status Rumah'],
        "NIK": request.get_json(force=True)['data']['NIK'],
        "Foto KTP": request.get_json(force=True)['data']['Foto KTP'],
        "Foto Rumah": request.get_json(force=True)['data']['Foto Rumah'],
        "Cerita Penggunaan Dana": request.get_json(force=True)['data']['Cerita Penggunaan Dana'],
        "Cerita Latar Belakang": request.get_json(force=True)['data']['Cerita Latar Belakang'],
        "Cerita Perjuangan": request.get_json(force=True)['data']['Cerita Perjuangan'],
        "Beasiswa Penting": request.get_json(force=True)['data']['Beasiswa Penting'],
        "Cerita Kegiatan": request.get_json(force=True)['data']['Cerita Kegiatan'],
    }

    dataFetched = scoring_process(data)

    return dataFetched

@app.route('/testConnection', methods=['GET'])
def test():
    return "Kitabisa scholarship management model"

if __name__ == "__main__":
    app.run()