from flask import Blueprint
from flask import Blueprint, request, redirect, url_for, jsonify
from PIL import Image, ImageFilter, ImageEnhance
from helpers import get_secure_filename_filepath


bp = Blueprint('filters', __name__, url_prefix='/filters')

@bp.route('/blur', methods=['POST']) 
def blur():
    filename = request.json['filename'] #type:ignore
    filename, filepath = get_secure_filename_filepath(filename)

    try:
        radius = int(request.json['radius']) #type:ignore
        image = Image.open(filepath)
        out = image.filter(ImageFilter.GaussianBlur(radius))
        out.save(filepath)
        return redirect(url_for('download_file', name=filename))

    except FileNotFoundError:
        return jsonify({"message": "File not found."}), 404




@bp.route('/blur', methods=['POST']) #type:ignore
def contrast():
    filename = request.json['filename'] #type:ignore
    filename, filepath = get_secure_filename_filepath(filename)

    try:
        factor = float(request.json['factor']) #type:ignore
        image = Image.open(filepath)
        out = ImageEnhance.Contrast(image).enhance(factor)
        out.save(filepath)
        return redirect(url_for('download_file', name=filename))

    except FileNotFoundError:
        return jsonify({"message": "File not found."}), 404

@bp.route('/brightness', methods=['POST']) #type:ignore
def brightness():
    filename = request.json['filename'] #type:ignore
    filename, filepath = get_secure_filename_filepath(filename)

    try:
        factor = float(request.json['factor']) #type:ignore
        image = Image.open(filepath)
        out = ImageEnhance.Brightness(image).enhance(factor)
        out.save(filepath)
        return redirect(url_for('download_file', name=filename))

    except FileNotFoundError:
        return jsonify({"message": "File not found."}), 404