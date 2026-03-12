import os
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS


def allowed_file(filename):

    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def save_uploaded_files(files, upload_folder):

    saved_files = []

    for file in files:

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            filepath = os.path.join(upload_folder, filename)

            file.save(filepath)

            saved_files.append(filepath)

    return saved_files