from config import create_app
from dynaconf import settings

application, es = create_app.create_app(
    debug=settings.DEBUG, testing=settings.TESTING
)
