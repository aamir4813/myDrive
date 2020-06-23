from mydrive.webApp import app , db
from flask import render_template , request , flash , redirect , url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mydrive.models.user_model import Users
from mydrive.models.files_model import Files

from flask_login import current_user , login_required

import os

app.config["ALLOWED_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF" ,"ZIP" , "ISO"]


@app.route("/upload" , methods=["POST" , "GET"])
@login_required
def upload():
    print("yes")
    user_id = current_user.id

    if request.files:

        tempFile = request.files['file']
        fileName = tempFile.filename

        if fileName is "":
            print("No filename")
            return  redirect(url_for('display_all'))

        fileExtension = fileName.rsplit(".", 1)[1]
        if allowed_file(fileName , fileExtension ):

            filePath = os.path.join(os.getcwd() + "/Storage" , fileName )
            tempFile.save(os.path.join(app.config["UPLOAD_FOLDER"], fileName))
            file_object = Files(user_id = user_id ,  fileName = fileName , filePath = filePath , fileExtension = fileExtension)
            
            db.session.add(file_object)
            db.session.commit()

            print("File Saved !!")
            return redirect(url_for('display_all'))
    
    return redirect(url_for('profile'))


def allowed_file(filename , ext):

    if not "." in filename:
        return False

    # ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False