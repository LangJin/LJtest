from flask import request,url_for,send_from_directory,session
from . import userbp
from werkzeug import secure_filename
import os
from config import upload_folder
import random,string
from ..utils.othertools import setcors



@userbp.route("/upload",methods=["post"])
def fileupload():
    '''
    上传图片接口，支持'png', 'jpg', 'jpeg', 'gif'格式。
    '''
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        file = request.files["file"]
        if file and ('.' in file.filename and \
            file.filename.rsplit('.', 1)[1] in set(['png', 'jpg', 'jpeg', 'gif'])):
            filename = secure_filename(file.filename)
            fname = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
            filename = fname+"."+filename.split(".")[1]
            uploadhost = os.path.join(os.getcwd()+upload_folder, filename)
            file.save(uploadhost)
            # file_url = url_for("static",filename='images/uploads/'+filename)
            return setcors(data=filename,status=200)
        else:
            return setcors(msg="请上传正确的图片。")
    else:
        return setcors(msg=loginstatus)


@userbp.route('/imgs')
def uploaded_file():
    '''
    读取图片接口
    '''
    imgname = request.args.get("imgname")
    return send_from_directory(os.getcwd()+upload_folder,imgname)