import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_(self, code, units):
        if code in self.portfolio:
            self.portfolio[code]['units'] += units
        else:
            self.portfolio[code] = {'units': units, 'average_price': self.current_price(code)}

    def remove_(self, code, units):
        if code in self.portfolio:
            if units >= self.portfolio[code]['units']:
                del self.portfolio[code]
            else:
                self.portfolio[code]['units'] -= units

    def current_price(self, code):
        stock = yf.Ticker(code)  # Corrected assignment of yf.Ticker
        return stock.history(period='1d')['Close'].iloc[-1]

    def track_performance(self):
        total_amount = 0
        current_value = 0

        for ticker, data in self.portfolio.items():
            avg = data['average_price']
            units = data['units']
            current = self.current_price(ticker)
            total_amount += avg * units
            current_value += current * units
            print(f"{ticker}: {units} shares, Average Price: ${avg:.2f}, Current Price: ${current:.2f}")

        print(f"\nTotal Investment: ${total_amount:.2f}")
        print(f"Current Portfolio Value: ${current_value:.2f}")
        print(f"Profit/Loss: ${current_value - total_amount:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        action = input("Choose an action (add, remove, track, exit): ").lower()
        if action == "add":
            code = input("Enter stock Name: ").upper()
            units = int(input("Enter number of shares to add: "))
            portfolio.add_(code, units)
        elif action == 'remove':
            code = input("Enter stock code: ").upper()
            units = int(input("Enter number of shares to remove: "))
            portfolio.remove_(code, units)
        elif action == "track":
            portfolio.track_performance()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
