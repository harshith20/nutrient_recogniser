from flask import Flask, render_template, request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath,abspath
import requests
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image  import load_img,img_to_array
from tensorflow.keras.models import load_model
from  tensorflow.python.keras.utils import np_utils 


app = Flask(__name__)
#model = pickle.load(open('', 'rb'))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'static/uploads/'
image_path=''
class_names=['Apple Braeburn', 'Apple Crimson Snow', 'Apple Golden 1', 'Apple Golden 2', 'Apple Golden 3', 'Apple Granny Smith', 'Apple Pink Lady', 'Apple Red 1', 'Apple Red 2', 'Apple Red 3', 'Apple Red Delicious', 'Apple Red Yellow 1', 'Apple Red Yellow 2', 'Apricot', 'Avocado', 'Avocado ripe', 'Banana', 'Banana Lady Finger', 'Banana Red', 'Beetroot', 'Blueberry', 'Cactus fruit', 'Cantaloupe 1', 'Cantaloupe 2', 'Carambula', 'Cauliflower', 'Cherry 1', 'Cherry 2', 'Cherry Rainier', 'Cherry Wax Black', 'Cherry Wax Red', 'Cherry Wax Yellow', 'Chestnut', 'Clementine', 'Cocos', 'Corn', 'Corn Husk', 'Cucumber Ripe', 'Cucumber Ripe 2', 'Dates', 'Eggplant', 'Fig', 'Ginger Root', 'Granadilla', 'Grape Blue', 'Grape Pink', 'Grape White', 'Grape White 2', 'Grape White 3', 'Grape White 4', 'Grapefruit Pink', 'Grapefruit White', 'Guava', 'Hazelnut', 'Huckleberry', 'Kaki', 'Kiwi', 'Kohlrabi', 'Kumquats', 'Lemon', 'Lemon Meyer', 'Limes', 'Lychee', 'Mandarine', 'Mango', 'Mango Red', 'Mangostan', 'Maracuja', 'Melon Piel de Sapo', 'Mulberry', 'Nectarine', 'Nectarine Flat', 'Nut Forest', 'Nut Pecan', 'Onion Red', 'Onion Red Peeled', 'Onion White', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Peach 2', 'Peach Flat', 'Pear', 'Pear 2', 'Pear Abate', 'Pear Forelle', 'Pear Kaiser', 'Pear Monster', 'Pear Red', 'Pear Stone', 'Pear Williams', 'Pepino', 'Pepper Green', 'Pepper Orange', 'Pepper Red', 'Pepper Yellow', 'Physalis', 'Physalis with Husk', 'Pineapple', 'Pineapple Mini', 'Pitahaya Red', 'Plum', 'Plum 2', 'Plum 3', 'Pomegranate', 'Pomelo Sweetie', 'Potato Red', 'Potato Red Washed', 'Potato Sweet', 'Potato White', 'Quince', 'Rambutan', 'Raspberry', 'Redcurrant', 'Salak', 'Strawberry', 'Strawberry Wedge', 'Tamarillo', 'Tangelo', 'Tomato 1', 'Tomato 2', 'Tomato 3', 'Tomato 4', 'Tomato Cherry Red', 'Tomato Heart', 'Tomato Maroon', 'Tomato Yellow', 'Tomato not Ripened', 'Walnut', 'Watermelon']

import os, shutil
folder = os.path.join(basedir,UPLOAD_FOLDER)
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/',methods=['GET'])
def Home():
    return render_template('upload.html')
@app.route("/predict", methods=['POST'])
def predict(): 
 file =  request.files['file']	
 if file.filename == '':
    flash('No file selected for uploading')
    return redirect(request.url)
 if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(basedir,UPLOAD_FOLDER,filename))	 	

 image_path=os.path.join(basedir,UPLOAD_FOLDER, filename)
 im = load_img( image_path, target_size=(128, 128,3))
 img_array = img_to_array(im)
 img_array = tf.expand_dims(img_array, 0)
 model = load_model(os.path.join(basedir,'my_model.h5'))
 predictions=model.predict(img_array)
 score = tf.nn.softmax(predictions[0])
 s=class_names[np.argmax(score)]
 
 return render_template('upload.html',prediction_text="it is a {}".format(s),filename=filename,class_name=s.lower())
@app.route('/nutrien/<class_name>')
def nutrient(class_name):
        #print('display_image filename: ' + filename)
        s=str(class_name)
        a=s.split()
        class_name=a[0]+' nutrition  facts'
        class_name=class_name.lower()
        s=class_name+'/'
        k='photos/'
        class_name=os.listdir(os.path.join(basedir,'static',k,class_name))
        
        return redirect(url_for('static', filename='photos/' + s+class_name[0]), code=302)   

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


if os.path.isfile(image_path):
 os.remove(image_path)
 print('hi bro')

if __name__ == "__main__":
    app.run(debug=True)


