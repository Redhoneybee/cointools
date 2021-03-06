# Cointools 
![Generic badge](https://img.shields.io/badge/version-1.0.4-green.svg)


- pypi : https://pypi.org/project/cointools/

1. Install
```
-> pip install cointools

```


2. import

```
from cointools.manager import MultipleManager
from cointools.service import BaseServiceHandler
```

3. example
## 1) class MultipleManager
```
class MyManager(MultipleManager) : 
    def connect(self) : 
        pass 

    def get_ticker(self) : 
        pass

    def finish(self, ticker) :
        pass

    def verify_to_service(self) :
        pass

    def verify_to_ticker(self) : 
        pass

    
```

#### connect(self) -> None
you can connect to the "self._conn" variable through the Bitcoin exchange api you want.

* exmaple(connect) 
```
    ...
    # self._key : tuple

    def coonnect(self) : 
        self._conn = pyupbit.Upbit(self._key[0], self._key[1])
```

#### setter(self) -> str
This function is a custom input function to obtain the desired ticker.

# " you can make the black list about using ticker. "

* example(setter)
```
    ...
    def setter(self) : 
        return input("Which ticker do you want ?: ")

```

#### finish(self, ticker) -> None
This is a function that works after end the thread.

# " you can remove ticker in black list. "

* example(finish)
```
    ...
    def finish(self, ticker) : 
        pass

```

#### verify_to_service(self) -> bool 
it is used for functions that require confirmation before service start.


* example(verify_to_service)
```
    ...
    def verify_to_service(self) : 
        return True

```

#### verify_to_ticker(self) -> bool
it is used to check the ticker after receiving the ticker.

* example(verify_to_ticker)
```
    ...
    def verify_to_service(self) : 
        return True

```



## 2) class BaseServiceHandler
```
...
class MyService(BaseServiceHandler) : 
    def setup(self) : 
        pass 
    
    def action(self) : 
        pass
    
    def finish(self) : 
        pass
```

* value
 - _conn : it's connection of bitcoin exchange API.
 - _ticker : it's ticker in the thread.



#### setup(self) -> None 
This is a function that sets up before the action is executed.

```
    ...
    def setup(self) : 
        self._price = None
```
#### action(self) -> None
This function monitor and action about ticker.

# " you use to principle of investment. "

example(full) 
```
from cointools.manager import MultipleManager
from cointools.service import BaseServiceHandler

KEY = ("test key", "test secret)
class MyManager(MultipleManager) : 
    def connect(self) : 
        self._conn = pyupbit.Upbit(self._key[0], self._key[1])
    
class MyService(BaseServiceHandler) : 
    def action(self) : 
        print(f"{self._ticker} hello!")

    def finish(self) : 
        print(f"{self._ticker} goob bye~")

with MyManager(KEY, MyService) as manager :
    manager.connect()
    manager.start()
```

