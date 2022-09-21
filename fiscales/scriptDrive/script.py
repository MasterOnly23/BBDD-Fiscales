from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive 
from pydrive2.files import FileNotUploadedError
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()


credentials_path = 'scriptDrive/credentials_module.json'

#login

def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = credentials_path
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credentials_path)

    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8080])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(credentials_path)
    credenciales = GoogleDrive(gauth)
    return credenciales

def list_file(query):
    busqueda = []
    credentials = login()
    # Archivos con el nombre 'mooncode': title = 'mooncode'
    # Archivos que contengan 'mooncode' y 'mooncoders': title contains 'mooncode' and title contains 'mooncoders'
    # Archivos que NO contengan 'mooncode': not title contains 'mooncode'
    # Archivos que contengan 'mooncode' dentro del archivo: fullText contains 'mooncode'
    # Archivos en el basurero: trashed=true
    # Archivos que se llamen 'mooncode' y no esten en el basurero: title = 'mooncode' and trashed = false

    lista_archivos = credentials.ListFile({'q':query}).GetList()
    # for f in lista_archivos:
    #     nombre_archivo = f['title']
    #     fecha_creacion = f['mimeType']
    #     fecha_modificacion = f['createdDate']
    #     size_archivo = f['modifiedDate']
    #     link = f['fileSize']
    #     busqueda.append(f)

    return lista_archivos

