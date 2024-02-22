# BankNiftyDBMonitor
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)


BankNiftyDBMonitor is a web application built with Flask to monitor live and historical data of Bank Nifty. It fetches live Bank Nifty values from Yahoo Finance and stores them in a SQLite database. Users can view the live Bank Nifty value on the main page and historical Bank Nifty data on a separate page.


https://github.com/HacktiveMindset/BankNiftyDBMonitor/assets/141541920/816a9bde-fe19-473b-b33c-6013e42dee5a


## Features

- **Live Bank Nifty Value**: Displays the live Bank Nifty value on the main page, updating every 5 seconds.
- **Historical Bank Nifty Data**: Provides a separate page to view historical Bank Nifty data stored in the database.
- **Automatic Data Updates**: Automatically updates Bank Nifty data every 5 seconds without user interaction.

## Installation

### Clone the Repository

```bash
git clone https://github.com/HacktiveMindset/BankNiftyDBMonitor.git
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the Flask application:
``` 
python app.py
```

Access the application in your web browser at http://127.0.0.1:5000.

The main page (/) will display the live Bank Nifty value, updating every 5 seconds.

To view historical Bank Nifty data, navigate to /history.

## Contributing
Contributions are welcome! Please feel free to fork the repository, make pull requests, or open issues for any bugs or feature requests.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/HacktiveMindset/BankNiftyDBMonitor/blob/main/LICENSE) file for details.

## Acknowledgments


Special thanks to [Piyushhacker (Piyush Mujmule)](https://github.com/HacktiveMindset) for initiating and maintaining this project.

## Contact

For inquiries or feedback, please contact

[![INSTAGRAM](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/piyush.mujmule)
