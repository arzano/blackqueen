<p align="center"><img width=17.5% src="http://nele.xyz/net-3.png"></p>
<p align="center"><img width=60% src="http://nele.xyz/black-queen-label.png"></p>

<p align="center">
<a href="https://www.haskell.org/ghc/" ><img src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg"></a>
<a href="https://travis-ci.org/mmagorsc/blackqueen"> <img src="https://travis-ci.org/mmagorsc/blackqueen.svg?branch=master"></a>
<a href="https://codeclimate.com/github/mmagorsc/blackqueen/maintainability"><img src="https://api.codeclimate.com/v1/badges/716c832ef3bbf2ad0e42/maintainability" /></a>
<a href="#contributing"> <img src="https://img.shields.io/badge/contributions-welcome-orange.svg"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>


## tl;dr

Black Queen is a self learning Loosing-Chess engine. It is based on neural networks and utilizes supervised learning as well as reinforcement learning. 
Therefor it can be trained using either an existing database of anti chess games (for example taken from lichess) or by self-play. 

## Table Of Contents 

- [Loosing Chess](#loosing-chess)
- [Installation](#installation)
- [Training](#training)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Loosing Chess

According to _The Classified Encyclopedia of Chess Variants_ Loosing Chess (also known as Anti Chess) is one of the most popular chess variants. 
The objective of the game is to loose all your chess pieces. In the following you can see an exemplary game of loosing chess:

<p align="center"><img src="http://nele.xyz/antichess.gif" height="300" width="300"></p>

## Installation

The most straightforward way to install BlackQueen is using *pip*:


``` shell
$ git clone https://github.com/mmagorsc/blackqueen/ 
$ cd blackqueen
$ pip install .
```

## Training 

In order to use the engine you have to train the BlackQueen first. The neural network can be trained using either supervised learning or reinforcement learning. Pretrained models may be added in future releases. 

### Supervised Learning

In order to start the supervised learning we have to obtain a database containing anti chess. So far the pgn-format is supported. Databases are available at [https://database.lichess.org/antichess/](https://database.lichess.org/antichess/), for example: 

``` shell
$ cd data/games/
$ curl -O https://database.lichess.org/antichess/lichess_db_antichess_rated_2019-05.pgn.bz2
$ bunzip2 lichess_db_antichess_rated_2019-05.pgn.bz2
$ cd ../..
```

Afterwards the supervised learning can be started using

``` shell
$ python src/chess_zero/run.py sl
```

### Reinforcement Learning 

The reinforcement learning process consists of three workers: _self_, _opt_, _eval_. First of all the _self_ worker is used to generate training data by self-play. Afterwards the _opt_ worker is used to optimize i.e. train the model using the previously generated training data. Finally the _eval_ worker is used to eval whether the newly trained model is stronger as the last model. If so, the last model will be replaced by the new model. To do so just execute: 

``` shell
python src/chess_zero/run.py self
python src/chess_zero/run.py opt
python src/chess_zero/run.py eval
``` 

## Usage

The _Universal Chess Interface_ is implemented. Just execute 

``` shell
python src/chess_zero/run.py uci
``` 

to start the UCI. Afterwards launch a GUI of your choice which supports the universal chess interface. A few examples are: 

- [http://pychess.org/](http://pychess.org/)
- [http://scid.sourceforge.net/](http://scid.sourceforge.net/)
- [http://www.playwitharena.de/](http://www.playwitharena.de/)

## Trainig Results

The engine has been evaluated using XY. In the following plot you can see the number of wins of BlackQueen in percent depending on the number of training steps. 

## Contributing

Contributions are welcome. You have an idea, suggestion for improvement or have found a bug? Just create an issue or send a pull request. 

## License 

The project is licensed under the MIT-license. Furthermore the project is based on Zeta36's great Chess-Alpha-Zero library and Akababa's nice fork which are also licensed under the MIT license. 
