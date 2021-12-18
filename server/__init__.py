from flask import Flask, Response
from kazoo.client import KazooClient, KazooState


app = Flask(__name__)
zk = KazooClient()



@app.route("/Health")
def health_check():
    return Response(status=200)



def create_app(env):
    #Intialize modules
    if env == "prod":
        zk.set_hosts('zookeeper.default.svc.cluster.local:2181')
        app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    elif env == "dev":
        zk.set_hosts('host.docker.internal:2181')
        app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    else:
        return None
    zk.start()
    from server.api.routes import notify
    app.register_blueprint(notify, url_prefix="/notification/v1")
    return app


