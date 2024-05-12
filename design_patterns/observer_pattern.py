"""
Observer Pattern (Behavioral)
Purpose: Allows an object to notify other objects (observers) about changes in its state.
How It Works: The Observer pattern is a publish-subscribe model where the subject maintains a list of observers and notifies them in case of state changes. This pattern is crucial for implementing distributed event handling systems.
Use Case: Used in implementing event handling systems, data broadcasting, or implementing real-time data feeds like stock market updates.
"""

class NewsPublisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def add_news(self, news):
        self._latest_news = news
        self.notify_subscribers()

    def get_news(self):
        return self._latest_news


class Subscriber:
    def update(self):
        # Get the latest news from the publisher
        pass


# Usage
publisher = NewsPublisher()
subscriber1 = Subscriber()
publisher.attach(subscriber1)
publisher.add_news("Breaking News: Python 4.0 Released!")


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class AmericanStockMarket(Observer):
    def update(self, subject):
        print("American stock market received: {0}".format(subject))

class EuropeanStockMarket(Observer):
    def update(self, subject):
        print("European stock market received: {0}".format(subject))

if __name__ == '__main__':
    ibm = Subject()
    asm = AmericanStockMarket()

    ibm.attach(asm)
    esm = EuropeanStockMarket()

    ibm.attach(esm)
    ibm.notify()