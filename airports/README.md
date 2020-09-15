# airports

airport dataset with latitude, longitude, elevation, country and other information.

the `airports.json` file is compiled from the data available at [ourairports.com/data/](https://ourairports.com/data/) using the files `airports.csv` and `countries.csv`

a python script is used to create the json file, some lines needed to be fixed in the original file because of the presence of the delimiter `,` in the name of some airports and only airports of the type `small_airport`, `medium_airpot` and `large_airport` are present in the file.
