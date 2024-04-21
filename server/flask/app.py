from .server import create_app


def run_app():
    app = create_app()
    app.run()