![image](raw/logo.png)

# ImmunoGIT: A Repository of Models and Metadata for Human Immune System Responses

## Description
ImmunoGIT is a project focused on extracting, enriching, and organizing computational models related to immune system responses. The project interacts with the BioModels platform to retrieve SBML and SBML-QUAL models, enriches their metadata with relevant biological descriptions, and centralizes them in a public GitHub repository with a user-friendly interface via GitHub Pages.

## Table of Contents
- [Installation and Quick Startup](#installation-and-quick-startup)
- [Key Features](#key-features)
- [Folder Structure](#folder-structure)
- [Model Verification](#model-verification)
- [Contributing](#contributing)
- [GitHub Pages](#github-pages)
- [Documentation and User Guide](#documentation-and-user-guide)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [References](#references)

## Installation and Quick Startup
To set up the project locally, follow these steps:

### Running Python Notebooks
1. Launch Jupyter notebook:
    ```bash
    jupyter notebook
    ```
2. Open `GetModelsAndMetadata.ipynb` and run the cells to interact with the BioModels API.

### Browsing and Downloading Models
- Access the GitHub Pages interface for viewing and downloading models.
- Browse through the organized models by source and format.
- Download metadata in JSON or CSV format.

## Key Features

### Development of Python3 Notebooks
- **Objective**: Interface with BioModels API using Python notebooks.
- **Tools**: `bioservices` library.
- **Steps**:
    - Use `GetModelsAndMetadata.ipynb` to search for and download SBML/SBML-QUAL models.
    - Filter models based on keywords like "immune response," "cytokines," etc.
    - Retrieve metadata (ID, name, authors, description) in JSON format.

### Metadata Extraction and Enrichment
- **Objective**: Enrich metadata of models that are not manually curated.
- **Steps**:
    - Add tags and annotations compliant with international standards (e.g., Gene Ontology, MeSH).
    - Enrich SBML-QUAL metadata with both biological and relevant descriptions.
    - Use GUI tools for tagging, and apply FAIR principles.

### Result Centralization
- **Objective**: Host models and enriched metadata in this GitHub repository.
- **Steps**:
    - Organize models into subdirectories based on source (e.g., BioModels, Reactome).
    - Centralize metadata in JSON and CSV formats.
    - Provide a web interface using GitHub Pages for browsing and downloading models.

### Model Verification and Testing
- **Objective**: Verify the format of models (SBML/SBML-QUAL).
- **Steps**:
    - Use scripts to check if the models conform to expected formats.

## Folder Structure
Here’s the structure of the repository:
```
/models/
    /BioModels/        # Models from BioModels
    /Reactome/         # Models from Reactome
    /SBGN/             # Models in SBGN format
/metadata/
    models_metadata.json  # Global metadata
    metadata_BioModels.json  # BioModels-specific metadata
/notebooks/
    GetModelsAndMetadata.ipynb  # Python scripts for interacting with BioModels
/docs/
    README.md             # Project overview and instructions
    UserGuide.md          # Detailed usage instructions
    ContributionGuide.md  # How to contribute to the project
```

## Model Verification

Before integrating models into the GitHub repository, we ensure they meet the following criteria:
- **Format**: Check that models are in SBML or SBML-QUAL format.
- **Metadata**: Ensure that metadata is enriched and complies with FAIR principles.
- **Test models** for compatibility with existing tools.

## Contributing

If you’d like to contribute :

For detailed instructions, refer to the [Contribution Guide](docs/ContributionGuide.md).

## GitHub Pages

Visit the GitHub Pages site to:
- Browse models and metadata.
- Download models and metadata files.
- Access interactive visualizations or results.

## Documentation and User Guide

A detailed user guide will be available in the `docs/` folder. The guide will include:
- How to use the notebooks.
- Step-by-step instructions for interacting with models and metadata.
- Troubleshooting and common errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Additional assistance
- To view the technical specifications, see [Specifications.md](Specifications.md).

---

## Credits

### Supervisors
- **Anna Niarakis** – PU, CoSysBio, MCD-CBI  
- **Nicolas Ricort - Teixidor** – IE, CoSysBio, MCD-CBI

### Students
- Guillaume Souède  
- Issa Kerima Khalil  
- Mamadou Hawa Bakle  
- Yasmine Boukakida

### Affiliations
- **University of Toulouse**  
M1 Bioinformatics and Systems Biology (M1-BBS)

- **Building Immune Digital Twins WG (BIDT-WG)**  
    Research Data Alliance (RDA)

- **Centre de Biologie Intégrative Toulouse (CBI)**  
Molecular, Cellular and Developmental biology unit (MCD)  
Computational Systems Biology for complex human diseases (CoSysBio)

## References

1. [Research Data Alliance (RDA)](https://www.rd-alliance.org/about-the-rda/)
2. [Building Immune Digital Twins WG Feed](https://www.rd-alliance.org/groups/building-immune-digital-twins-wg/activity/)
3. [RDA Working Group: Building Immune Digital Twins - Case Statement](https://www.rd-alliance.org/wp-content/uploads/2024/03/Building-Immunge-Digital-Twins-WG_Case_Statement_Revised.pdf)
