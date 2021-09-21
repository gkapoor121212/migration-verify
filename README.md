# Migration Verify

Contains utility Python scripts to verify successful migration to a different platform and generate reports. It can be currently used for 

  - Getting all the URLs of a current website and verification of their status in new the website.


### Installation

Migration Verification Tool requires [Python3](https://www.python.org/) v3+ to run.

Install the dependencies to start using the scripts.

```sh
$ pip install -r requirements.txt
```

### How to use

To get all the links of website use the following command
```sh
$ python3 GetAllTheLinks.py -u https://example.com
```

This command will generate a file 'URLList.csv' which will contain all the URLs. Feel free to modify the available links based on your status verification requirement.

To get the URL status of all these use this command. Make sure you are providing a correct URL for development instance of new version of your website.
```sh
$ python3 GetLinkStatus.py -u https://dev.example.com
```

The generated CSV will contain the new website URL along with the HTTP status. Load the CSV file in Google Sheet and use/present/modify data accordingly.

License
----

MIT


**Free Software, Hell Yeah!**
