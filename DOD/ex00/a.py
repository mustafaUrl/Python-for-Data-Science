import numpy as np

def quartiles_numpy(data):
    """
    NumPy kullanarak %25 ve %75 çeyrek değerlerini hesaplar.
    
    Parametreler:
    data (list veya np.ndarray): Çeyrek hesaplanacak veri.

    Returns:
    tuple: %25 ve %75 çeyrek değerleri.
    """
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    return Q1, Q3



from scipy import stats

def quartiles_scipy(data):
    """
    SciPy kullanarak %25 ve %75 çeyrek değerlerini hesaplar.
    
    Parametreler:
    data (list veya np.ndarray): Çeyrek hesaplanacak veri.

    Returns:
    tuple: %25 ve %75 çeyrek değerleri.
    """
    Q1 = stats.scoreatpercentile(data, 25)
    Q3 = stats.scoreatpercentile(data, 75)
    return Q1, Q3

# Test için farklı veri
data4 = [1, 42, 360, 11, 64]
print(quartiles_numpy(data4))  # Q1 ve Q3 ondalık değerler içerecek
print(quartiles_scipy(data4))   # Aynı şekilde burada da
