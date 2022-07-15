import pickle
import logging
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def print_(palabra="Inicio"):
    print("=".rjust(50, "="))
    print(f"{palabra}".rjust(50, "."))
    print("=".rjust(50, "="))

def print__(palabra="Inicio"):
    print(f"{palabra}".rjust(50, "."))

def open_and_save_pickle(filename, log_message, new_key, new_value):
    """
    takes user as name of file user.pk
    log_message for debuggin porpuses, a message
    dict = {new_key: new_value}
    this dict is added to dict in user.pk file
    """
    out_file = f"pickle_files/{filename}.pk"
    with open(out_file, 'rb') as handle_file:
        dict = pickle.load(handle_file)
        logger.info(log_message)
        logger.info(dict)
        dict[new_key] = new_value
        with open(out_file, 'wb') as pickle_file:
            pickle.dump(dict, pickle_file)
    return None

def open_new_pickle(filename, log_message):
    """
    crea archivo vacio
    guarda en archivo el dict con 1 llave
    """
    dict = {}
    out_file = f"pickle_files/{filename}.pk"
    with open(out_file, 'wb') as pickle_file: # wb creates a new one
        logger.info(log_message)
        logger.info(dict)
        pickle.dump(dict, pickle_file)


def read_pickle(filename, log_message):
    out_file = f"pickle_files/{filename}.pk"
    with open(out_file, 'rb') as handle_file:
        dict_final = pickle.load(handle_file)
        logger.info(log_message)
        logger.info(dict_final)
    return dict_final
