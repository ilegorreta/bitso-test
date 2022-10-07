# Bitso Sr. Data Engineer test

This repository is composed of two challenges:

The first one consisted in tracking and monitoring the activity from all the exchanges that offer the same markets as Bitso. The following two tables (with their corresponding schemas) were created during the process:

  - **similar_exchanges.csv**:
    - ('exchange_id': string, 'exchange_name': string, 'trust_score': int, 'trust_score_rank': int)
  - **markets.csv**:
    - ('exchange_id': string, 'base': string, 'target':string)

The data was obtained through an API called [CoinGecko](https://www.coingecko.com/) which is an independent cryptocurrency data aggregator offering Bitcoin and cryptocurrency data, real time prices, charts, market cap, portfolio, widgets, news and alerts. 

The following list comprises the endpoints used during the extraction:
  - get_coin_ticker_by_id
  - get_exchanges_tickers_by_id
  - cg.get_exchanges_list

The scheduled_frequency for this application was set on a daily basis.

The output for the first challenge is under ```data/test_1/markets.csv``` and ```data/test_1/similar_exchanges.csv```, respectively

The second application is about monitoring and alerting whenever the [bid-ask spread](https://www.investopedia.com/articles/investing/082213/how-calculate-bidask-spread.asp) from the “order books” in the books BTC_MXN and USD_MXN is bigger than 0.1% in Bitso. The implementation for this requirement was a dev data-lake living in the container where every hour the [Bitso API](https://bitso.com/api_info%23introductionis) is called, the bid-ask spread is calculated, determined if it is above a well-defined threshold (0.1%) and saved the information in a partition fashion based on the exchange, market, day and hour. A second job was triggered right after the creation of the previous file and prints how many times the spread was above the threshold.
The scheduled_frequency for these jobs was set to run once an hour.

The output for the second challenge are the files generated under the lake (```data/{market}/{year}-{month}-{day}/hour/files.csv```) simulating the directory structure partitions in S3.  

Both application were developed using Python 3.8, Pandas 1.5.0 and pycoingecko 3.0.0 ([CoinGecko API wrapper](https://www.coingecko.com/)).

The whole project was developed through GitHub Actions, which is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate the development, testing, and deployment of the application throughout its lifecyle. This way we can deploy our application using GitHub's servers based on a version control system. In  this project, GitHub Actions is the scheduler of each pipeline and where the actual processing is going to take place. 

Each time any of the workflows runs, we are commiting and pushing the changes into the main branch of the repository, so we could keep track of the updated versions of the tables (app 1) and to be adding new partitions into the datalake (app 2). 

It is worth mentioning that since this is a development project, I am deliberately commiting the ```.env``` file containing the corresponding environment variables into the repo, for the sake of reproducibility. In a real prod environment this should be part of the ```.gitignore``` file and could take advantage of [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets).
The credentials for the GitHub account, as well as the Bitso API endpoints were encrypted using GitHub Secrets.

---
## Requirements
* [Docker](https://docs.docker.com/get-docker/)

Note: Since we are using Docker, it is not necessary to install the rest of the Python modules, libraries and dependencies individually using [pip](https://pypi.org/project/pip/), [Conda](https://docs.conda.io/en/latest/) or [Brew](https://brew.sh/).

---
## How to execute the project
As said before, the project is going to be automatically running at a given scheduled frequency, although it is possible to execute manually each one of the scripts.

I developed this project making use of [VSCode DevContainers](https://code.visualstudio.com/docs/remote/containers), based on the Dockerfile provided in the repository. It is also posible to manually create a Docker image based on this Dockerfile and to enter a container using that image (that's basically what VSCode DevContainers is doing under the hood).

To manually run the first challenge we need to run the following script: ```src/test_1.py```.
For the second challenge, ```test_2.py``` is the script which retrieves data from Bitso API and stores the partition in the lake, whereas ```test_2_spread_validation.py``` is the spread validator file.

---
## Directory Tree Structure
It is noteworthy pointing out the directory structure of the repository:

```
.
├── Dockerfile
├── README.md
├── data
│   ├── bitso
│   │   ├── btc_mxn
│   │   │   └── 2022-10-06
│   │   │       ├── 15
│   │   │       │   └── files.csv
│   │   │       ├── 16
│   │   │       │   └── files.csv
│   │   │       ├── 17
│   │   │       │   └── files.csv
│   │   │       ├── 18
│   │   │       │   └── files.csv
│   │   │       ├── 19
│   │   │       │   └── files.csv
│   │   │       └── 23
│   │   │           └── files.csv
│   │   └── usd_mxn
│   │       └── 2022-10-06
│   │           ├── 18
│   │           │   └── files.csv
│   │           ├── 19
│   │           │   └── files.csv
│   │           └── 23
│   │               └── files.csv
│   └── test_1
│       ├── markets.csv
│       └── similar_exchanges.csv
├── requirements.txt
├── run.sh
└── src
    ├── test_1.py
    ├── test_2.py
    ├── test_2_spread_validation.py
    └── utils
        ├── SpreadValidator.py
        ├── Ticker.py
        ├── __pycache__
        │   ├── SpreadValidator.cpython-38.pyc
        │   ├── Ticker.cpython-38.pyc
        │   ├── utils_test_1.cpython-38.pyc
        │   └── utils_test_2.cpython-38.pyc
        ├── utils_test_1.py
        └── utils_test_2.py
```

---
## Additional useful resources
* [Postman](https://www.postman.com/) - API platform for testing APIs
* [VS Code](https://code.visualstudio.com/) - Code Editor and IDE

---
## Future Considerations
Due to the time constraints during the development of this project, there were a couple of pending implementations which could benefit the overall functionality of the applications:
  - Update rather than ingest all the data again for the days following the first run on the first challenge
  - Use Webhooks on the Bitso API integration
  - Unit testing


## Developed by: Ivan Legorreta
**Phone number**: +52 55 1320 7574

**Email**: ilegorreta@outlook.com
