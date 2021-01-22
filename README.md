# DNACArchiveConf

*Retrieves and archives in a zip file all config files from devices managed by DNAC*

---


## Motivation

DNAC 2.1.2 introduced a REST endpoint for device configuration retrieval.  This script demonstrates how to leverage this endpoint to retrieve startup and running configuration of all devices managed by DNAC.

## Installation

To install please clone this directory.  
Install the requirements
```bash
pip install -r requirements.txt
```
## Technologies & Frameworks Used

To function this script uses both the Requests library and the DNA Center SDK (dnacentersdk).  For the script to work please make sure that this libraries are in your project python (virtual environment).  



## Usage

The project has been tested with Python 3.8, but is likely to work with 3.4 onwards.  
Before running the script it needs to be made aware of the credentials for your DNA Center.  
Please amend the creds.json file with your credentials
```bash
{
	"dnacurl": "<url or ip of DNA Center>",
	"username": "<your username>",
	"passwd": "<your password>",
	"version": "2.1.2"
}
```

To run the script in your environment
```bash
python ConfArchAll.py"
```

The script will log onto DNAC center and retrieve the all the configuration files.  The configuration files will be saved as a **ZIP** file in the directory that the script is run from. The file is called _dnacconfall.zip_

## Unarchiving the ZIP file
Only tested on MAC as of today.  
Using the unzip command line tool or the default unzip in Finder will result in compression method not supported.  
To unzip the files then please make use of the Mac utility (available from the App Store) - **The Unarchiver** . 
The downloaded zip file is password protected.  
The password to de-encrypt the files is **Cisco123#**

**ToDo's:** 

Allow user input to create own password for zip files.

Allow user input to determine name of downloaded zip file.

Prompt user for management IPs for Devices to retrieve rather than all devices.  

Test on Linux


## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Simon Hart <sihart@cisco.com>

## Credits

Thanks to Russ Widener for sharing the Cisco CX technote created by Tomas De Leon that provided documentation on the Configuration archive REST endpoint

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
