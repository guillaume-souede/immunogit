![image](raw/logo.png)

# ImmunoGIT Specifications document

## Biological introduction
This project lies at the interface between computational biology and immunology. By bridging these two fields, the construction of Immune Digital Twins (IDTs) representing dynamic virtual representations of the human immune system will enable us to understand and predict how the immune system responds to a variety of situations.

As the science that studies the immune system and its regulation, immunology represents a real stake in the treatment of autoimmune diseases (AIDs) such as multiple sclerosis [[1]](#1), rheumatoid arthritis [[2]](#2), or systemic lupus erythematosus [[3]](#3), which affect millions of people worldwide, often with severe complications. Both public and private laboratories (INSERM [[4]](#4) and Sanofi [[5]](#5)) are working in this area, offering complex treatments such as biotherapies and immunosuppressants. DDDTs (Digital Drug Development Twins) could accelerate this pharmaceutical development process while reducing costs, as DTs enable the impact of treatments to be modeled at various levels, including the identification of therapeutic targets and drug validation [[6]](#6).

The wide diversity of actors involved in the immune system and the resulting pathologies (which vary in severity) call for the use of omics approaches, which enable in-depth analysis of the underlying molecular mechanisms. These novel approaches to medicine are paving the way for targeted and personalized therapies.
However, the use of immunosuppressants is not a harmless practice: for instance, according to the American Gastroenterology Association (AGA), reactivation of hepatitis B is a major risk for some patients [[7]](#7). The AGA has updated its recommendations: the decision between antiviral prophylaxis or clinical follow-up depends on the level of risk and the type of treatment. In addition, the regulatory and ethical aspects associated with the use of DTs in healthcare settings are crucial: Food and Drug Administration (FDA) and European Medicines Agency (EMA) require rigorous standards to be met in order to be considered as medical devices. Ethical issues, notably relating to data protection, will also need to be swept under the carpet [[8]](#8).

A wide range of actors in fields such as proteomics, metabolomics and (spatial) transcriptomics are involved, such as the study of gene expression regulation and spatial transcriptomics, which maps the expression of genes involved in a tissue, and could help prevent these IAMs. 

Computational models are essential tools for simulating and analyzing the complex mechanisms of the immune system. These models enable molecular and cellular interactions to be reproduced, making it easier to optimize therapeutic strategies. However, their development is often hampered by the absence of well-structured repositories to organize and share these resources. Databases such as BioModels [[[9]](#19) [[10]](#10) host biological models in Systems Biology Markup Language [[11]](#11) (SBML) format, designed to represent and exchange models of biochemical reactions.
We'll also be using files in Systems Biology Marked Up Language-qualitative [[12]](#12) ie SBML-qual, an extension of SBML that enables biological systems to be modeled qualitatively using a Boolean and logical approach. It allows systems to be modeled without the need for precise quantitative data, making it particularly well suited to the study of regulatory and signaling networks. Thanks to its interoperability with different software packages, SBML-QUAL facilitates the collaborative exchange, analysis and development of models, thus contributing to a better standardization of qualitative approaches in systems biology.

But models specific to the immune system remain scattered and insufficiently organized. This project aims to fill this gap by creating a dedicated repository, in line with a roadmap derived from the state of the art [[13]](#13) In accordance with the FAIR [[14]](#14) principles (Findable, Accessible, Interoperable, Reusable), the repository will be modular, practical for group work, and have a robust infrastructure.

This repository will centralize and annotate relevant computational models, while making them accessible for applications such as the construction of immune digital twins. By building on existing resources and integrating with the short-term goals of international collaborative efforts, this project will help lay the foundations for a scalable digital infrastructure, essential for meeting the challenges of precision medicine.

## Host Team
This project is led by Professor Anna Niarakis and Engineer Nicolas Ricort-Teixidor, both of whom work in the Computational Systems Biology Pole at the Toulouse Center for Integrative Biology (CBI).

The CBI is an international multidisciplinary research structure dedicated to the understanding of how living organisms function, using what are known as integrative and multi-scale approaches. Made up of several laboratories, including the host laboratory Molecular, Cellular and Developmental Biology (MCD), its research themes cover a wide range of fields addressing major health-related societal issues. 

More specifically, in the context of this project, it is involved in CoSysBio [(Computational Systems Biology for complex human diseases)](https://cbi-toulouse.fr/eng/equipe-niarakis), which develops integrative approaches combining mathematics, computer science and bioinformatics to identify new therapeutic targets and model complex pathologies. Immunological digital twins are a major challenge: hybrid models combining artificial intelligence and mechanistic networks could predict the evolution of diseases and refine therapeutic strategies in personalized medicine [[15]](#15). Historically, a digital twin is an organized set of adaptable models that emulate the behaviors of a given physical system (a term derived from “industry”) using data obtained throughout its life cycle. It is therefore a dynamic model, which can have several levels of complexity (known as “digitization”). They help optimize diagnosis and treatment (dose), particularly for diseases involving the immune system. 

The ImmunoGIT initiative will contribute to this by structuring and sharing models dedicated to these immune pathologies.

More broadly, the project will benefit from the support of the Research Data Alliance [[16]](#16) (RDA). Created in 2013, this international organization is dedicated to the creation of standards and the interoperability of biological data. It acts as a bridge between researchers and clinicians from a variety of backgrounds. 

Each working group within the organization carries out an 18-month collaborative project with the aim of meeting a specific need in the scientific community, through the development of tools, best practices and specifications. The work carried out is in line with the short-term objectives of the Building Immune Digital Twins working group [[17]](#17) (WG BIDT), namely the development of a repository [[18]](#18). Because of the difficulty of measuring the state of the immune system, their development is complex. This calls for strong initiatives, made possible by the WG BIDT.

The main objective is to create a repository using reproducible approaches, in particular by means of Python3 Notebooks enabling :  
- **Retrieval** of `SBML` and `SBML-QUAL` models from the BioModels platform.  
- **Extraction and enrichment** of associated metadata.  
- **Centralization** of enriched models and metadata on a GitHub website.  

## Key Steps

To achieve these objectives, the following key steps will be implemented:

1. **Development of Python3 notebooks to interface with BioModels**  
   - Use libraries such as `bioservices` to access the BioModels platform.  
   - Automate the search, filtering, and downloading of `SBML` and `SBML-QUAL` models.  
   - Enable the extraction of associated metadata (tags, descriptions, ontologies).  

2. **Inspection and enrichment of models and metadata**  
   - Provide a manual or semi-automatic process to enrich the metadata of uncurated `SBML-QUAL` models.  
   - Add additional information such as biological descriptions, tags, and annotations compliant with international standards (e.g., Gene Ontology).  

3. **Centralization and organization of results**  
   - Host enriched models and metadata on a public or private GitHub repository.  
   - Organize files and folders for easy browsing and searching.  
   - Create a dedicated GitHub Page, including a user interface for viewing and downloading models.  

4. **Documentation of tools and resources**  
   - Document the Python3 notebooks and the steps required to run them.  
   - Provide a user guide to help users understand the tools and centralized results.  

5. **Verification and testing of models**  
   - Check the conformity of retrieved models with expected formats (`SBML`/`SBML-QUAL`).  

## Features

To meet the project's objectives, several essential functionalities have been identified. These include interaction with the BioModels platform, metadata processing, result centralization, and documentation.

### Interaction with the BioModels Platform

#### **Description**  
A Python script to interact with the BioModels API, search for, and download computational models in `SBML` or `SBML-QUAL` format. It filters models based on specific keywords or identifiers to ensure relevance to the human immunological response.  

#### **Input Data**  
- Keywords (e.g., "immune response", "cytokines", "T-cell").  
- Selection criteria, such as "manually curated" models.  

#### **Output Data**  
- Models in `SBML` or `SBML-QUAL` format.  
- If manually curated, a `JSON` file containing metadata (format, ID, name, submission date, modification date, authors, source link).  
- If not manually annotated, metadata will be in `CSV` format.  

#### **Tools/Libraries**  
- `bioservices` – A Python library for interacting with BioModels, UniProt, Ensembl, and NCBI APIs.  
- `GetModelsAndMetadata.ipynb` – A Python3 script using `bioservices` to search, download, and structure models.  

### Organization and Structuring of Metadata

#### **Description**  
Automated structuring and organization of retrieved `JSON` metadata using Python3 scripts.  

#### **Input Data**  
- Metadata in `JSON` format.  

#### **Output Data**  
- Structured metadata stored in `JSON` and/or `CSV` format.  

### Annotation and Enrichment of Metadata

#### **Description**  
Manually or semi-automatically inspecting metadata to add relevant information, such as specific tags or FAIR-compliant annotations.  

#### **Input Data**  
- Raw metadata in `JSON` format.  
- Annotation criteria (e.g., additional tags, FAIR tags).  

#### **Output Data**  
- Enriched metadata with specific tags and detailed model descriptions.  
- A `CSV` file if the model is in `SBML-QUAL` format.  

#### **Tools/Libraries**  
- GUI for tagging (e.g., MeSH, Gene Ontology).  

### GitHub Repository Structure

#### **Description**  
A GitHub repository (`immunogit`) has been created to centralize `SBML`/`SBML-QUAL` models and metadata, offering an intuitive interface via GitHub Pages.  

#### **Input Data**  
- Models in `SBML`/`SBML-QUAL` format.  
- Enriched metadata in `JSON` format.  

#### **Output Data**  
An organized GitHub repository containing:  
- A `/models/` folder structured by source:  
  - `/BioModels/` – Models from BioModels.  
  - `/Reactome/` – Models from Reactome.  
  - `/SBGN/` – Models in `SBGN` format.  
- A `/metadata/` folder centralizing metadata:  
  - `models_metadata.json` – Global metadata.  
  - `metadata_BioModels.json` – BioModels-specific metadata.  
- Detailed documentation:  
  - `README.md` in English.  
  - A wiki/user guide explaining the organization and contribution process.  
- A web interface via GitHub Pages:  
  - Browsing and viewing models.  
  - Downloading models and metadata.  

#### **Tools/Libraries**  
- GitHub for repository management and collaboration.  
- GitHub Pages for the user interface.  

### Model Verification and Testing

#### **Description**  
Before integration, retrieved models are checked for format compatibility (`SBML`/`SBML-QUAL`).  

#### **Input Data**  
- Retrieved `SBML`/`SBML-QUAL` files.  

#### **Output Data**  
- Models conforming to defined criteria, or reports on incompatibilities.  

### Documentation

#### **Description**  
Comprehensive documentation in English, including explanations of notebooks, integration steps, and GitHub repository usage.  

#### **Input Data**  
- Python3 notebooks.  
- Model files.  

#### **Output Data**  
- A user guide.  
- Examples of use.  
- Error tracking.  

#### **Tools/Libraries**  
- LaTeX, Markdown.  

## Constraints and Risks

### Functional Constraints

#### **1. Validation and Standards Compliance**  
- `SBML` and `SBML-QUAL` models must follow international standards (e.g., FAIR principles, `SBML` Level 3).  
- Metadata must include annotations conforming to recognized ontologies (e.g., Gene Ontology, MeSH).  

#### **2. Data Retrieval and Management**  
- Models must only be extracted from validated databases like BioModels.  
- Metadata must be structured and enriched using Python3 scripts.  

#### **3. Workflow Requirements**  
Data retrieval must follow a structured workflow:  
1. API search.  
2. Extraction of relevant data.  
3. Validation and enrichment.  
4. Publication on GitHub.  

### Organizational Constraints

#### **1. Human Resources**  
- Training or documentation is required to use the tools (BioModels, etc.).  

#### **2. Deadline Management**  
- Ensure adherence to key project deadlines.  

#### **3. Collaborative Work Organization**  
Each team member contributes generally while specializing in:  
- **Writing & Documentation:** Issa, Hawa, Yasmine, Guillaume.  
- **Coordination:** Issa, Hawa, Yasmine, Guillaume.  
- **Development & Coding:** Issa, Hawa, Yasmine, Guillaume.  
- **GitHub Repository Maintenance:** Guillaume.  

If a member is unavailable for an extended period, task redistribution will be assessed.  

### Technical Constraints

#### **1. Required Tools**  
- Use of BioModels for retrieving models and metadata.  
- Use of GitHub for organization and collaboration.  
- Development of a reusable module (`common_immunogit.py`) for notebooks.  

#### **2. Supported Formats**  
- Models: `SBML` and `SBML-QUAL` only.  
- Metadata: `JSON` format for interoperability.  

#### **3. Development Environment**  
- Work exclusively in Python3-compatible environments.  
- File and script management via a collaborative GitHub repository.  
- Adherence to coding standards and naming conventions. 

## References
<a id="1">[1]</a>
No Author. (n.d.).
Sclérose en plaques (SEP) - Troubles neurologiques.
Édition professionnelle du Manuel MSD. Retrieved February 6, 2025, from https://www.msdmanuals.com/fr/professional/troubles-neurologiques/maladies-démyélinisantes/sclérose-en-plaques-sep

<a id="2">[2]</a>
No Author. (n.d.).
Polyarthrite rhumatoïde (PR) - Troubles musculosquelettiques et du tissu conjonctif.
Édition professionnelle du Manuel MSD. Retrieved February 6, 2025, from https://www.msdmanuals.com/fr/professional/troubles-musculosquelettiques-et-du-tissu-conjonctif/troubles-articulaires/polyarthrite-rhumatoïde-pr

<a id="3">[3]</a>
No Author. (n.d.).
Lupus érythémateux disséminé - Troubles musculosquelettiques et du tissu conjonctif.
Édition professionnelle du Manuel MSD. Retrieved February 6, 2025, from https://www.msdmanuals.com/fr/professional/troubles-musculosquelettiques-et-du-tissu-conjonctif/maladies-rhumatismales-systémiques/lupus-érythémateux-disséminé

<a id="4">[4]</a>
No Author. (n.d.).
Maladies auto-immunes · Inserm, La science pour la santé.
Inserm. Retrieved February 6, 2025, from https://www.inserm.fr/dossier/maladies-auto-immunes/

<a id="5">[5]</a>
No Author. (n.d.).
Sanofi: Dupixent® (dupilumab) approuvé dans le traitement de l'asthme sévère par la Commission européenne.
Sanofi. Retrieved February 6, 2025, from https://www.sanofi.com/fr/media-room/communiques-de-presse/2019/2019-05-07-13-00-00-1818457

<a id="6">[6]</a>
Niarakis, A., Laubenbacher, R., An, G., et al. (2024).
Immune digital twins for complex human pathologies: applications, limitations, and challenges.
npj Systems Biology and Applications, 10(1), 1-14. https://doi.org/10.1038/s41540-024-00450-5

<a id="7">[7]</a>
Ali, F. S., Nguyen, M. H., Hernaez, R., et al. (2025).
AGA Clinical Practice Guideline on the Prevention and Treatment of Hepatitis B Virus Reactivation in At-Risk Individuals.
Gastroenterology, 168(2), 267-284. https://doi.org/10.1053/j.gastro.2024.11.008

<a id="8">[8]</a>
Niarakis, A., Laubenbacher, R., An, G., et al. (2024).
Immune digital twins for complex human pathologies: applications, limitations, and challenges.
npj Systems Biology and Applications, 10(1), 1-14. https://doi.org/10.1038/s41540-024-00450-5

<a id="9">[9]</a>
Malik-Sheriff, R. S., Glont, M., Nguyen, T. V. N., et al. (2020).
BioModels—15 years of sharing computational models in life science.
Nucleic Acids Research, 48(D1), D407–D415. https://doi.org/10.1093/nar/gkz1055

<a id="10">[10]</a>
Glont, M., Nguyen, T. V. N., Graesslin, M., et al. (2018).
BioModels: expanding horizons to include more modelling approaches and formats.
Nucleic Acids Research, 46(D1), D1248–D1253. https://doi.org/10.1093/nar/gkx1023

<a id="11">[11]</a>
Laubenbacher, R., Adler, F., An, G., et al. (2024).
Toward mechanistic medical digital twins: some use cases in immunology.
Frontiers in Digital Health, 6, 1349595. https://doi.org/10.3389/fdgth.2024.1349595

<a id="12">[12]</a>
Chaouiya, C., Bérenguier, D., Keating, S. M., et al. (2013).
SBML qualitative models: a model representation format and infrastructure to foster interactions between qualitative modelling formalisms and tools.
BMC Systems Biology, 7, 135. https://doi.org/10.1186/1752-0509-7-135

<a id="13">[13]</a>
Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016).
The FAIR Guiding Principles for scientific data management and stewardship.
Scientific Data, 3, 160018. https://doi.org/10.1038/sdata.2016.18

<a id="14">[14]</a>
RDA Working Group (2024).
Building Immune Digital Twins - Case Statement.
RDA. https://www.rd-alliance.org/wp-content/uploads/2024/03/Building-Immunge-Digital-Twins-WG_Case_Statement_Revised.pdf

<a id="15">[15]</a>
Laubenbacher, R., Adler, F., & An, G. (2024). 
Toward mechanistic medical digital twins: Some use cases in immunology. 
*Frontiers in Digital Health*, 6, 1349595. https://doi.org/10.3389/fdgth.2024.1349595

<a id="16">[16]</a>
No Author. (n.d.). 
About the RDA. 
*Research Data Alliance*. 
https://www.rd-alliance.org/about-the-rda/

<a id="17">[17]</a>
No Author. (n.d.). 
Building Immune Digital Twins WG Feed. 
*Research Data Alliance*. 
https://www.rd-alliance.org/groups/building-immune-digital-twins-wg/activity/

<a id="18">[18]</a>
No Author. (2024). 
RDA Working Group: Building Immune Digital Twins - Case Statement. 
*Research Data Alliance*. 
https://www.rd-alliance.org/wp-content/uploads/2024/03/Building-Immunge-Digital-Twins-WG_Case_Statement_Revised.pdf
