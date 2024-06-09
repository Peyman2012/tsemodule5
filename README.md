### tsemodule7
#### code by t.me/python4finance
#### Please visit [python4finance.ir](http://www.python4finance.ir/) 
#### you can contact me via @sadiqkarimi in Telegram application
### Project folder structure

tsemodel7/
│
├── tsemodel7/
│   ├── __init__.py
│   ├── stock_manager.py
│   └── index_manager.py
│
├── setup.py
└── README.md

1. __init__.py file
This file allows your library to export the StockManager and IndexManager modules.

from .stock_manager import StockManager
from .index_manager import IndexManager


