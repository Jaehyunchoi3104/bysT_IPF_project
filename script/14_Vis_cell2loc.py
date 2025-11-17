# cell2location reference model train

import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import cell2location
from cell2location.utils.filtering import filter_genes
from cell2location.models import RegressionModel

# export reference anndata
adata_ref = sc.read_h5ad("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/sc.h5ad")

# export models
mod = cell2location.models.RegressionModel.load(
    "/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_reference_model",
    adata_ref
)

# export estimated expression in each cluster
if 'means_per_cluster_mu_fg' in adata_ref.varm.keys():
    inf_aver = adata_ref.varm['means_per_cluster_mu_fg'][[f'means_per_cluster_mu_fg_{i}'
                                    for i in adata_ref.uns['mod']['factor_names']]].copy()
else:
    inf_aver = adata_ref.var[[f'means_per_cluster_mu_fg_{i}'
                                    for i in adata_ref.uns['mod']['factor_names']]].copy()
inf_aver.columns = adata_ref.uns['mod']['factor_names']
inf_aver.iloc[0:5, 0:5]

#adata_vis = sc.read_h5ad("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial01.h5ad") 
#adata_vis = sc.read_h5ad("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial02.h5ad") 
adata_vis = sc.read_h5ad("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial03.h5ad") 

intersect = np.intersect1d(adata_vis.var_names, inf_aver.index)
adata_vis = adata_vis[:, intersect].copy()
inf_aver = inf_aver.loc[intersect, :].copy()

# anndata 설정
cell2location.models.Cell2location.setup_anndata(adata=adata_vis, batch_key="sample")

# 모델 정의
mod_vis = cell2location.models.Cell2location(
    adata_vis, cell_state_df=inf_aver,
    N_cells_per_location=30,
    detection_alpha=20
)

# 학습
mod_vis.train(
    max_epochs=10000,
    batch_size=None,
    train_size=1,
    accelerator="cpu"
)

# posterior 추출
adata_vis = mod_vis.export_posterior(
    adata_vis,
    sample_kwargs={'num_samples': 1000, 'batch_size': adata_vis.n_obs}
)
# Save model
#mod_vis.save("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/mod_vis01", overwrite=True)
#mod_vis.save("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/mod_vis02", overwrite=True)
mod_vis.save("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/mod_vis03", overwrite=True)

# Save anndata object with results
adata_vis.write("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial03_c2l.h5ad")

history_df = mod_vis.history["elbo_train"]
first_epoch = history_df.index[0]
first_loss = float(history_df.iloc[0])
final_epoch = history_df.index[-1]
final_loss = history_df.iloc[-1].values[0]  # ELBO 값

print(f"Fiest epoch: {first_epoch}, ELBO loss: {first_loss}")
print(f"Final epoch: {final_epoch}, ELBO loss: {final_loss}")
#history_df.to_csv("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial01_elbo.csv")
#history_df.to_csv("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial02_elbo.csv")
history_df.to_csv("/home/sbblab_test/jaehyunchoi/IPF_cell2loc/IPF_lung_trial03_elbo.csv")
