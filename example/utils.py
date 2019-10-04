import numpy as np


def mask_to_rle(mask, name):
    """Convert mask from np.ndarray of shape [L, H, W] to str with Kaggle's run length encoding."""
    n_layers, _, _ = mask.shape
    rle = ''
    for layer in range(n_layers):
        defect_class = layer + 1
        pixels = mask[layer].T.flatten()
        pixels = np.concatenate([[0], pixels, [0]])
        runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
        runs[1::2] -= runs[::2]
        rle += f'{name}_{defect_class},' + ' '.join(str(x) for x in runs) + '\n'
    return rle


def normalize(image):
    IMG_MEAN = (0.485, 0.456, 0.406)
    IMG_STD = (0.229, 0.224, 0.225)
    mean = np.array(IMG_MEAN, dtype=np.float32) * 255.0
    std = np.array(IMG_STD, dtype=np.float32) * 255.0
    denominator = np.reciprocal(std, dtype=np.float32)
    norm_image = (image.astype(np.float32) - mean) * denominator  # image normalisation
    return norm_image
