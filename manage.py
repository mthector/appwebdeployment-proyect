from flask import Flask # type: ignore
from app import app, db
from databases.db import *
import config as custom_config

app = Flask(__name__)
app.config.from_object(custom_config)
db = SQLAlchemy(model_class=Base)
db.init_app(app)
app.config['DEBUG'] = True

def create_tables():
    "Create relational database tables"
    with app.app_context():
        db.create_all()


def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA"
    with app.app_context():
        db.drop_all()


def add_data_tables():
    with app.app_context():
        db.create_all()

        categories = [
            Category(name="Drums"),
            Category(name="Metal Wind"),
            Category(name="Woodwind"),
            Category(name="Ropes"),
            Category(name="Others")
        ]

        suppliers = [
            Supplier(name="NP Drums"),
            Supplier(name="Sanganxa"),
            Supplier(name="Yamaha"),
            Supplier(name="Luthier"),
            Supplier(name="Iberpiano")
        ]


        db.session.add_all(categories)
        db.session.add_all(suppliers)
        db.session.commit()

        i1 = Instrument(name = "Trumpet", image="https://www.sanganxa.com/525-medium_default/trompeta-bach-180ml-37-25-plateada-sib.jpg", image_2="https://www.sanganxa.com/42919-large_default/trompeta-bach-180ml-37-25-plateada-sib.jpg")
        i1.category_id = categories[1].id
        i1.supplier_id = suppliers[2].id

        i2 = Instrument(name = "Clarinet", image="https://www.sanganxa.com/27672-medium_default/clarinete-jupiter-jcl700n-en-sib.jpg", image_2="https://www.sanganxa.com/33838-large_default/clarinete-yamaha-ycl-255-s-llaves-plateadas.jpg")
        i2.category_id = categories[2].id
        i2.supplier_id = suppliers[1].id

        i3 = Instrument(name = "Horn", image="https://www.sanganxa.com/33592-large_default/trompa-alexander-103-mla.jpg", image_2="https://www.sanganxa.com/281-large_default/trompa-yamaha-yhr-567d-campana-desmontable.jpg")
        i3.category_id = categories[1].id
        i3.supplier_id = suppliers[2].id

        i4 = Instrument(name = "Trombone", image="https://www.sanganxa.com/33162-large_default/trombon-getzen-4147ib-ian-bousfield.jpg", image_2="https://www.sanganxa.com/33167-large_default/trombon-getzen-4147ib-ian-bousfield.jpg")
        i4.category_id = categories[1].id
        i4.supplier_id = suppliers[2].id

        i5 = Instrument(name = "Tuba", image="https://www.sanganxa.com/34193-large_default/tuba-eastman-ebc632s-plateada.jpg", image_2="https://www.sanganxa.com/25416-large_default/tuba-eastman-ebc632s-plateada.jpg")
        i5.category_id = categories[1].id
        i5.supplier_id = suppliers[2].id

        i6 = Instrument(name = "Saxophone", image="https://www.sanganxa.com/28510-large_default/saxo-alto-yamaha-yas-280-s-plateado.jpg", image_2="https://www.sanganxa.com/28509-large_default/saxo-alto-yamaha-yas-280-s-plateado.jpg")
        i6.category_id = categories[2].id
        i6.supplier_id = suppliers[2].id

        i7 = Instrument(name = "Tenor Saxophone", image="https://www.sanganxa.com/40315-large_default/saxo-tenor-yamaha-yts-280-plateado.jpg", image_2="https://www.sanganxa.com/40314-large_default/saxo-tenor-yamaha-yts-280-plateado.jpg")
        i7.category_id = categories[2].id
        i7.supplier_id = suppliers[3].id

        i8 = Instrument(name = "Soprano Saxophone", image="https://www.sanganxa.com/28230-large_default/saxo-soprano-selmer-jubile-sii-gg.jpg", image_2="https://www.sanganxa.com/28229-large_default/saxo-soprano-selmer-jubile-sii-gg.jpg")
        i8.category_id = categories[2].id
        i8.supplier_id = suppliers[3].id

        i9 = Instrument(name = "Flügelhorn", image="https://www.sanganxa.com/31588-large_default/fliscorno-jupiter-jfh-1100-rs.jpg", image_2="https://www.sanganxa.com/31590-large_default/fliscorno-jupiter-jfh-1100-rs.jpg")
        i9.category_id = categories[2].id
        i9.supplier_id = suppliers[3].id

        i10 = Instrument(name = "Bassoon", image="https://www.sanganxa.com/30845-large_default/fagot-yamaha-yfg-812-c-ii-opt4-blr2.jpg", image_2="https://www.sanganxa.com/30502-large_default/fagot-yamaha-yfg-812-c-ii-opt4-blr2.jpg")
        i10.category_id = categories[2].id
        i10.supplier_id = suppliers[3].id

        i11 = Instrument(name = "Flaute", image="https://www.sanganxa.com/30274-large_default/flauta-yamaha-yfl-262-serie-estudio.jpg", image_2="https://www.sanganxa.com/38144-large_default/flauta-yamaha-yfl-262-serie-estudio.jpg")
        i11.category_id = categories[2].id
        i11.supplier_id = suppliers[3].id

        i12 = Instrument(name = "Eufonio ", image="https://www.sanganxa.com/23701-large_default/bombardino-sib-eastman-eep323-lacado.jpg", image_2="https://www.sanganxa.com/33432-large_default/bombardino-sib-eastman-eep323-lacado.jpg")
        i12.category_id = categories[2].id
        i12.supplier_id = suppliers[3].id

        i13 = Instrument(name = "Drums ", image="https://www.sanganxa.com/42589-large_default/bateria-mapex-tornado-tnm5844ftcuyb.jpg", image_2="https://www.sanganxa.com/31705-large_default/set-paiste-universal-pst3-14quot-16quot-20quot.jpg")
        i13.category_id = categories[2].id
        i13.supplier_id = suppliers[3].id

        i14 = Instrument(name = "Snare Drum ", image="https://www.sanganxa.com/32149-large_default/caja-db-14quotx55quot-10-div-db0076-cromada.jpg", image_2="https://www.sanganxa.com/2544-large_default/caja-db-14quotx55quot-10-div-db0076-cromada.jpg")
        i14.category_id = categories[2].id
        i14.supplier_id = suppliers[3].id

        i15 = Instrument(name = "Cymbal ", image="https://www.sanganxa.com/42165-large_default/juego-platos-paiste-alpha-18-concert-par.jpg", image_2="https://www.sanganxa.com/31447-large_default/funda-platos-ortola-60-cm.jpg")
        i15.category_id = categories[2].id
        i15.supplier_id = suppliers[3].id

        i16 = Instrument(name = "Bass Drum ", image="https://www.sanganxa.com/36739-large_default/bombo-santafe-banda-stf2560-22-55x28-cm.jpg", image_2="https://www.sanganxa.com/29520-large_default/funda-bombo-ortola-5523-66-x-30-cm.jpg")
        i16.category_id = categories[2].id
        i16.supplier_id = suppliers[3].id

        i17 = Instrument(name = "Timpani", image="https://www.sanganxa.com/32935-large_default/timbal-majestic-cof-2600-fibra-26quot.jpg", image_2="https://www.sanganxa.com/32823-large_default/timbal-majestic-cof-2900-fibra-29quot.jpg")
        i17.category_id = categories[2].id
        i17.supplier_id = suppliers[3].id

        i18 = Instrument(name = "Xylophone ", image="https://www.sanganxa.com/7143-large_default/xilofono-santafe-stf-5001.jpg", image_2="https://www.sanganxa.com/7144-large_default/xilofono-santafe-stf-5001.jpg")
        i18.category_id = categories[2].id
        i18.supplier_id = suppliers[3].id


        db.session.add_all([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18])
        db.session.commit()

if __name__ == '__main__':
    drop_tables()
    add_data_tables()