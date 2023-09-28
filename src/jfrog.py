#Definition: To send jar file to jFrog Repository this program is developed
#Developer : Gaurang Panchani
#Version   : v1
#Date      : 24-SEP-2023

import requests

file_url = "http://52.3.242.163:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"

file_name = "kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
auth_cred = ("admin", "Admin@1234")
    
with open(file_name, 'rb') as fobj:
    res = requests.put(file_url, auth=auth_cred, data=fobj)
    print(res.text)
    print(res.status_code)