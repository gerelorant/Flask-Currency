from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_currency.model import CurrencyMixin


class Currency(object):
    """Flask-Currency extension class.

    :param app (Flask): Flask instance
    :param db (SQLAlchemy): Flask-SQLAlchemy instance
    :param currency_class: Currency model class. (optional)
    """
    def __init__(
            self,
            app: Flask,
            db: SQLAlchemy,
            currency_class: type(CurrencyMixin) = None
    ):
        self.app = app
        self.db = db
        self.model = currency_class
        self.init_app(app)

    def init_app(self, app: Flask):
        """Initialize extension with Flask app.

        :param app: Flask application instance
        """
        app.extensions["currency"] = self

        if self.model is None:
            class Currency(self.db.Model, CurrencyMixin):
                pass

            self.model = Currency
