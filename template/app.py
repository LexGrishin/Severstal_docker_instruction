import os
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

    #########################################


if __name__ == '__main__':
    app(os.environ['TEST_IMG_PATH'],
        os.environ['SUBMISSION_PATH'],
        os.environ['MODEL_RUN_DEVICE'])
