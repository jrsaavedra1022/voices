from tqdm import tqdm

def progress_bar(iterable, total=None, description=None):
    """
    Muestra una barra de progreso usando tqdm.
    
    Args:
        iterable: objeto iterable
        total (opcional): cantidad total de elementos
        description (opcional): descripción de la barra
    """
    return tqdm(iterable, total=total, desc=description)