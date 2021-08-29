from app.admin import bp_admin
from flask_cors import cross_origin
from app import MODULES, csrf


@bp_admin.route('/modules', methods=['GET'])
@cross_origin
@csrf.exempt
def get_modules():
    response = {
        "modules": [module.to_dict() for module in MODULES]
    }