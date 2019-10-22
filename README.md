# Instructions for Efficiency Prize competition

Here are detailed instructions about Efficiency Prize stage for Severstal: Steel Defect Detection challenge. 

### Table of content

1. [Terms for Efficiency Prise competition](#terms)
2. [Hardware specifications](#hwspec)
3. [Instructions to build Docker image](#instructions)

### Terms for Efficiency Prise competition <a name="terms"></a>

 - Participants who finish in the top 50 on the Kaggle Private Leaderboard will be allowed for Efficiency Prize stage.
 - Participants should submit to Severstal Docker image of their solution and inference code with Dockerfile from which Docker image was built (see [instruction](#instructions)).
 - Participants are allowed to submit a different code than the one that places them in the Top 50, as long as that solution also scores within the Top 50.
 - Submission deadline for the Efficiency Prize is 11:59 PM UTC November 10, 2019.
 - Participant who provided solution that gets the fastest inference on test images and still scores within the Top 50 is declared the winner of Efficiency Prize.
 - The winner should deliver to Severstal the final model's software code as used to generate the winning Submission and associated documentation.
 - Main competition [Rules](https://www.kaggle.com/c/severstal-steel-defect-detection/rules) also apply.
 - Severstal will post all of the results of the evaluations for the Efficiency Prize in the forum for the Competition.
 

### Hardware specifications <a name="hwspec"></a>

Docker containers provided by participants run on following hardware configuration.

Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz  
GeForce GTX 1080 Ti, Driver Version: 390.67  
CUDA 10.0 cudnn 7  
64GiB RAM  
CentOS 7


### Instructions to build Docker image <a name="instructions"></a>

This instruction is intended to help kagglers to build Docker image for their solutions. We assume you use Python to build your solution.

Repository contains two folders:
- *template* : Contains Dockerfile template and necessary code to wrap your solution for Efficiency scoring. Use it to build your own Docker image.
- *example* : Contains an example of using *template* to package up a dummy-model into Docker image which successfully runs on our hardware. 

**Steps to package up your solution into Docker image:**
1. Install [Docker](https://docs.docker.com/install/) on your PC. Version 19.03 is required.
2. Copy *template* folder to your PC.
3. Put your solution code, model weights and all necessary files into *template* folder.
4. Now you should wrap you inference code for Efficiency scoring. Open *app.py* template and place your inference code into `app()` function. 
5. Then you should modify *Dockerfile* template. Open *Dockerfile* template and place commands to install necessary libs and dependencies there. 
6. Open terminal and change dir to *template* folder:  
    ```bash
    $ cd path_to_template_folder
    ```
7. Build Docker image:  
    ```bash
    $ sudo docker build -f Dockerfile -t your_docker_image_name .
    ```

**How to test your Docker image:**  
1. To test your Docker container with GPU usage you should install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) first.
2. Put test images to some path *your_test_images_path*.
3. To run your Docker container use command with specified *your_test_images_path* and *your_submission_path*:  
    - *on GPU*:   
    ```bash
    $ sudo docker run -e MODEL_RUN_DEVICE='cuda:0' -it --gpus all -v your_test_images_path:/usr/src/app/test_images -v your_submission_path:/usr/src/app/temp your_docker_image_name
    ```
    - *on CPU*:  
    ```bash   
    $ sudo docker run -e MODEL_RUN_DEVICE='cpu'  --rm -v your_test_images_path:/usr/src/app/test_images -v your_submission_path:/usr/src/app/temp your_docker_image_name
    ```  
4. If *app.py* runs successfully, you will see *submission.csv* in *your_submission_path*.
