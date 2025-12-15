# churn-ml
Project-based learning for Machine Learning

## Scope and Learning Plan
- **Dataset:** Telco Customer Churn (`openml id=45568`), tabular, binary target.
- **Primary goal:** Learn ML by comparing diverse models, not just finishing quickly.
- **Baselines (sklearn, all via Pipeline + Stratified CV):** Logistic Regression, Decision Tree, Random Forest/Gradient Boosting, SVM (RBF or linear), kNN. Report ROC-AUC, PR-AUC, F1 (positive class), confusion matrix, and optionally calibration curves.
- **Hyperparameter tuning:** Small, educational `RandomizedSearchCV` grids to see variance and inductive bias effects. Log mean/std CV scores and settings.
- **PyTorch MLP:** Start with preprocessed tabular features (one-hot + scaled). Train a small MLP with batching, optimizer choice (SGD vs Adam/AdamW), early stopping. Later, try embeddings for categorical features.
- **Unsupervised explorations:** Clustering (k-means, GMM/EM) to inspect churn by cluster; dimensionality reductions (PCA/ICA; t-SNE/UMAP for visualization); feature importance/selection (tree/permutation-based).
- **Reporting habit:** For each experiment, write a short entry in `report/report.md` (hypothesis → setup → metrics → takeaway) and save plots to `report/figures/` (ROC/PR curves, confusion matrices, calibration, learning curves).
- **Data discipline:** Use consistent train/val/test splits (stratified), avoid leakage, and keep preprocessing inside the pipeline so CV/test use the exact same transforms.
