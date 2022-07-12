import pickle
import logging
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
logger.info("default protocol: " + str(pickle.DEFAULT_PROTOCOL))

username = "ramiroquai"


# crea dict vacio 
# crea archivo vacio
# guarda en archivo el dict con 1 llave
dict = {}
out_file = f"pickle_files/{username}.pk"

dict["atributo1"] = "11"
with open(out_file, 'wb') as pickle_file:
    pickle.dump(dict, pickle_file)


# devuelve el dict creado
# agrega una llave y actuliza la llave update
with open(out_file, 'rb') as handle_file:
    dict = pickle.load(handle_file)
    assert(dict == {"atributo1": "11"})
    logger.info("paso 2")
    logger.info(dict)
    dict["atributo2"] = "2"
    with open(out_file, 'wb') as pickle_file:
        pickle.dump(dict, pickle_file)


# devuelve el dict creado
# agrega una llave y actuliza la llave update
with open(out_file, 'rb') as handle_file:
    dict = pickle.load(handle_file)
    logger.info("paso 2.1")
    logger.info(dict)
    assert(dict == {"atributo1": "11", "atributo2": "2"})
    dict["atributo3"] = "33"
    with open(out_file, 'wb') as pickle_file:
        pickle.dump(dict, pickle_file)


with open(out_file, 'rb') as handle_file:
    dict_final = pickle.load(handle_file)
    logger.info("paso 3")
    logger.info(dict)
    assert(dict_final == {"atributo1": "11", "atributo2": "2", "atributo3": "33"})

# devuelve el dict creado
# y haz el request