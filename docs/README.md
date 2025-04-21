# Documentation du script SMBLGetmodelandmetadata.py    

## Objectif du script    
Ce script permet de récupérer automatiquement des modèles SBML (Systems Biology Markup Language) depuis la plateforme BioModels, en fonction de requêtes spécifiques. Pour chaque modèle, le script télécharge :  
- le fichier SBML (.xml),  
- les métadonnées associées (.json),    
et archive les deux fichiers dans un fichier ZIP.      

Les modèles sont ensuite classés dans des répertoires selon des catégories biologiques pertinentes (immuno-oncology, immuno-thérapie, réponse immunitaire, etc.), afin de faciliter l'organisation et l'analyse.      

## Résultats obtenus        
Après exécution du script sur les modèles liés à l’immunité humaine (taxonomie 9606), nous avons obtenu 131 modèles SBML manuellement curés :      
- 68 modèles tagués "immuno-oncology"       
- 63 modèles non tagués "immuno-oncology", parmi lesquels :     
  - Certains sont classés selon leur titre en :      
    - Immun-therapy (3 modèles contenant "therapy),      
    - Response-immun (6 modèles contenant "response"),        
    - System-immun (5 modèle contenant "system"),      
  - Les 49 modèles restants sont classés dans le répertoire "others".      

L'ensemble des résultats est organisé dans le répertoire :      
models/BioModels/SBML/      
Avec les sous-répertoires suivants :      
  - Biomodels_immuno_oncology/      
  - Biomodels_therapy/      
  - Biomodels_response-immun/      
  - Biomodels_system-immun/      
  - Biomodels_others/      

Chaque modèle est stocké sous forme d’archive ZIP contenant :      
- le fichier .xml (SBML),      
- et le fichier .json (métadonnées).      

## Requêtes utilisées    
Le comportement du script dépend de la requête passée à l’API BioModels. Voici les différentes requêtes utilisées :    
- **Tous les modèles liés à l’immunité humaine :**      
immun* AND curationstatus:"Manually curated" AND modelformat:"SBML" AND TAXONOMY:9606    
- **Modèles tagués "immuno-oncology" :**      
immun* AND curationstatus:"Manually curated" AND modelformat:"SBML" AND TAXONOMY:9606 AND submitter_keywords:"Immuno-oncology"    
- **Modèles non tagués "immuno-oncology" :**      
immun* AND curationstatus:"Manually curated" AND modelformat:"SBML" AND TAXONOMY:9606 AND NOT submitter_keywords:"Immuno-oncology"    

## Flux de travail du script    
- **Requête de recherche**    
Le script effectue une recherche sur la base BioModels en utilisant une requête définie    
- **Récupération des modèles**    
Les modèles correspondant à la requête sont récupérés grâce à l’API BioModels, avec gestion de la pagination pour parcourir toutes les pages de résultats.    
- **Téléchargement des fichiers SBML**    
Pour chaque modèle, le fichier .xml au format SBML est téléchargé depuis l’URL fournie par BioModels.    
- **Récupération des métadonnées**      
Les métadonnées JSON associées à chaque modèle sont également téléchargées.    
- **Archivage dans un fichier ZIP**    
Chaque modèle et ses métadonnées sont compressés dans un fichier ZIP unique.    
- **Organisation par catégorie**    
Les fichiers ZIP sont ensuite classés dans des répertoires selon des catégories     

## Fonctions principales du script    
**1. get_all_models(query, page_size=10)**      
  - **But** : Récupère tous les modèles correspondant à une requête.    
  - **Paramètres** :    
    - **query (str)** : requête de recherche    
    - **page_size (int)** : nombre de modèles par page (par défaut 10)    
  - **Retour** : Liste complète des modèles    
  - **Fonctionnement** : pagination automatique via l’API BioModels    

**2. download_model_file(model_id, sbml_url, directory)**  
  - **But** : Télécharge le fichier SBML du modèle  
  - **Paramètres** :  
    - **model_id** : ID du modèle  
    - **sbml_url** : URL de téléchargement  
    - **directory** : répertoire de destination  
  - **Retour** : chemin du fichier local téléchargé  
  - **Gestion des erreurs** : retourne None si échec  

**3. download_model_with_metadata(model_data, base_directory)**  
  - **But** : Télécharge le fichier SBML et les métadonnées, et les archive  
  - **Paramètres** :  
    - **model_data** : dictionnaire avec infos du modèle  
    - **base_directory** : répertoire principal de stockage  
  - **Étapes** :  
    - Vérifie l’URL du modèle  
    - Classe le modèle selon des mots-clés dans le titre  
    - Télécharge le SBML  
    - Télécharge les métadonnées (API)  
    - Sauvegarde en .json  
    - Archive .xml + .json dans un .zip  
    - Nettoie les fichiers temporaires  

**4. main()**  
  - **But** : Fonction principale  
  - **Étapes** :  
      - Définit la requête  
      - Crée les répertoires de sortie  
      - Récupère tous les modèles  
      - Lance download_model_with_metadata() pour chaque modèle  

## Sorties du script  
**1. Répertoires organisés**  
models/BioModels/SBML/  
  - Biomodels_immuno_oncology/  
  - Biomodels_therapy/  
  - Biomodels_response-immun/  
  - Biomodels_system-immun/  
  - Biomodels_others/  

**2. Fichiers ZIP par modèle**  
Chaque .zip contient :  
  - modelID.xml (le modèle SBML)  
  - modelID_metadata.json (métadonnées associées)  

## Exemple d’utilisation  
Bash :    
python SMBLGetmodelandmetadata.py  
- Le script exécute la requête définie, télécharge les fichiers SBML + métadonnées, classe et archive chaque modèle.  
- Messages affichés en console pour suivre la progression.  

## Dépendances  
- **bioservices** : interaction avec l’API BioModels  
- **requests** : téléchargement de fichiers  
- **json** : traitement des métadonnées  
- **zipfile** : création des fichiers ZIP  
- **os** : gestion des fichiers et répertoires  


