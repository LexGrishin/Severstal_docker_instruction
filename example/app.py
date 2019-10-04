import os
import cv2
import torch
import numpy as np
from glob import glob
from tqdm import tqdm

from model import DummyModel
from utils import mask_to_rle, normalize

from timer import timer


@timer
def app(test_img_path, submission_path, device):
    """Wraps inference code for Efficiency scoring.

        Parameters
        ----------
        test_img_path : str
            Path to test images.
        submission_path : str
            Path to save `submission.csv`.
        device : str
            Device to run model on.
    """
    ########################################
    #         place your code here         #
    ########################################
    model = DummyModel().to(device)
    weights = torch.load('model_weights/dummy_weights.pkl',
                         map_location=device)
    model.load_state_dict(weights)

    img_paths = glob(os.path.join(test_img_path, '*'))

    submission = ['ImageId_ClassId,EncodedPixels\n']
    model.eval()
    with torch.no_grad():
        for path in tqdm(img_paths):
            name = path.split('/')[-1]
            image = normalize(cv2.imread(path, cv2.IMREAD_COLOR))
            image = torch.from_numpy(image.transpose(2, 0, 1))
            score = model(image.unsqueeze(0).to(device))
            mask = (score.cpu().numpy()[0] > 0.5).astype(np.uint8)
            rle = mask_to_rle(mask, name)
            submission.append(rle)
    with open(os.path.join(submission_path, 'dummy_submission.csv'), 'w') as f:
        f.write(''.join(submission))
    #########################################


if __name__ == '__main__':
    app(os.environ['TEST_IMG_PATH'],
        os.environ['SUBMISSION_PATH'],
        os.environ['MODEL_RUN_DEVICE'])
