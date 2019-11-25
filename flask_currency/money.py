import typing

from flask import current_app
from werkzeug.local import LocalProxy

from flask_currency.model import CurrencyMixin

curr = LocalProxy(lambda: current_app.extensions["currency"])


class Money:
    def __init__(
            self,
            amount: float,
            currency: typing.Union[str, CurrencyMixin]
    ):
        self._amount = float(amount)
        if isinstance(currency, CurrencyMixin):
            self._currency = currency
        else:
            self._currency = curr.model.query\
                .filter_by(code=currency).first()

        if self._currency is None:
            raise ValueError("No currency found with code {}".format(currency))

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: float):
        self._amount = float(value)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, CurrencyMixin):
            currency = value
        else:
            currency = curr.model.query\
                .filter_by(code=value).first()

        self.amount = self.value_in(currency)
        self._currency = currency

    def convert_to(self, currency):
        money = Money(self.amount, self.currency)
        money.currency = currency
        return money

    def value_in(self, currency):
        if not isinstance(currency, CurrencyMixin):
            currency = curr.model.query\
                .filter_by(code=currency).first()

        value = self.amount *  self._currency.value / currency.value

        return round(value, currency.decimals)

    @property
    def formatted(self):
        return self.currency.format(self.amount)

    def __repr__(self):
        return self.formatted

    def __str__(self):
        return self.formatted

    def __html__(self):
        return self.formatted
