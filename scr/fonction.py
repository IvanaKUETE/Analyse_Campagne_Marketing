import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



### Pourcentage de valeurs manquantes 

# Fonction pour calculer les valeurs manquantes par colonne
def tableau_valeurs_manquantes(df):
        # Total des valeurs manquantes
        val_manquantes = df.isnull().sum()
        
        # Pourcentage de valeurs manquantes
        pourcentage_val_manquantes = 100 * val_manquantes / len(df)
        
        # Création d'un tableau avec les résultats
        tableau_val_manquantes = pd.concat([val_manquantes, pourcentage_val_manquantes], axis=1)
        
        # Renommage des colonnes
        tableau_val_manquantes_col_renommees = tableau_val_manquantes.rename(
        columns = {0 : 'Valeurs Manquantes', 1 : '% du Total des Valeurs'})
        
        # Tri de tableau par pourcentage de valeurs manquantes de manière décroissante
        tableau_val_manquantes_col_renommees = tableau_val_manquantes_col_renommees[
            tableau_val_manquantes_col_renommees.iloc[:,1] != 0].sort_values(
        '% du Total des Valeurs', ascending=False).round(1)
        
        # Afficher quelques informations récapitulatives
        print ("\nVotre dataframe a sélectionné a " + str(df.shape[1]) + " colonnes.\n"      
            "\nIl y a " + str(tableau_val_manquantes_col_renommees.shape[0]) +
              " colonnes qui ont des valeurs manquantes.\n")
        
        # Renvoyer le dataframe avec les informations manquantes
        return tableau_val_manquantes_col_renommees



### Distribution de variables 

def effectif_freq(dataset, column_name):
    """
    Calcule les effectifs et pourcentages de chaque modalité d'une colonne donnée,
    et retourne un DataFrame avec les résultats.

    :param dataset: DataFrame pandas contenant les données.
    :param column_name: Nom de la colonne à analyser (str).
    :return: DataFrame avec les effectifs et pourcentages par modalité.
    """
    # Vérifier si la colonne existe dans le dataset
    if column_name not in dataset.columns:
        raise ValueError(f"La colonne '{column_name}' n'existe pas dans le DataFrame.")
    
    # Calculer les effectifs et pourcentages
    counts = dataset[column_name].value_counts()
    percentages = round(dataset[column_name].value_counts(normalize=True) * 100, 2)
    
    # Créer un DataFrame pour les résultats
    result_df = pd.DataFrame({
        'Modalité': counts.index,
        'Effectifs': counts.values,
        'Pourcentage': percentages.values
    })
    
    return result_df
