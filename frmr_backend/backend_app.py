from frmr_backend.utils.config import app, socketio
from frmr_backend.endpoints import FRMR

app.register_blueprint(FRMR.bp)

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True, port=8001)
