# questReport
send a quest report of a list to telegram

languages:  :de:  :us:

#### HELP ON DISCORD: https://discord.gg/RDmxphS

## Install

`pip3 install -r requirements.txt`

## Config

`cp config_example.ini config.ini`

set singlechat_id to empty for no venues and linked directly to google maps

a json file is created after the first start, put here the sum of stardust, pokemon id and item id what you like to be send

## Start

`python3 quest-main.py`

`python3 quest-main.py another_config.ini`

## Notes

the json file can be changed during operation without having to restart the script

the script works fully automatically. it sends quest as soon as it is found and removes it automatically when it is no longer available

## ToDo list

- we want to build a backend to simplify the configuration of the json file

## Example

![example](https://raw.githubusercontent.com/Micha854/questReport/master/example.png)