# Breast Cancer Biomarker Discovery Using Transcriptomic Analysis

## Overview

This project investigates gene expression differences between breast cancer and normal breast tissue using publicly available transcriptomic data from the Gene Expression Omnibus (GEO) database.

The aim of this analysis is to identify differentially expressed genes, characterize molecular patterns associated with breast cancer progression, and explore biological pathways that may contribute to disease development.

The project integrates statistical differential expression analysis, gene annotation, dimensionality reduction, clustering, and functional enrichment analysis to identify potential biomarker candidates and biological mechanisms.

---

## Dataset

**Dataset:** GSE42568  
**Platform:** Affymetrix Human Genome U133 Plus 2.0 Array (GPL570)  
**Organism:** Homo sapiens  

The dataset contains gene expression profiles from:

- 104 breast cancer tissue samples
- 17 normal breast tissue samples

The raw expression data was obtained from the Gene Expression Omnibus (GEO) database and processed for downstream transcriptomic analysis.

---

## Analysis Workflow

The analysis pipeline consisted of the following steps:

1. **Data Acquisition**
   - Downloaded GEO expression dataset using GEOparse.
   - Extracted sample metadata and expression profiles.

2. **Data Processing**
   - Constructed gene expression matrix.
   - Classified samples into cancer and normal groups based on metadata.
   - Prepared data for statistical comparison.

3. **Differential Expression Analysis**
   - Compared gene expression between breast cancer and normal tissue.
   - Applied statistical testing to identify significantly altered genes.
   - Corrected for multiple hypothesis testing using adjusted p-values (False Discovery Rate).

4. **Gene Annotation**
   - Mapped Affymetrix probe IDs to gene symbols and functional annotations using GPL570 annotation data.

5. **Exploratory Analysis**
   - Principal Component Analysis (PCA) to evaluate sample-level expression patterns.
   - Volcano plot visualization of significant expression changes.
   - Hierarchical clustering heatmap of top differentially expressed genes.

6. **Functional Enrichment Analysis**
   - Performed Gene Ontology (GO) enrichment analysis.
   - Identified biological processes associated with altered gene expression.

---

## Key Findings

### Differentially Expressed Genes

A total of:

**6,468 significant genes**

were identified between breast cancer and normal breast tissue after multiple testing correction.

The analysis identified both upregulated and downregulated gene expression patterns.

---

## Biological Insights

### Upregulated Processes

Significant enrichment was observed in pathways associated with:

- Chromatin remodeling
- Chromatin organization
- DNA metabolism
- RNA processing
- Transcriptional regulation

These findings suggest alterations in gene regulatory mechanisms and cellular control processes within breast cancer tissue.

---

### Downregulated Processes

Downregulated genes were associated with:

- Cellular respiration
- Electron transport chain activity
- Fatty acid oxidation
- Mitochondrial ATP synthesis
- Lipid metabolism

Several metabolic genes showed reduced expression, including:

- FABP4
- LPL
- LEP
- RBP4
- CD36
- PLIN1
- PCK1

These results indicate suppression of normal breast metabolic programs during cancer development.

---

## Visualizations

Generated figures include:

- Differential expression volcano plot
- Principal Component Analysis (PCA)
- Clustered heatmap of significant genes
- Gene Ontology enrichment plots

---

## Technologies Used

### Programming Language

- Python

### Data Analysis

- pandas
- numpy
- scipy
- statsmodels
- scikit-learn

### Bioinformatics Tools

- GEOparse
- GSEAPY

### Visualization

- matplotlib
- seaborn

---

## Project Structure
