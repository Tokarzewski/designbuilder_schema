from designbuilder_schema.utils import load_model, save_model

filepath = r".\samples\models\Shoebox10x10.xml"
model = load_model(filepath)
save_model(model, r".\samples\models\Shoebox10x10_resaved.xml")
