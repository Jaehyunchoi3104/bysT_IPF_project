[Project Name] Byst_IPF_proj
[Paper Name] Type 2 innate-like pathogenic function of PD-1high CD4 T cells aggravate pulmonary fibrosis
[Created] 2025-04-17
[Owner] Jaehyun Choi

[Data]
- raw_data/: GSE295241
- processed: filtered and normalized with Scanpy and R,  see 01_preprocessing.ipynb

[In vivo mouse data]
1. Preprocessing: [[01_preprocessing.ipynb]] [conda env conda1]
2. Clustering: 02_clustering.ipynb [conda env conda1]
3. DEG Analysis: 03_DEG_analysis.md [R] 
GO and KEGG analyses were performed using differentially expressed genes (log₂ fold change > 0.58, adjusted P-value < 0.05) through the DAVID functional annotation tool
4. Velocity analysis: 04_deepvelo.ipynb [conda env conda2 and conda3] , 08_monocle3.Rmd 
5. psuedotime and Fate probabilities analysis: 05_fate_anlaysis.ipynb [conda env conda4]
6. SCENIC_TF interaction analysis : 06_pySCENIC.md and 07_SCENIC_analysis.ipynb [conda env conda1]
7. Bulk RNA seq analysis (Spleen vs Lung) :bulkRNAseq/

[Public human IPF data] _GSE122960,GSE135893,GSE136831
1. Preprocessing: 11_IPF_merging_preprocessing.ipynb [conda env conda1]
2. Whole data analysis: 12_IPF_clustering.ipynb [conda env conda1]
3. CD4 + T cell analysis: 13_IPF_CD4T_analysis.md [conda env conda1]
GO and KEGG analyses were performed using differentially expressed genes (log₂ fold change > 0.58, adjusted P-value < 0.05) through the DAVID functional annotation tool
4. deconvolution analysis: 
5. Visium preprocessing: 
6. Visium distance correlation analysis : 



[Note]
conda environments in env/
