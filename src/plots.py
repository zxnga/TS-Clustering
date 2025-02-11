import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, inconsistent
from scipy.cluster.hierarchy import dendrogram

def plot_inconsistency_score(data, method='ward', depth=2):
    """
    Plots the inconsistency scores
    for different numbers of clusters based on hierarchical clustering.

    Parameters:
    -----------
    data : array-like
        The data used for hierarchical clustering (e.g., a 2D numpy array or pandas DataFrame).
    method : str, optional
        The linkage method to use for clustering (default is 'ward').
    depth : int, optional
        The depth parameter for calculating inconsistency (default is 2).

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The matplotlib figure object containing the plot.
    """
    Z = linkage(data, method=method)
    inconsistencies = inconsistent(Z, depth)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(range(1, len(inconsistencies) + 1), inconsistencies[:, 2], marker='o')
    ax.set_xlabel('Number of Clusters')
    ax.set_ylabel('Inconsistency Score')
    ax.set_title('Inconsistency Score for Different Numbers of Clusters')
    
    fig.tight_layout()
    # plt.show()
    return fig

import matplotlib.pyplot as plt

def plot_clusters_in_color(data, cluster_assignments, colormap, 
                           title='Clustering 3 groups',
                           xlabel='Time (Hour)', ylabel='Value',
                           figsize=(7,4)):
    """
    Plots the transposed data with each time series colored according to its cluster assignment.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the data. When transposed, each column corresponds to a different
        time series that will be colored based on its cluster.
    cluster_assignments : array-like
        Cluster labels for each series. The order should match the order of data.columns.
    colormap : list or array-like
        A list of colors where each index corresponds to a cluster. For example,
        ['blue', 'orange', 'green'].

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The matplotlib figure object.
    """
    colors = [colormap[int(cl)] for cl in cluster_assignments]
    fig, ax = plt.subplots(figsize=figsize)

    data.T.plot(legend=False, color=colors, title=title, ax=ax)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # plt.show()
    return fig

def plot_dendrogram(linkage_matrix, labels, 
                    title="Dendrogram of Time Series Clustering",
                    xlabel="Time Series", ylabel="Distance",
                    figsize=(10, 6)):
    """
    Plots a dendrogram from a linkage matrix using the provided labels.

    Parameters:
    -----------
    linkage_matrix : array-like
        The linkage matrix resulting from a hierarchical clustering (e.g., from scipy.cluster.hierarchy.linkage).
    labels : array-like
        The labels for each data point. For instance, if you are clustering time series,
        you might pass data.index or a list of time series names.

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The matplotlib figure object containing the dendrogram.
    """
    fig, ax = plt.subplots(figsize=figsize)
    dendrogram(linkage_matrix, labels=labels, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # plt.show()
    
    return fig