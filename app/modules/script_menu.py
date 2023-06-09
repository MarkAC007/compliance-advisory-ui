# Replace 'module_name' with the respective module name (e.g., 'references', 'iframes', etc.)
from flask import Blueprint, render_template

module_name = Blueprint('module_name', __name__)

@module_name.route('/module_name')
def show_module_name():
    return render_template('module_name.html')