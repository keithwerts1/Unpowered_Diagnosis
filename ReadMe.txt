Welcome to the Unpowered Devices Report ReadMe Document.

The Purpose of this report is to help aid designers in finding hotspots where connectivity might be broken between a powered feature and an unpowered feature to speed along the process of energizing the grid.  You will be be running the a few SQL queries against the migration database to capture data from the OMS_UNPOWERED_FEATURES table and the OMS_CONNECTIVITY table, then gathering details on features from each Substation and Feeder ID that have unpowered features.  Then the Program 'FOS_FbyF.py' will run through each Feeder and create a report of the hotspots that designers can focus on during Feeder cleanup.  You will then take the output of that program and paste it into the excel template provided and send it to the designers.

First, let's start by pulling in the most recent code:

1. If this is your first time running the report, you will need to clone the program from github. Open up git bash, cd to the location that you want to clone the program to, and type:

git clone https://github.com/sqlblackbelt/UnpoweredDevices.git

Or, if you have already run this report before, make sure you grab the most recent code by opening up git bash, cd to your UnpoweredDevices folder, and run:

git pull

This is pull in the most recent code.

2. Once you have the code pulled, make sure that you have all files added to the correct locations:

Source: \\enttstnas01.corp.oncor.com\framme_extracts\Deployment Data Lake\FeederData\Pickles
**Note: Copy all of the contents of the Pickles folder
Target: FeederData\Pickles

All other files and folders should be there.

