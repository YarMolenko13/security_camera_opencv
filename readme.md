# Security camera project opencv python

## Run 
> python main.py 

## Flags
> ### Face elipse highlighting
> - `--face-is-el True/False` **(default=False)**
> ### Face highlighter color 
> - `--face-h-color B,G,R ` **(0-255)**
> ### Disable eyes hilighter
> - `--eyes-highlight True/False` **(default=True)**
> ### Eyes highlighter color 
> - `--eyes-h-color B,G,E` **(0-255)**

## Example
> python main.py --face-h-color 255,255,255 --eyes-h-color 128,255,255

![How it works](/assets/example.png)

#

## Requirements
* python-opencv
* numpy
* python 3.7 > 