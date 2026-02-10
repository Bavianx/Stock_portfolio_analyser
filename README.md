# Stock_portfolio_analyser
A command-line stock portfolio management system built in Python. Track your investments, monitor your positions, and make data-driven decisions with real-time market data.

Features

Add stocks to your portfolio with share count and purchase price
Average cost calculation - automatically calculates your average buy price when adding to existing positions
View portfolio - display all holdings with shares and average buy price
Persistent storage - portfolio saves to JSON file between sessions
Automatic backup system - creates backups before every save
Corrupted file handling - safely recovers from damaged portfolio files
Input validation - ensures all data entered is valid
Coming soon:

 -Trending stocks this week (live API data)
 -Portfolio analysis with trim/hold/add recommendations
 -Remove stock from portfolio


Technologies Used

Python 3
requests - API calls for real-time market data
json - data persistence and storage
os - file system operations and backup management

Roadmap

 Real-time prices via API integration
 Trending stocks - top movers of the week
 Portfolio analysis - trim/hold/add recommendations based on position weighting and P&L
 P&L tracking - profit and loss per position
 Portfolio value - total current value of all holdings
 Remove stock functionality
 Price alerts - notify when stock hits target price
