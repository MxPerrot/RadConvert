# RadConvert

## Description

This project converts and compares real life exemple of radiation units using [XKCD's radiation dose chart](https://xkcd.com/radiation/).

It uses a tkinter GUI to display the user interface

## Getting started

Clone this repo on your machine, go into the project directory and run 

```bash
python3 main.py
```

There are no requirements. All the necessary libraries are included in the default python package

## Screenshots
![Screenshot of the app](assets/images/screenshots/screenshot2.png?raw=true "Title")

## Todo

### Features
- Display the Radiation Chart on demand
- Add a more detailed description and links 
- Add a switch input button to switch between main and secondary input

### Fixes
- Rewrite radiation exemples
- Make long units more readable
- Make UI more adaptable to changes in elements' size
- Better input management.
    - Floating point inaccuracy
    - Add a "main" side so that when changing unit from the secondary side, it doesn't change the main input value
    - 