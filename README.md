# ESILV-ADSA-MiniProblem

![GitHub](https://img.shields.io/github/license/Madjakul/ESILV-ADSA-MiniProblem) ![GitHub contributors](https://img.shields.io/github/contributors/Madjakul/ESILV-ADSA-MiniProblem) ![code size](https://img.shields.io/github/languages/code-size/Madjakul/ESILV-ADSA-MiniProblem)
___


## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.8+


## Installing miniproblem

This module doesn't require any external libraries. However if you do not have Python on your computer and prefer using Docker we have an easy way to build the images and to run it. For now, all you need to do is to copy the repository to your computer.


## Using miniproblem 


### For MACOS and Linux Users


#### Without Docker

Simply open the terminal from the repository and run
```bash
make run ARG=[the step number you want]
```


#### With Docker

Open the terminal from the repository and start by building the 4 images coresponding to each of the 4 steps of the problem. From there, you can run:
```bash
make build
```

Once all the images are built, you can run the 4 steps in a row by simply using:
```bash
make dockrun
```

The results of all the steps will be displayed in your terminal.


### For Windows Users


#### Without docker

Open your IDE terminal or the command prompt from the repository and run the following:
```
python3 -m miniproblem [the step number you want]
```

Sometimes the syntax ```python3``` isn't reconized,  you may want to give a try to
```
py -m miniproblem [the step number you want]
```


#### With docker

You will have to build all the images and run them afterward, one by one. Open your favourite consol commands handler from the repository and build the images with the following:
```
docker build -t miniproblem1:latest -f Step1.Dockerfile .
docker build -t miniproblem2:latest -f Step2.Dockerfile .
docker build -t miniproblem3:latest -f Step3.Dockerfile .
docker build -t miniproblem4:latest -f Step4.Dockerfile .
```

once everything is built, you can run which ever image you want and see the result in your consol.
```
docker run -it miniproblem1
docker run -it miniproblem2
docker run -it miniproblem3
docker run -it miniproblem4
```


## Contributors

Thanks to the following people who have contributed to this project:
* [TLimnavong]


## Contact
If you want to contact me you can reach me at [@Madjakul]


[@Madjakul]: https://twitter.com/Madjakul
[TLimnavong]: https://github.com/TLimnavong
