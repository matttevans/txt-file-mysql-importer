# Text file to MySQL importer
Mainly created for the importation of the `Collection 1` data breach. 
Given a directory, bulk imports all colon-delimited `.txt` files into a MySql database in the format `email:password`. Creates a new table for each text file. 
Easily modified to however your text file is set up. Just change the columns and delimiter to whatever you need. 

This is by no means as efficient as possible but it gets the job done in a relatively quick manner. 

## Installation
Move/Copy `main.py` to the same directory as your `.txt` files.

## Usage
`main.py`

## Features
* Bulk-rename all files
  - Remove all `www.`
  - Strip all parenthesis `()`, square brackets `[]`, curly brackets `{}` and their contents.
  - Strip all whitespace
* Create a new table for each file
  - Example:
    - `website1.com.txt {12,000}[NOHASH].txt` becomes `website1_com`
* Optionally delete files when completed.

## Example 
`website1.com {12,000} [NOHASH].txt`
```
1 email@example.com:password1234
2 test@example.com:qwertyuiop
...
...
12000 admin@example.com:passw0rd
```

