from flask_sqlalchemy import Model
import sqlalchemy as sa


class CurrencyMixin(Model):
    """Declarative mixin class for currency model."""
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(32))
    code = sa.Column(sa.String(3), unique=True, nullable=False)
    sign = sa.Column(sa.String(4), nullable=False)
    value = sa.Column(sa.Float, nullable=False)
    format_str = sa.Column(sa.String(32))

    @classmethod
    def set_default(cls, currency_code: str):
        """Set currency as base currency with value of 1.

        :param currency_code: Code of base currency
        """
        currency = cls.query.filter_by(code=currency_code).first()
        if currency is None:
            raise ValueError(f'Currency not found: {currency_code}')

        value = currency.value
        for c in cls.query.all():
            c.value /= value

    def set_as_default(self):
        """Set currency as base currency with value of 1."""
        type(self).set_default(self.code)

    def format(self, amount: float):
        """Return formatted string.

        :param amount: Amount of currency.
        :return: Formatted string.
        """
        return self.format_str.format(amount)
