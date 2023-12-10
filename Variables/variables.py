import configparser

config = configparser.ConfigParser()
config.read("./Settings/config.ini")
# USDA_api_key = config['USDA']['api_key']

USDA_api_key = "vl5XPpYd1iF0LcsdCQ7b6Mccew17sM22NfyedsxW"

usda_food_searching_by_name = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={USDA_api_key}&query="


#------------- database variables -------------
database_products_ru_table_name = "products_ru"
products_ru_database_fields = ["product_name", "fats", "proteins", "carbohydrates", "energy"]
