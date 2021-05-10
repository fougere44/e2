# Analyse de la campagne de marketing par une institution bancaire portugaise
Ce répertoire vise à analyser des données de marketing en banque autour de la souscription d'un dépôt à long terme. Il a été crée dans le cadre du programme Data IA de l'école Simplon * Microsoft à Nantes.

Le jeu de données utilisé est issu du site UCI: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
Le fichier csv utilisé pour faire ces analyses est le suivant: bank-full.csv

## Manipuler le *notebook* localement (sur votre machine)

1. Installez Anaconda sur votre machine (https://www.anaconda.com/products/individual)

2. Clonez le dépôt :
    ```
    git clone https://github.com/fougere44/e2.git
    ```

3. Déplacez-vous dans le répertoire du dépôt :
    ```
    cd e2/project
    ```

4. Créez l'environnement virtuel python :
    ```
    python -m venv env
    ```

5. Activez l'environnement virtuel "env" :
    ```
    cd env/Scripts
    activate
    ```
    
6. Installer les librairies :
    ```
    pip install -r requirements.txt
    ```

7. Chargez les extensions Jupyter Lab :

    - pour les utilisateurs de Linux, WSL, Mac :
    ```
    bash binder/postBuild
    ```
    
    - pour les utilisateurs de PowerShell :
    ```
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install @jupyterlab/toc
    ```

8. Lancez Jupyter Lab :
    ```
    jupyter lab
    ```


## Lancer l'application Flask sur le port http://127.0.0.1:5000/ avec Visual Studio Code

1. Installez l'environnement de développement Visual Studio Code sur votre machine (https://code.visualstudio.com/)

2. Clonez le dépôt :
    ```
    git clone https://github.com/fougere44/e2.git
    ```

3. Déplacez-vous dans le répertoire du dépôt :
    ```
    cd e2/project
    ```

4. Lancer le projet sous Visual Studio Code avec le raccourci "code ."
   ```
    C:\Users\...\project\code .
    ```

5. Activez l'environnement virtuel "bank_env" :
    ```
    cd env/Scripts
    activate
    ```
    
6. Retourner dans le dossier "projet" :
    ```
    cd /
    cd C:\...\project
    ```

7. Définir les variables de l'application Flask :
    ```
    set FLASK_APP=app
    set FLASK_ENV=development
    flask run
    ```

8. Faire un ctrl + click à cette adresse : 
    ```
    http://127.0.0.1:5000/
    ```

9. Amusez-vous !


![alt text](https://i.ibb.co/3SPNGv8/flask-app.png)








## Langages 

Jupyter notebooks / Python / HTML5 / CSS3


