# Flask-Currency
Currency handling extension for Flask.

## Usage
###Initialization
Initialize extension by providing Flask and Flask-SQLAlchemy instance.
```python
from flask import Flask
from flask_currency import Currency
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app) 
currency = Currency(app, db)


if __name__ == '__main__':
    app.run()
```
Optionally, an extended currency model can be provided 
(for translation support, etc.). If the model is not extended, it can be 
accessed through the `Currency.model` attribute.

 ### Money class
 A money class is defined, which uses the Currency model for value calculation 
 and formatting.
 ```python
>>> from flask_currency import Money
>>> price = Money(100, 'USD')
>>> print(price)
'$100.00'

>>> in_eur = price.convert_to('EUR')
>>> print(in_eur)
'90.71 €'
```

### Currencies
The currencies table must be maintained, currency data must be added manually.
```python
eur = currency.model(
    name='Euro',
    code='EUR',
    sign='€',
    value=1,
    format_str='{:,.2f} €'
)
db.session.add(eur)
db.session.commit()
```