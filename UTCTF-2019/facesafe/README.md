The theme of this problem is that you have to get access to a "safe" that has 10 users, and uses images to verify the identity of those users (these users correspond to the classes of the CIFAR-10 dataset). You have to trick a neural net into classifying you as "Mr. Deer", who corresponds to the "deer" class of the CIFAR-10 dataset. However, the neural net has been trained such that it usually misclassifies any image of actual deer. You instead have to create a specifically crafted adversarial input image.

In case this doesn't make too much sense, an excellent writeup for the problem is viewable [here](https://ctf.harrisongreen.me/2019/utctf/facesafe/).

Also, some acknowledgements: the code for this project was heavily inspired by and borrowed from the folks who wrote the HackMIT 2017 challenges - in particular, Shreyas Kapur (@revalo). Thank you for your help! You can view the challenges [here](https://github.com/techx/hackmit-puzzle-2017-tinbot).

## Setup

Install any dependencies: 

```bash
pip install -r requirements.txt
```

The server will run with any Keras backend, but tensorflow is prefered for faster boot up time. The solution file only works with tensorflow.

To generate the model, run

```bash
python generate_models.py
```

## Deploy

To run locally, run

```bash
python runserver.py
```

To run in production, you can use docker. Simply do `docker built -t facesafe:latest` followed by `docker run`. 

### Example Solution

There are many different ways of solving this puzzle. The one used is borrowed from the HackMIT folks at `locker/trainer/solve.py`
