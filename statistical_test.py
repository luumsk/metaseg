import numpy as np
import scipy.stats as stats
from itertools import combinations
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scikit_posthocs import posthoc_dunn

def check_normal_distribution(data, labels):
    """
    Check if each list in the data follows a normal distribution using the Shapiro-Wilk test.
    Returns a list of booleans indicating normality for each list.
    """
    normality_results = []
    for i, lst in enumerate(data):
        stat, p_value = stats.shapiro(lst)
        is_normal = p_value > 0.05
        normality_results.append(is_normal)
        print(f"{labels[i]}: Shapiro-Wilk test p-value = {p_value:.4f}, Normal = {is_normal}")
    return normality_results

def calculate_significant_differences(data, labels=None):
    """
    Calculate significant differences between the lists.
    """
    normality_results = check_normal_distribution(data, labels)
    all_normal = all(normality_results)
    
    # Flatten the data and create labels
    flat_data = np.concatenate(data)
    labels = np.concatenate([[f"List_{i+1}"] * len(lst) for i, lst in enumerate(data)])
    
    if all_normal:
        # Perform one-way ANOVA
        stat, p_value = stats.f_oneway(*data)
        print(f"ANOVA test p-value = {p_value:.4f}")
        
        if p_value < 0.05:
            # If significant, perform Tukey's HSD test
            print("Performing Tukey's HSD test for pairwise comparisons...")
            tukey_result = pairwise_tukeyhsd(endog=flat_data, groups=labels, alpha=0.05)
            print(tukey_result)
        else:
            print("No significant differences found with ANOVA.")
            
    else:
        # Perform Kruskal-Wallis test
        stat, p_value = stats.kruskal(*data)
        print(f"Kruskal-Wallis test p-value = {p_value:.4f}")
        
        if p_value < 0.05:
            # If significant, perform Dunn's test
            print("Performing Dunn's test for pairwise comparisons...")
            dunn_result = posthoc_dunn(data, p_adjust='bonferroni')
            print(dunn_result)
        else:
            print("No significant differences found with Kruskal-Wallis test.")


dice_scores = {
    "nnunet_tversky": [
        0.8198692146,
        0.8165887689,
        0.8105517141,
        0.8081718826,
        0.8119824638,
    ],
    "segresnet": [
        0.8142133343,
        0.8118873159,
        0.7957310756,
        0.8064948842,
        0.797247452,
    ],
    "nnunet_default": [
        0.8225347525,
        0.8158033478,
        0.804618464,
        0.8048596011,
        0.8105946943,
    ]
}

lists = np.array(list(dice_scores.values()))
print(lists.shape)
calculate_significant_differences(lists, labels=list(dice_scores.keys()))
