from flask import render_template
# from flask import Flask, render_template, request, redirect, url_for, flash, abort, send_file
# from werkzeug.utils import secure_filename
# import logging
# from logging import Formatter, FileHandler
# import os
# from jinja2 import exceptions
# # from covid_visualizer import data_visualizer
# from helper import *

from project.app import app, pages


@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)


@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


# # Home Page
# @app.route('/')
# def home():
#     return render_template('pages/placeholder.home.html')
#
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
#
#
# # Upload File.
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if 'configfile' not in request.files:
#             flash('No file part')
#             configfilename = ''
#         else:
#             configfile = request.files['configfile']
#
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if 'configfile' not in request.files or configfile.filename == '':
#             flash('No selected file')
#             configfilename = 'None'
#
#         # Save the Data file path
#         if file and allowed_file(file.filename):
#             app.logger.info('File Saved')
#             filename = secure_filename(file.filename)
#             datapath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(datapath)
#
#         # Save the Configuration file path
#         if 'configfile' in request.files and configfile.filename != 'None' and allowed_file(configfile.filename):
#             app.logger.info('Configuration File Saved')
#             configfilename = secure_filename(configfile.filename)
#             configdatapath = os.path.join(app.config['UPLOAD_FOLDER'], configfilename)
#             configfile.save(configdatapath)
#         elif configfilename == 'None':
#             configdatapath = 'None'
#             # Saving File Contents in DB
#             # save_in_db(datapath)
#         all_filenames = datapath + '&' + configdatapath
#         return redirect(url_for('reconstruct', allfilename=all_filenames))
#     return render_template('pages/placeholder.upload.html')
#
#
# # Read and visualize the data from csv
# @app.route('/reconstruct', methods=['GET'])
# def reconstruct():
#     try:
#         URL = request.url
#         Segments = URL.split('=')
#         imagefile = Segments[1].split('%26')[0].replace('//', '/').replace('%3A', ':').replace('%2F', '/').replace('%5C',
#                                                                                                                   '/')
#         xmlfile = Segments[1].split('%26')[1].replace('//', '/').replace('%3A', ':').replace('%2F', '/').replace(
#             '%5C', '/')
#
#         # bar_class = image_read(imagefile, xmlfile)
#         # if(bar_class=='other'):
#         #     return render_template('pages/placeholder.reupload.html')
#         bar_class ='bar'
#         return render_template('pages/placeholder.output.html',bar_type = bar_class, url = URL)
#     except exceptions.TemplateNotFound:
#         abort(404)
#
# @app.route('/download', methods=['GET'])
# def download_file():
#     data = 'static/data/data.csv'
#     return send_file(data,as_attachment=True)
#
# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404
#
#
# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')
#
# # Launch.
# if __name__ == '__main__':
#     app.run(host="", debug=True)
