![image](raw/logo.png)

# ImmunoGIT Specifications document

## Biological introduction
This project lies at the interface between computational biology and immunology. By bridging these two fields, the construction of Immune Digital Twins (IDTs) representing dynamic virtual representations of the human immune system will enable us to understand and predict how the immune system responds to a variety of situations.

As the science that studies the immune system and its regulation, immunology represents a real stake in the treatment of autoimmune diseases (AIDs) such as multiple sclerosis [@noauthor_sclerose_nodate], rheumatoid arthritis [@noauthor_polyarthrite_nodate], or systemic lupus erythematosus [@noauthor_lupus_nodate], which affect millions of people worldwide, often with severe complications. Both public and private laboratories (INSERM [@noauthor_maladies_nodate] and Sanofi [@noauthor_sanofi_nodate]) are working in this area, offering complex treatments such as biotherapies and immunosuppressants. DDDTs (Digital Drug Development Twins) could accelerate this pharmaceutical development process while reducing costs, as DTs enable the impact of treatments to be modeled at various levels, including the identification of therapeutic targets and drug validation [@niarakis_immune_2024].

The wide diversity of actors involved in the immune system and the resulting pathologies (which vary in severity) call for the use of omics approaches, which enable in-depth analysis of the underlying molecular mechanisms. These novel approaches to medicine are paving the way for targeted and personalized therapies.
However, the use of immunosuppressants is not a harmless practice: for instance, according to the American Gastroenterology Association (AGA), reactivation of hepatitis B is a major risk for some patients [@ali_aga_2025]. The AGA has updated its recommendations: the decision between antiviral prophylaxis or clinical follow-up depends on the level of risk and the type of treatment. In addition, the regulatory and ethical aspects associated with the use of DTs in healthcare settings are crucial: Food and Drug Administration (FDA) and European Medicines Agency (EMA) require rigorous standards to be met in order to be considered as medical devices. Ethical issues, notably relating to data protection, will also need to be swept under the carpet [@niarakis_immune_2024].

A wide range of actors in fields such as proteomics, metabolomics and (spatial) transcriptomics are involved, such as the study of gene expression regulation and spatial transcriptomics, which maps the expression of genes involved in a tissue, and could help prevent these IAMs. 

Computational models are essential tools for simulating and analyzing the complex mechanisms of the immune system. These models enable molecular and cellular interactions to be reproduced, making it easier to optimize therapeutic strategies. However, their development is often hampered by the absence of well-structured repositories to organize and share these resources. Databases such as BioModels [@malik-sheriff_biomodels15_2020][@glont_biomodels_2018] host biological models in Systems Biology Markup Language [@laubenbacher_toward_2024] (SBML) format, designed to represent and exchange models of biochemical reactions.
We'll also be using files in Systems Biology Marked Up Language-qualitative [@chaouiya_sbml_2013] ie SBML-qual, an extension of SBML that enables biological systems to be modeled qualitatively using a Boolean and logical approach. It allows systems to be modeled without the need for precise quantitative data, making it particularly well suited to the study of regulatory and signaling networks. Thanks to its interoperability with different software packages, SBML-QUAL facilitates the collaborative exchange, analysis and development of models, thus contributing to a better standardization of qualitative approaches in systems biology.

But models specific to the immune system remain scattered and insufficiently organized. This project aims to fill this gap by creating a dedicated repository, in line with a roadmap derived from the state of the art [@wilkinson_fair_2016]. In accordance with the FAIR [@noauthor_rda_2024] principles (Findable, Accessible, Interoperable, Reusable), the repository will be modular, practical for group work, and have a robust infrastructure.

This repository will centralize and annotate relevant computational models, while making them accessible for applications such as the construction of immune digital twins. By building on existing resources and integrating with the short-term goals of international collaborative efforts, this project will help lay the foundations for a scalable digital infrastructure, essential for meeting the challenges of precision medicine.

## Host Team
This project is led by Professor Anna Niarakis and Engineer Nicolas Ricort-Teixidor, both of whom work in the Computational Systems Biology Pole at the Toulouse Center for Integrative Biology (CBI).

The CBI is an international multidisciplinary research structure dedicated to the understanding of how living organisms function, using what are known as integrative and multi-scale approaches. Made up of several laboratories, including the host laboratory Molecular, Cellular and Developmental Biology (MCD), its research themes cover a wide range of fields addressing major health-related societal issues. 

More specifically, in the context of this project, it is involved in CoSysBio [(Computational Systems Biology for complex human diseases)](https://cbi-toulouse.fr/eng/equipe-niarakis), which develops integrative approaches combining mathematics, computer science and bioinformatics to identify new therapeutic targets and model complex pathologies. Immunological digital twins are a major challenge: hybrid models combining artificial intelligence and mechanistic networks could predict the evolution of diseases and refine therapeutic strategies in personalized medicine [@laubenbacher_toward_2024]. Historically, a digital twin is an organized set of adaptable models that emulate the behaviors of a given physical system (a term derived from “industry”) using data obtained throughout its life cycle. It is therefore a dynamic model, which can have several levels of complexity (known as “digitization”). They help optimize diagnosis and treatment (dose), particularly for diseases involving the immune system. 

The ImmunoGIT initiative will contribute to this by structuring and sharing models dedicated to these immune pathologies.

More broadly, the project will benefit from the support of the Research Data Alliance [@noauthor_about_nodate] (RDA). Created in 2013, this international organization is dedicated to the creation of standards and the interoperability of biological data. It acts as a bridge between researchers and clinicians from a variety of backgrounds. 

Each working group within the organization carries out an 18-month collaborative project with the aim of meeting a specific need in the scientific community, through the development of tools, best practices and specifications. The work carried out is in line with the short-term objectives of the Building Immune Digital Twins working group [@noauthor_building_nodate] (WG BIDT), namely the development of a repository [@noauthor_rda_2024]. Because of the difficulty of measuring the state of the immune system, their development is complex. This calls for strong initiatives, made possible by the WG BIDT.

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
::: {#refs}
:::


::: center
**ImmunoGIT**\
Création d'un référentiel de modèles et de métadonnées concernant les
réponses du système immunitaire humain\
:::

------------------------------------------------------------------------

\
:::

::: center
[Université de Toulouse]{.smallcaps}\
[M1 Bioinformatique et Biologie des Systèmes]{.smallcaps}
:::

::: center
::: flushleft
Guillaume Souède\
Issa Kerima Khalil\
Mamadou Hawa Balde\
Yasmine Boukadida
:::

::: flushright
2024 --- 2025\
:::
:::

# Contexte du projet

## Introduction biologique

Ce projet s'inscrit à l'interface de la biologie computationnelle et de
l'immunologie. Faisant le pont entre ces deux domaines, la construction
de jumeaux numériques immunitaires (IDT ou Immune Digital Twins) comme
représentations virtuelles dynamiques du système immunitaire humain
permettra de comprendre et prédire ses réponses face à des situations
variées.\
L'immunologie, science qui étudie le système immunitaire et sa
régulation, représente un véritable enjeu dans le traitement des
maladies auto-immunes (MAI) telles que la sclérose en plaques\[1\], la
polyarthrite rhumatoïde\[2\] ou le lupus érythémateux systémique\[3\],
qui affectent des millions de personnes dans le monde et entraînent des
complications sévères. Des laboratoires publics comme privés
(INSERM\[4\] et Sanofi\[5\]) évoluent dans ce domaine et proposent des
traitements complexes comme les biothérapies et les immunosuppresseurs.
Les DDDT (Digital Drug Development Twins) pourraient accélérer ce
processus de développement pharmaceutique tout en réduisant les coûts,
les DT permettant de modéliser l'impact des traitements à différents
niveaux, dont l'identification de cibles thérapeutiques et la validation
des médicaments. \[6\]\
La grande diversité des acteurs impliqués dans l'immunité et des
pathologies qui en découlent (de sévérité variable) justifient le
recours aux approches omiques, qui permettent une analyse approfondie
des mécanismes moléculaires sous-jacents. Ces approches nouvelles de la
médecine ouvrent la voie à des thérapeutiques ciblées / personnalisées.
Pourtant, la prise d'immunosuppresseurs n'est pas une pratique anodine :
par exemple, selon l'association américaine de gastroentérologie (AGA),
la réactivation de l'hépatite B constitue un risque majeur pour certains
patients\[8\]. L'AGA a mis à jour ses recommandations : la décision
entre prophylaxie antivirale ou suivi clinique dépend du niveau de
risque et du type de traitement. De plus, les aspects réglementaires et
éthiques associés à l'utilisation des DT en santé sont cruciaux : Food
and Drug Administration (FDA) et European Medicines Agency (EMA)
requièrent des normes rigoureuses pour être considérés comme des
dispositifs médicaux. Des questions éthiques, notamment relatives à la
protection des données, devront être balayées. \[6\]\
Un nombre varié d'acteurs de thématiques comme la protéomique, la
métabolomique et la transcriptomique (spatiale) s'y intègrent, comme
l'étude des régulations de l'expression génétique et la transcriptomique
spatiale, véritable cartographie de l'expression des gènes impliqués
dans un tissu, et pourraient permettre une prévention de ces MAI.\
Les modèles computationnels sont des outils essentiels pour simuler et
analyser les mécanismes complexes du système immunitaire. Ces modèles
permettent de reproduire les interactions moléculaires et cellulaires,
facilitant ainsi l'optimisation des stratégies thérapeutiques.
Cependant, leur développement est souvent freiné par l'absence de
référentiels bien structurés pour organiser et partager ces ressources.
Des bases de données comme BioModels\[9\] \[10\] hébergent des modèles
biologiques au format Systems Biology Markup Language\[11\] (SBML) conçu
pour représenter et échanger des modèles des réactions biochimiques.
Mais les modèles spécifiques au système immunitaire y restent dispersés
et insuffisamment organisés. Ce projet vise à combler cette lacune en
créant un référentiel dédié, conforme à une feuille de route issue de
l'état de l'art \[12\]. Ainsi, le référentiel sera notamment conforme
aux principes FAIR\[13\](Findable, Accessible, Interoperable, Reusable)
modulable, apte au travail en groupe et d'infrastructure robuste.\
Ce référentiel centralisera et annotera les modèles computationnels
pertinents, tout en les rendant accessibles pour des applications comme
la construction de jumeaux numériques immunitaires. En s'appuyant sur
les ressources existantes et en s'intégrant aux objectifs à court terme
d'efforts collaboratifs internationaux, ce projet contribuera à poser
les bases d'une infrastructure numérique évolutive, essentielle pour
répondre aux enjeux de la médecine de précision.\

## Équipe d'accueil

Ce projet est porté par le Professeur des Universités Anna Niarakis et
l'Ingénieur d'Études Nicolas Ricort - Teixidor, en exercice au sein du
Pôle de Biologie Computationnelle des Systèmes du Centre de Biologie
Intégrative de Toulouse (CBI).\
Le CBI est une structure de recherche multidisciplinaire internationale
axée sur la compréhension du fonctionnement des organismes vivants à
travers des approches dites intégratives et multi-échelles. Composé de
plusieurs laboratoires, dont le laboratoire hôte Biologie Moléculaire,
Cellulaire et du Développement (MCD), ses thématiques de recherche
couvrent des domaines variés répondant à des enjeux sociétaux majeurs
liés à la santé. Mais, à l'égard de ce projet plus particulièrement, il
est impliqué dans CoSysBio
(<https://cbi-toulouse.fr/eng/equipe-niarakis>) (Computational Systems
Biology for complex human diseases), qui développe des approches
intégratives combinant mathématiques, informatique et bioinformatique
pour identifier de nouvelles cibles thérapeutiques et modéliser des
pathologies complexes. Les jumeaux numériques immunologiques en sont un
enjeu majeur : des modèles hybrides associant intelligence artificielle
et réseaux mécanistiques pourraient prédire l'évolution des maladies et
affiner les stratégies thérapeutiques en médecine personnalisée \[12\].
Historiquement, un jumeau numérique est un ensemble organisé de modèles
adaptables qui émulent les comportements d'un système physique (terme
issu de l' "industrie") donné grâce à des données obtenues au long de
son cycle de vie. C'est donc un modèle dynamique, qui peut avoir
plusieurs niveaux de complexité (dits "de numérisation"). L'initiative
ImmunoGit y contribuera en structurant et partageant des modèles dédiés
à ces pathologies immunitaires.\
Plus largement, le projet bénéficiera du soutien de la Research Data
Alliance\[14\] (RDA). Cette organisation internationale créée en 2013
dédiée à la création de standards et à l'interopérabilité des données
biologiques est une passerelle entre chercheurs et cliniciens de profils
variés, axée sur la création de standards et l'interopérabilité des
données biologiques.\
Chaque groupe de travail qui la compose mène un projet collaboratif de
18 mois avec pour objectif, au travers du développement d'outils, de
bonnes pratiques et spécifications, de répondre à un besoin précis de la
communauté scientifique. Le travail réalisé s'intègre aux objectifs à
court terme, à savoir le développement d'un référentiel \[15\], du
groupe de travail Building Immune Digital Twins\[16\] (WG BIDT). Les
jumeaux numériques immunitaires (IDTs) sont une application directe de
la modélisation dans le domaine médical : ils permettent d'optimiser le
diagnostic et les traitements (dose), particulièrement pour les maladies
impliquant le système immunitaire. De par la difficulté à mesurer l'état
du système immunitaire, leur développement est complexe. Cela nécessite
des initiatives fortes, rendues possibles par le WG BIDT.\

# Description générale

## Sujet d'étude

Au cours du projet ImmunoGIT, il convient de répondre à des besoins
fondamentaux en biologie computationnelle et en immunologie au travers
d'une ressource ouverte et interopérable permettant la collecte et
l'organisation (par des étiquettes ou "tags") des modèles informatiques
pertinents pour les études sur le système immunitaire humain. Cette
ressource contribuera au développement d'outils nécessaires à la
création de jumeaux numériques immunitaires.\

## Objectifs

Le projet s'inscrit dans le domaine de la bioinformatique et des
sciences des systèmes. Il a pour ambition de développer un référentiel
FAIR modulable regroupant des modèles computationnels et leurs
métadonnées, spécifiquement orientés vers les réponses du système
immunitaire humain. Il répond ainsi à un besoin croissant en médecine de
précision et en recherche biomédicale, notamment dans le contexte des
jumeaux numériques immunitaires (Immune Digital Twins).\
Le référentiel sera constitué de modèles extraits de la section
manuellement curée de la base de données BioModels, qui est reconnue
pour sa qualité et sa pertinence scientifique. Ces modèles, décrits dans
des formats standards tels que SBML (Systems Biology Markup Language) et
SBML-QUAL (Systems Biology Markup Language - Qualitative Models)
permettent de simuler des processus biologiques complexes, comme les
interactions cellulaires, les cascades de signalisation et les
mécanismes de régulation.\
Le développement d'un tel référentiel contribuera à la recherche sur les
maladies impliquant le système immunitaire, comme les maladies
auto-immunes, les infections virales et bactériennes, ou encore les
cancers. Il servira également de base pour l'élaboration de simulations
prédictives et d'approches personnalisées dans le cadre des jumeaux
numériques immunitaires.\
L'objectif principal est de créer un référentiel en utilisant des
approches reproductibles au travers notamment de Notebooks Python
permettant :

-   De récupérer des modèles SBML et SBML-QUAL depuis la plateforme
    BioModels.

-   D'extraire et d'enrichir les métadonnées associées.

-   De centraliser les modèles et métadonnées enrichis sur un site
    GitHub.

Pour atteindre ces objectifs, plusieurs étapes clés seront mises en
place :

1.  Développement de Notebooks Python3 pour l'interaction avec BioModels
    :

    -   Utiliser des bibliothèques comme bioservices pour accéder à la
        plateforme BioModels.

    -   Automatiser la recherche, le filtrage et le téléchargement des
        modèles SBML et SBML-QUAL.

    -   Permettre l'extraction des métadonnées associées (tags,
        descriptions, ontologies).

2.  Inspection et enrichissement des modèles et métadonnées :

    -   Prévoir un processus manuel ou semi-automatique pour enrichir
        les métadonnées des modèles partiellement annotés.

    -   Ajouter des informations supplémentaires telles que des
        descriptions biologiques, des tags, et des annotations conformes
        aux standards internationaux (par exemple, Gene Ontology).

3.  Centralisation et organisation des résultats :

    -   Héberger les modèles et les métadonnées enrichis sur un dépôt
        GitHub public ou privé.

    -   Organiser les fichiers et les dossiers pour faciliter la
        navigation et la recherche.

    -   Créer une page GitHub dédiée via GitHub Pages, comprenant une
        interface utilisateur pour visualiser et télécharger les
        modèles.

4.  Documentation des outils et ressources :

    -   Documenter le fonctionnement des Notebooks Python3 et les étapes
        nécessaires pour les exécuter.

    -   Fournir un guide utilisateur pour accompagner la prise en main
        des outils et la compréhension des résultats centralisés.

5.  Validation et tests des modèles :

    -   Vérifier la conformité des modèles récupérés avec les formats
        attendus (SBML/SBML-QUAL).

# Fonctionnalités

Pour répondre aux objectifs du projet, plusieurs fonctionnalités
essentielles ont été identifiées et intégrées. Ces fonctionnalités
couvrent l'interaction avec la plateforme BioModels, le traitement des
métadonnées, la centralisation des résultats et la documentation.

## Interaction avec la plateforme BioModels

#### Description

Un script Python permettant d'interagir avec l'API de BioModels pour
rechercher et télécharger des modèles computationnels au format SBML ou
SBML-QUAL. Il filtre les modèles en fonction de mots-clés ou
d'identifiants spécifiques pour garantir leur pertinence par rapport aux
réponses immunitaires humaines.

#### Données en entrée

Mots-clés (exemple : \"immune response\", \"cytokines\", \"T-cell\").
Critères de sélection, comme les modèles \"manually curated\".

#### Données en sortie

Les fichiers de modèles générés seront au format SBML ou SBML-QUAL et
seront accompagnés, lorsqu'ils ont fait l'objet d'une curation manuelle,
d'un fichier JSON contenant les métadonnées associées. Le fichier JSON
inclura plusieurs informations essentielles, telles que le format du
modèle, son identifiant unique, son nom, ainsi que les dates de
soumission et de dernière modification. Il précisera également le(s)
nom(s) du ou des auteurs et fournira un lien vers la source du modèle.
Lorsque le fichier n'a pas fait l'objet d'une annotation manuelle, le
fichier sera au format CSV et comportera les mêmes informations.

#### Outil/Bibliothèque

BioServices\[16\], GetModelsAndMetadata.ipynb adapté de
libOmexMeta\[17\].

##### `bioservices`

Une bibliothèque Python qui permet d'interagir avec plusieurs API
bioinformatiques, comme celles de BioModels, UniProt, Ensembl, ou NCBI.
Elle simplifie l'accès aux données, permet d'automatiser le
téléchargement de modèles et l'extraction de métadonnées associées,
facilitant ainsi les tâches de récupération et de traitement des
informations biologiques.

##### `GetModelsAndMetadata.ipynb`

Un script Python qui utilise bioservices pour rechercher, télécharger et
structurer des modèles biologiques au format SBML ou SBML-QUAL à partir
de l'API BioModels.

## Organisation et structuration des métadonnées

#### Description

Structuration et organisation des métadonnées JSON récupérées avec les
modèles. Processus automatisé via des scripts Python 3.

#### Données en entrée

Métadonnées au format JSON.

#### Données en sortie

Métadonnées structurées, conservées en JSON et CSV.

## Annotation et enrichissement des métadonnées 

#### Description

Cette fonctionnalité consiste à inspecter manuellement ou
semi-automatiquement les métadonnées pour ajouter des informations
pertinentes, telles que des tags spécifiques ou des annotations
conformes aux principes FAIR. L'annotation suivra les recommandations du
standard MIRIAM\[18\] (Minimum Information Required In the Annotation of
Models) afin d'assurer l'interopérabilité et la réutilisation des
modèles.

#### Données en entrée

Métadonnées brutes au format .json récupérées avec les modèles. Fichiers
JSON des métadonnées structurées. Critères d'annotation tels que :

-   des Tags supplémentaires (par exemple : Tcell, Immuno-oncology).

-   des Balises FAIR.

#### Données en sortie

Métadonnées enrichies contenant :

-   Tags spécifiques au domaine d'étude.

-   Descriptions plus détaillées des mécanismes modélisés.

#### Outils/Bibliothèques

Interface graphique pour étiquetage, tags (par exemple : MeSH, Gene
Ontology).

## Création du référentiel GitHub

#### Description

Un dépôt GitHub intitulé \"immunogit\" est créé pour centraliser les
modèles SBML/SBML-QUAL et leurs métadonnées enrichies, tout en offrant
une interface intuitive via GitHub Pages. Le dépôt est structuré de
manière à faciliter la navigation, avec une organisation claire des
modèles et de leurs métadonnées.

#### Données en entrée

Modèles au format SBML/SBML-QUAL. Métadonnées enrichies au format JSON.

#### Données en sortie

Un référentiel GitHub[@gitHubLink] organisé contenant :

-   Un dossier principal `/models/` structuré par source des modèles :

    -   `/BioModels/` : Modèles issus de BioModels.

    -   `/Reactome/` : Modèles issus de Reactome.

    -   `/SBGN/` : Modèles au format SBGN.

-   Un dossier `/metadata/` centralisant les métadonnées, avec :

    -   `models_metadata.json` : Métadonnées globales pour tous les
        modèles.

    -   `metadata_BioModels.json` : Métadonnées spécifiques aux modèles
        BioModels.

    -   `metadata_Reactome.json` : Métadonnées spécifiques aux modèles
        Reactome.

-   Une documentation détaillée avec :

    -   Un `README.md` en anglais, qui est au moins la traduction
        complète du présent cahier des charges, et décrivant le projet
        et les instructions d'utilisation.

    -   Un wiki/guide utilisateur expliquant l'organisation et la
        contribution.

-   Une interface web via GitHub Pages permettant :

    -   La navigation et la visualisation des modèles.

    -   Le téléchargement des modèles et de leurs métadonnées associées.

#### Outils/Bibliothèques

GitHub pour la gestion du dépôt et la collaboration. GitHub Pages pour
l'interface utilisateur.

## Vérification des modèles

#### Description

Avant leur intégration dans le référentiel, les modèles téléchargés sont
vérifiés pour s'assurer qu'ils sont compatibles avec les filtres
appliqués et conformes aux formats SBML/SBML-QUAL.

#### Données en entrée

Fichiers SBML/SBML-QUAL récupérés.

#### Données en sortie

Modèles conformes aux critères définis ou signalement des éventuelles
incompatibilités.

## Documentation

# Contraintes et risques

## Contraintes fonctionnelles 

#### 1. Circuit de validation et conformité aux standards

Les modèles SBML et SBML.qual doivent respecter les standards
internationaux (ex. principes FAIR, SBML Level 3). Les métadonnées
associées doivent inclure des annotations conformes aux ontologies
reconnues (par exemple, Gene Ontology, MeSH). Les fichiers doivent
passer par une phase de validation technique (outils comme COPASI,
CellDesigner).

#### 2. Récupération et gestion des données

Les modèles doivent être extraits uniquement depuis des bases de données
validées et fiables comme BioModels. Les métadonnées doivent être
récupérées, structurées et enrichies automatiquement ou semi-
automatiquement via des scripts Python adaptés.

#### 3. Workflow spécifique

La récupération des données (modèles et métadonnées) doit suivre un
workflow défini pour garantir la cohérence :

-   Recherche via API.

-   Extraction des données pertinentes.

-   Validation et enrichissement.

-   Publication sur GitHub.

## Contraintes organisationnelles 

#### 1. Ressources humaines

Nécessité de formations ou d'une documentation approfondie afin
d'utiliser les outils (Biomodels, etc.).

#### 2. Gestion des délais

Respect des délais clés pour rendre les documents et coordination des
réunions d'avancement.

#### 3. Organisation du travail collaboratif

Chaque membre du projet doit être capable de contribuer de manière
générale aux thématiques abordées, tout en développant une
spécialisation/affinité dans un ou plusieurs des domaines suivants :

-   **Écriture et documentation** : Issa, Hawa, Yasmine et Guillaume.

-   **Initiative et coordination** : Issa, Hawa, Yasmine et Guillaume.

-   **Développement et codage** : Issa, Hawa, Yasmine et Guillaume.

-   **Suivi et mise à jour du dépôt GitHub** : Guillaume.

Il est de la responsabilité de chaque membre de veiller à une
organisation et une communication efficaces au sein du groupe de
travail. En cas d'indisponibilité prolongée d'un membre de l'équipe, une
réévaluation rapide de la répartition des tâches doit être effectuée par
les autres.

## Contraintes techniques

#### 1. Obligation d'utiliser des outils spécifiques

Utilisation de la plateforme BioModels pour récupérer les modèles et
métadonnées. Utilisation de GitHub pour centraliser et organiser les
livrables. Développement d'un script sous forme de module réutilisable
(`common_immunogit.py`) permettant son appel via l'instruction `import`
dans tous les Notebook.

#### 2. Formats et standards

Les modèles et formats sont limités :

-   Modèles uniquement au format SBML et SBML.qual.

-   Métadonnées au format JSON pour garantir leur interopérabilité.

**Organisation de l'environnement de développement** : Travail
exclusivement sur des environnements compatibles Python3. Gestion des
fichiers et scripts sur un dépôt GitHub collaboratif. Règles de codage
et conventions de nommage.
