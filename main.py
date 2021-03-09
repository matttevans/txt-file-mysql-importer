# Written by Matt Evans

import mysql.connector
import os
import re 

def Run():

	try:
		connection = mysql.connector.connect(host='localhost',
											 database='',
											 user='root',
											 password='')
		path = os.getcwd()
		filenames = os.listdir(path)
		
		table_count = 0
		
		for filename in filenames:
			
			if (filename.endswith(".txt")):
			
				table_name = filename.replace('.txt','').replace('.','_').lower().rstrip()
				
				create_table_query = 'CREATE TABLE IF NOT EXISTS `' + table_name + '` (email varchar(255), password varchar(255)) CHARACTER SET utf8'

				if(CheckTableExists(connection, table_name)):
				
					print('Starting ' + filename)
					print(create_table_query)
					
					cursor = connection.cursor()
					cursor.execute(create_table_query)
					
					query = "LOAD DATA LOCAL INFILE '" + filename + "' INTO TABLE `" + table_name + "` FIELDS TERMINATED BY ':'"
					print(query)
						
					cursor.execute(query)
					connection.commit()
					
					print('Finished ' + filename)	
					
					table_count += 1
					# delete file
					# os.remove(filename)
					
				else:
					print('Skipping ' + filename)
		
		print(str(table_count) + ' tables affected')
		
	except mysql.connector.Error as error:
		print("Failed to insert record into " + table_name + " table {}".format(error))

	finally:
		if connection.is_connected():
			connection.close()
			print("Connection closed")

def CheckTableExists(connection, tablename):

    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if cursor.fetchone()[0] == 1:
        cursor.close()
        return False

    cursor.close()
    return True
	
#
# Removes all parenthesis, square brackets, curly brackets, and their contents. Also removes www., converts to lower, and removes whitespace at the end
#	
def CleanFileNames():

	bracket_pattern = r'\[.*?\]'
	curly_pattern = r'\{.*?\}'
	parenthesis_pattern = r'\(.*?\)'

	path =  os.getcwd()
	filenames = os.listdir(path)

	for filename in filenames:
		
		if(filename.endswith('.txt')):
		
			temp = filename.replace('www.','').replace('Расшифровка ','').replace('ww.','').lower().rstrip()
			temp2 = re.sub(bracket_pattern, '', temp)
			temp3 = re.sub(curly_pattern, '',temp2)
			temp4 = re.sub(parenthesis_pattern, '', temp3)
			os.rename(filename, temp4)
			
def main():
	
	#CleanFileNames()
    Run()

if __name__ == "__main__":
    main()
