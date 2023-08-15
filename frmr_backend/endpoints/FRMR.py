from frmr_backend.utils.config import socketio
from frmr_backend.utils.FRMR_helpers import getResponseAPI, getRequestParams, getSpecification
from frmr_backend.utils.config import BaseURLfrmr
from flask import render_template, Blueprint
import uuid

bp = Blueprint('frmr', __name__)


@bp.route('/ws/frmr')
def main():
    random_uuid = uuid.uuid4()

    @socketio.on('connect', namespace=f'/frmr/{random_uuid}')
    def user_connect():
        socketio.emit('socket', namespace=f'/frmr/{random_uuid}')

    @socketio.on('disconnect', namespace=f'/frmr/{random_uuid}')
    def user_disconnect():
        socketio.emit('socket', namespace=f'/frmr/{random_uuid}')

    @socketio.on('payload', namespace=f'/frmr/{random_uuid}')
    def payloadEvent(payload):
        responseAPI = getResponseAPI(payload)

        requestParams = '&'.join(
            [f'{key}={payload[key]}' for key in payload if key != 'endpoint' and payload[key] is not None]
        )
        requestURL = f"{BaseURLfrmr}{payload['endpoint']}?{requestParams}"
        data = [responseAPI.json(), requestURL, payload['endpoint'], responseAPI.status_code]
        socketio.emit('payload', data=data, namespace=f'/frmr/{random_uuid}')

    rp = getRequestParams()
    specification = getSpecification()
    return render_template(
        'index.html', rp=rp, specification=specification, registery='FRMR', namespace=f'/frmr/{random_uuid}'
    )
