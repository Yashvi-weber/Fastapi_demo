from dotenv import load_dotenv
import os

load_dotenv()       #call this import files
a = os.environ.get("Password")   #os will let you
b = os.environ.get("my_database_url") 