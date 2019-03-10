from blueprint import db
from flask_restful import fields
from blueprint.client import __init__

class ListMobil(db.Model):

    __tablename__ = "ListMobil"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))
    merk_mobil = db.Column(db.String(255), nullable=False)
    model_mobil = db.Column(db.String(255), nullable=False)
    transmisi = db.Column(db.String(255), nullable=False)
    jarak_tempuh = db.Column(db.Integer, nullable=False)
    tahun = db.Column(db.Integer, nullable=False)
    tipe_bahan_bakar = db.Column(db.String(255), nullable=False)
    warna_mobil = db.Column(db.String(255), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    judul_lapak = db.Column(db.Text, nullable=True)
    deskripsi_lapak = db.Column(db.Text, nullable=True)
    # gambar = 

    response_field = {
        'id' : fields.Integer,
        'client_id' : fields.Integer,
        'created_at' : fields.String,
        'updated_at' : fields.String,
        'merk_mobil' : fields.String,
        'model_mobil' : fields.String,
        'transmisi' : fields.String,
        'jarak_tempuh' : fields.Integer,
        'tahun' : fields.Integer,
        'tipe_bahan_bakar' : fields.String,
        'warna_mobil' : fields.String,
        'harga' : fields.Integer,
        'judul_lapak' : fields.String,
        'deskripsi_lapak' : fields.String
    }
    def __init__(self, id, client_id, created_at, updated_at, merk_mobil, model_mobil, transmisi, jarak_tempuh, tahun, tipe_bahan_bakar, warna_mobil, harga, judul_lapak, deskripsi_lapak):
        
        self.id = id
        self.client_id = client_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.merk_mobil = merk_mobil
        self.model_mobil = model_mobil
        self.transmisi = transmisi
        self.jarak_tempuh = jarak_tempuh
        self.tahun = tahun
        self.tipe_bahan_bakar = tipe_bahan_bakar
        self.warna_mobil = warna_mobil
        self.harga = harga
        self.judul_lapak = judul_lapak
        self.deskripsi_lapak = deskripsi_lapak

    def __repr__(self):
        return '<Mobil %r>' % self.id