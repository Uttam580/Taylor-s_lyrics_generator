

![GitHub repo size](https://img.shields.io/github/repo-size/Uttam580/Taylor-s_lyrics_generator?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/Uttam580/Taylor-s_lyrics_generator?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/Uttam580/Taylor-s_lyrics_generator?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Uttam580/Taylor-s_lyrics_generator?color=red&style=plastic)

## Lyrics generator

### quick demo: 

![demo_gif](https://github.com/Uttam580/Taylor-s_lyrics_generator/blob/master/lstmBatch32Epoch15.gif)


### How Does It work?

Make seed lyrics. Feed it to the neural network to generate one character after the seed lyrics, ‘b’.
I took input char length 100.

input: 'I want to ' -> output 'b'

Append new character to the seed lyrics and remove the very first character.

new input : ' want to b'

Feed the new seed lyrics into the neural network and iterate the above process as many as you want.

'I want to ' -> ' want to b' -> 'want to be' -> .... -> 'ing of pop'

In the end, you might get something like ‘I want to be king of pop’
 
This process is known as teacher forcing: training neural network that uses model output from a prior time step as an input.

I trained model for 15 Epoch for batch size 32 , for more accuracy increase the epoch for training (400, 600 etc.)


### Resources: 

```Lstm network architect``` : https://colah.github.io/posts/2015-08-Understanding-LSTMs/

https://levelup.gitconnected.com/lyrics-generation-using-lstm-5a5a0bcac4fa
