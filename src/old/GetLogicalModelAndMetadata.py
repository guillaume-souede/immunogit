#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Fer 27 22:35:34 2025

@author: issakerimakhalil
"""

import os
import zipfile
import requests
import json
from bioservices import BioModels

# Initialisation du service BioModels
s = BioModels()

def get_all_models(query, page_size=10):
    """
    Fonction pour récupérer tous les modèles correspondant à la requête avec pagination.
    """
    models = []
    offset = 0

    while True:
        try:
            search_results = s.search(query, offset=offset)
            
            if 'models' not in search_results or not search_results['models']:
                break
            
            models.extend(search_results['models'])
            offset += page_size
            print(f"Page {offset // page_size} téléchargée, {len(search_results['models'])} modèles récupérés.")
        
        except Exception as e:
            print(f"Erreur lors de la récupération des modèles : {e}")
            break
    
    return models

def download_model_file(model_id, sbml_url, directory):
    """
    Télécharge le fichier SBML du modèle.
    """
    try:
        sbml_filename = f"{model_id}.xml"
        model_path = os.path.join(directory, sbml_filename)

        response = requests.get(sbml_url)
        if response.status_code == 200:
            with open(model_path, 'wb') as f:
                f.write(response.content)
            print(f"Modèle {model_id} téléchargé avec succès.")
        else:
            raise RuntimeError(f"Erreur lors du téléchargement du modèle {model_id}: {response.status_code}")

        return model_path

    except Exception as e:
        print(f"Erreur lors du téléchargement du modèle {model_id}: {e}")
        return None

def download_model_with_metadata(model_data, base_directory):
    """
    Télécharge le modèle et ses métadonnées, puis les enregistre dans un fichier zip.
    """
    try:
        model_id = model_data['id']
        sbml_url = model_data.get('url', None)
        title = model_data.get('name', "").lower()
        keywords = model_data.get('submitter_keywords', "").lower()
        immun = model_data.get('immun', "").lower()
        
        def contains_keyword(data, keyword):
            """
            Recherche récursive du mot-clé dans toutes les valeurs de type str du dictionnaire/liste.
            """
            if isinstance(data, dict):
                return any(contains_keyword(v, keyword) for v in data.values())
            elif isinstance(data, list):
                return any(contains_keyword(item, keyword) for item in data)
            elif isinstance(data, str):
                return keyword.lower() in data.lower()
            return False


        if not sbml_url:
            print(f"Aucune URL trouvée pour le modèle {model_id}.")
            return

        

        # Récupérer les métadonnées complètes
        try:
            full_metadata = s.get_model(model_id)
        except Exception as e:
            print(f"Erreur lors de la récupération des métadonnées complètes pour {model_id}: {e}")
            return
        
        # Déterminer le dossier de destination final
       
        if contains_keyword(full_metadata, "immun"):
            directory = os.path.join(base_directory, "immun")
            if "BIOM" in model_id:
               directory = os.path.join(directory, "Curated_models")
            else:
               directory = os.path.join(directory, "No_Curated_models")
        elif contains_keyword(full_metadata, "T cell"):
            directory = os.path.join(base_directory, "T-cell")
            if "BIOM" in model_id:
               directory = os.path.join(directory, "Curated_models")
            else:
               directory = os.path.join(directory, "No_Curated_models")
        else:
            return 
            
        # Créer le dossier s'il n'existe pas
        os.makedirs(directory, exist_ok=True)

        # Télécharger le fichier SBML
        model_path = download_model_file(model_id, sbml_url, directory)
        if model_path is None:
            return
     
            



        # Sauvegarder les métadonnées en JSON
        metadata_filename = f"{model_id}_metadata.json"
        metadata_path = os.path.join(directory, metadata_filename)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(full_metadata, f, ensure_ascii=False, indent=4)

        # Créer un fichier zip contenant le modèle et ses métadonnées
        zip_filename = os.path.join(directory, f"{model_id}.zip")
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(model_path, os.path.basename(model_path))
            zipf.write(metadata_path, os.path.basename(metadata_path))

        # Supprimer les fichiers temporaires après zippage
        os.remove(model_path)
        os.remove(metadata_path)

        print(f"Modèle {model_id} et ses métadonnées enregistrés dans {zip_filename}")

    except Exception as e:
        print(f"Erreur lors du traitement du modèle {model_data['id']} : {e}")

def main():
    # Requête mise à jour
    query = (
        'logical AND modelformat:"SBML"'
    )

    # Répertoire principal
    base_directory = "downloaded_models_logical"
    os.makedirs(base_directory, exist_ok=True)

    # Obtenir tous les modèles
    models = get_all_models(query)

    # Télécharger chaque modèle et les classer
    for model_data in models:
        download_model_with_metadata(model_data, base_directory)

if __name__ == "__main__":
    main()