
import os
import pandas as pd
import config

ls = pd.read_csv('plate_list.csv').columns.tolist()

for file in ls[1:]:
        print(os.listdir('../'))
        sqlite = '{}.sqlite'.format(file)
        csv = '{}_loc.csv'.format(file)
        os.system("aws s3 cp {} ./".format(config.sql_location))
        os.system("sqlite3 -header -csv {} 'SELECT Image_Metadata_Plate, Image_Metadata_Well, Image_Metadata_Site, Nuclei_Location_Center_X, Nuclei_L$")
        os.system("aws s3 cp {} {}".format(csv, config.csv_location))
        print("done with file: {}".format(file))
        os.remove(sqlite)
        os.remove(csv)


