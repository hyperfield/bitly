## Bitly: links and clicks

### Description

*Bitly: links and clicks* is a small script that works with the [bit.ly](https://bit.ly) API. This script outputs short links using the bit.ly service, and click statictics for a bit.ly link.

### How to install

You need Python 3 to execute this script. If Python 3 is not yet installed then download it from http://www.python.org for your operating system and install. Once you have Python on your system, run the following commands:

`source bitly-env/bin/activate`
`pip3 install -r requirements.txt`

### How to launch

If the *Bitly: links and clicks* virtual environment is not yet active, run
`source bitly-env/bin/activate`. Use `deactivate` to exit the virtual environment.

`python3 main.py` 

If you use a *nix-based operating system, you can do the following in your terminal:

`chmox +x main.py`

After this you will be able to execute the script by typing `./main.py` in your terminal (as long as you are in the script's directory).

### Environment variables

There is only one environment variable, which is contained in the `.env` file:

`TOKEN`

It stores the bit.ly token to use by *Bitly: links and clicks* to talk to the bit.ly API. If you don't yet have your own token, you can get it by registering on bit.ly.

### Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.