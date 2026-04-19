# Documentation for the script **SMBLGetmodelandmetadata.py** 
## **Script Objective** 
This script automatically retrieves **SBML** (Systems Biology Markup Language) models from the **BioModels** platform based on specific queries. For each model, the script downloads:  
- the SBML file (`.xml`),  
- the associated metadata (`.json`),  
and archives both files into a **ZIP** file.  

The models are then categorized into directories based on relevant biological categories (**immuno-oncology**, **immuno-therapy**, **immune response**, etc.) to facilitate organization and analysis.  

## **Results Obtained** After running the script on models related to human immunity (**taxonomy 9606**), we obtained **131 manually curated SBML models**:  
- **68 models** tagged "immuno-oncology"  
- **63 models** not tagged "immuno-oncology", including:  
  - **Immune-therapy** (3 models containing "therapy"),  
  - **Immune-response** (6 models containing "response"),  
  - **Immune-system** (5 models containing "system"),  
- The **49 remaining models** are classified in the "others" directory.  

The results are organized in the directory:  
`models/BioModels/SBML/`  
With the following sub-directories:  
  - `Biomodels_immuno_oncology/`  
  - `Biomodels_therapy/`  
  - `Biomodels_response-immun/`  
  - `Biomodels_system-immun/`  
  - `Biomodels_others/`  

Each model is stored as a **ZIP archive** containing:  
- the `.xml` file (SBML),  
- and the `.json` file (metadata).  

## **Queries Used** The script's behavior depends on the query passed to the BioModels API. Here are the different queries used:  
- **All models related to human immunity:** `immun* AND curationstatus:"Manually curated" AND modelformat:"SBML" AND TAXONOMY:9606`  
- **Models tagged "immuno-oncology":** `immun* AND curationstatus:"Manually curated" AND modelformat:"SBML" AND TAXONOMY:9606 AND submitter_keywords:"Immuno-oncology"`  
- **Models not tagged "immuno-oncology":** `immun* AND curationstatus:"Manually curated" AND modelformat:"SBML" AND TAXONOMY:9606 AND NOT submitter_keywords:"Immuno-oncology"`  

## **Script Workflow** - **Search Query** The script performs a search on the BioModels database using a defined query.  
- **Model Retrieval** Models matching the query are retrieved via the BioModels API, with pagination handling to navigate through all result pages.  
- **SBML File Download** For each model, the `.xml` file in SBML format is downloaded from the URL provided by BioModels.  
- **Metadata Retrieval** The JSON metadata associated with each model is also downloaded.  
- **ZIP Archiving** Each model and its metadata are compressed into a single ZIP file.  
- **Organization by Category** The ZIP files are then sorted into directories according to categories.  

## **Main Functions of the Script** **1. `get_all_models(query, page_size=10)`** - **Purpose**: Retrieves all models matching a query.  
  - **Parameters**:  
    - **`query (str)`**: search query  
    - **`page_size (int)`**: number of models per page (default 10)  
  - **Returns**: Full list of models  
  - **Operation**: automatic pagination via the BioModels API  

**2. `download_model_file(model_id, sbml_url, directory)`** - **Purpose**: Downloads the model's SBML file  
  - **Parameters**:  
    - **`model_id`**: Model ID  
    - **`sbml_url`**: download URL  
    - **`directory`**: destination directory  
  - **Returns**: path of the downloaded local file  
  - **Error Management**: returns `None` if failed  

**3. `download_model_with_metadata(model_data, base_directory)`** - **Purpose**: Downloads the SBML file and metadata, and archives them  
  - **Parameters**:  
    - **`model_data`**: dictionary with model info  
    - **`base_directory`**: main storage directory  
  - **Steps**:  
    - Verifies the model URL  
    - Categorizes the model based on keywords in the title  
    - Downloads the SBML  
    - Downloads the metadata (API)  
    - Saves as `.json`  
    - Archives `.xml` + `.json` into a `.zip`  
    - Cleans up temporary files  

**4. `main()`** - **Purpose**: Main function  
  - **Steps**:  
      - Defines the query  
      - Creates output directories  
      - Retrieves all models  
      - Launches `download_model_with_metadata()` for each model  

## **Script Outputs** **1. Organized Directories** `models/BioModels/SBML/`  
  - `Biomodels_immuno_oncology/`  
  - `Biomodels_therapy/`  
  - `Biomodels_response-immun/`  
  - `Biomodels_system-immun/`  
  - `Biomodels_others/`  

**2. ZIP Files per Model** Each `.zip` contains:  
  - `modelID.xml` (the SBML model)  
  - `modelID_metadata.json` (associated metadata)  

## **Usage Example** Bash:  
`python SMBLGetmodelandmetadata.py`  
- The script executes the defined query, downloads the SBML + metadata files, categorizes, and archives each model.  
- Messages are displayed in the console to track progress.  

## **Dependencies** - **`bioservices`**: interaction with the BioModels API  
- **`requests`**: file downloading  
- **`json`**: metadata processing  
- **`zipfile`**: creation of ZIP files  
- **`os`**: management of files and directories
