import requests , json , os

def stock_portfolio_system():
    filename = "portfolio.json"

    def load_file(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            with open(filename + ".backup", 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Loaded data from {filename}")
            return data
        except FileNotFoundError:
            print("Portfolio not found, Starting fresh!")
            return {}
        except json.JSONDecodeError:
            print(f"Corruption of your {filename} file")
            backup = filename + ".corrupted"
            print(f"Saving corrupted file as {backup}")     #takes data corrupted data and stores it as backup 

            try:
                os.rename(filename, backup)                 #backup created 
            except:
                pass                                        #If it already exists just continue
            print("Starting with empty grade book.")
            return {}                                       #creates new file to add data to
        
        except PermissionError:
            print(f"ERROR: Don't have permission to read {filename}!")
            print("Try running as administrator or check file permissions.")
            print("Starting with empty portfolio.")
            return {} 

        except Exception as e:
            print(f"ERROR: Unexpected error loading {filename}")
            print(f"Details: {e}")
            print("Starting with empty grade book.")
            return {}

        
    def save_to_file(stock_portfolio, filename):
        try:
            
            if os.path.exists(filename):                            # Create backup of existing file BEFORE overwriting
                with open(filename, 'r') as f:
                    old_data = f.read()
                with open(filename + ".backup", 'w') as f:
                    f.write(old_data)
            
            with open(filename, 'w') as f:                          # Now save new data
                json.dump(stock_portfolio, f, indent=4)
            
            print(f"Data saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Save failed: {e}")
            return False
        
    
    stock_portfolio = load_file(filename) 


    portfolio = {}

    def add_stock(portfolio, stock_ticker, shares, buy_price):
        if stock_ticker not in portfolio:
            portfolio[stock_ticker] = {     #initialises the stocks shares and buy price
                "shares" : 0,
                "buy_price" : 0
            }
            #Will update the current share and buy price of the stock 
        portfolio[stock_ticker]["shares"] += shares     #adds to the current shares 
        total_cost = portfolio[stock_ticker]["buy_price"]* portfolio[stock_ticker]["shares"]        # finds the average buy_price when shares are bought 
        total_cost += buy_price * shares        # adds to the total cost if more shares are purchased
        portfolio[stock_ticker]["buy_price"] = total_cost / portfolio[stock_ticker]["shares"]
        print(f"Added {shares} of {stock_ticker} with a cost of {buy_price:.2f}")
        print(f"Average cost £{portfolio[stock_ticker]['buy_price']:.2f}")
        print("=========================================")


    def view_portfolio(portfolio):
        if not portfolio: 
            print("No stocks added yet!")
            return
        
        print("\nYour Portfolio:")
        print("===============")
        for stock_ticker, data in portfolio.items():
            shares = data["shares"]    
            buy_price = data["buy_price"]
            print(f"{stock_ticker}  | {buy_price}  | {shares} ")


   # def trending_stock(api):
   # def portfolio_analysis(portfolio, stock_ticker, shares, buy_price):
   # def remove_stock(portfolio, stock_ticker)

    while True:
        print("=========================================")
        print("Stock portfolio Tracker!")
        print("=========================================")
        print("1. Add stock")
        print("2. View portfolio")
        print("3. Trending this week")
        print("4. Portfolio Analysis")
        print("5. Remove Stock")
        print("6. Save & Exit")
        try:
            choice = int(input("Please input correlating number of where you would like to go: "))
            print("=====================================================")
        except ValueError:
            print("Please input the correlating number")
            print("=====================================================")
            continue 

        if choice == 1:
            stock_ticker = input("Please enter the stock ticker: ").upper()
            if not stock_ticker.strip():
                print("Ticker cannot be empty!")
                print("=====================================================")
                continue

            if not all(c.isalpha() for c in stock_ticker):
                print("Ticker should only contain letters!")
                print("=====================================================")
                continue

            try:
                shares = float(input("Number of shares: "))
                if shares <= 0:
                    print("Shares must be greater than 0!")
                    print("=====================================================")
                    continue

                buy_price = float(input("Price you bought at: £"))
                if buy_price <= 0:
                    print("Price must be greater than 0!")
                    print("=====================================================")
                    continue

            except ValueError:
                print("Please enter a valid number!")
                print("=====================================================")
                continue

            add_stock(stock_portfolio, stock_ticker, shares, buy_price)

        elif choice == 2:
            view_portfolio(stock_portfolio)
            continue         

        elif choice == 6:
            confirm = input("Are you sure you would like to save and exit? (y/n): ")
            if confirm.lower() == "y":
                save_to_file(stock_portfolio, filename)
                print("See you later!")
                break
            else:
                print("Continue...")
stock_portfolio_system()


""""
        elif choice == 3:
             continue 
        elif choice == 4:
             continue 
        elif choice == 6:
            continue
    
        """

