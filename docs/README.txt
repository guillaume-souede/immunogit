# Documentation du script GetLogicalModelAndMetadata.py

## Objectif du script
Ce script Python permet d’automatiser la **recherche, le téléchargement, la classification et l’archivage** de modèles au format SBML (Systems Biology Markup Language) depuis la base de données [BioModels](https://www.ebi.ac.uk/biomodels/), en utilisant leur API publique.
Le script cible les modèles contenant le mot-clé **"logical"**, et les trie selon la présence de termes biologiques spécifiques comme **"immun"** ou **"T cell"**.

Chaque modèle est :
- téléchargé sous forme de fichier `.xml` (format SBML),
- associé à ses métadonnées complètes enregistrées en `.json`,
- puis archivé dans un fichier `.zip`.
Les modèles sont ensuite organisés dans des dossiers selon la présence des mots-clés et leur statut de curation.

## Structure des résultats
Après exécution, les résultats sont structurés comme suit :

downloaded_models_logical/
├── immun/
│ ├── Curated_models/
│ └── No_Curated_models/
└── T-cell/
├── Curated_models/
└── No_Curated_models/

Chaque dossier contient des archives `.zip` individuelles, incluant :
- `modelID.xml` : fichier SBML du modèle,
- `modelID_metadata.json` : métadonnées du modèle,
- regroupés dans : `modelID.zip`.

##  Requête utilisée
La requête effectuée sur la base BioModels est :
logical AND modelformat:"SBML"
Elle sélectionne tous les modèles logiques au format SBML.

##  Fonctionnement du script

1. **Recherche des modèles** : envoie une requête à l’API BioModels.
2. **Récupération des métadonnées** complètes pour chaque modèle.
3. **Téléchargement du fichier SBML** depuis l’URL indiquée.
4. **Classification** selon :
     - la présence du mot-clé `"immun"` ou `"T cell"` dans les métadonnées.
     - le statut de curation du modèle (présence de "BIOM" dans l’ID → modèle curé).
5. **Archivage** : création d’un fichier `.zip` pour chaque modèle contenant :
      - le fichier `.xml`,  
      - les métadonnées `.json`.

---

##  Dépendances
Ce script utilise les bibliothèques suivantes :

    - `bioservices` : pour interagir avec l’API de BioModels,    
    - `requests` : pour télécharger les fichiers,
    - `json` : pour manipuler les métadonnées,
    - `zipfile` : pour créer les fichiers `.zip`,
    - `os` : pour la gestion des dossiers et fichiers.
  Installation recommandée (via pip) :
```bash
pip install bioservices requests
Le script affiche dans le terminal la progression du téléchargement et de la classification des modèles.
