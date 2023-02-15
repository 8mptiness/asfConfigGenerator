import json
import os

def createFiles(log_pass, name, count, mafiles):
    with open(log_pass) as f:
        db_file = {"_MobileAuthenticator":{"identity_secret":"","shared_secret":""}}
        newpath = f'{os.path.abspath(os.curdir)}\config' 

        if not os.path.exists(newpath):
            os.makedirs(newpath)

        for line in f:
            log, pas = line.split(':')
            log, pas = log.strip(), pas.strip()

            with open('config.json') as f:
                data = json.load(f)
                data["SteamLogin"] = log
                data["SteamPassword"] = pas

            if len(name) == 0:
                with open(f'{newpath}\{log}.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                with open(f'{newpath}\{name}{count}.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

            if mafiles:
                with open(f'{mafiles}\{log}.maFile') as f:
                    mafile = json.load(f)
                    shared_secret = mafile["shared_secret"]
                    identity_secret = mafile["identity_secret"]

                if len(name) == 0:
                    with open(f'{newpath}\{log}.db', 'w') as f:
                        db_file["_MobileAuthenticator"]["identity_secret"] = identity_secret
                        db_file["_MobileAuthenticator"]["shared_secret"] = shared_secret
                        json.dump(db_file, f, ensure_ascii=False)
                else:
                    with open(f'{newpath}\{name}{count}.db', 'w') as f:
                        db_file["_MobileAuthenticator"]["identity_secret"] = identity_secret
                        db_file["_MobileAuthenticator"]["shared_secret"] = shared_secret
                        json.dump(db_file, f, ensure_ascii=False)
                     
            count += 1


def renameFiles(path):
    newpath = fr'{os.path.abspath(os.curdir)}\renamed'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for f in os.listdir(path):
        if f != 'manifest.json' and '.maFile' in f:
            with open(f'{path}\{f}') as file:
                data = json.load(file)
                name = data["account_name"]

            with open(f'{newpath}\{name}.maFile', 'w') as f:
                json.dump(data, f, ensure_ascii=False)