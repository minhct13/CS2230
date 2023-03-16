from flask import Blueprint, make_response, request, jsonify

from app.services import model
from app.services.classify import classify

classify_bp = Blueprint('classify_bp', __name__)

@classify_bp.route('/classify',methods=['POST'])
def classify_sent():
    """
    Take input as base64 image -> response matched images in db
    """
    sent = request.json.get("sent", "")
    res, status_code = classify(
                            model=model,
                            sent=sent)
    return make_response(
         jsonify({"message": res}),
         status_code
    )
