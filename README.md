# Final Project Representer
#### Video Demo:  https://youtu.be/aPVdaR8pv6k
#### Description:

Final Project Representer (abv. FPR) was developed as final project for Harvard CS50’s Introduction to Programming with Python course.
FPR's purpose is to create slideshow and represent it with synthetized speach for submitting the final project. Video capturing not provided.

## Getting Started

Modify provided example script.txt to your own texts and run project.py. Differently named script file can be used with command line argument.

### Files
* **project.py**:
    * main code file
    * provides all code
* **script.txt**:
    * sample script file
    * interpreter creates slides based on this
* **test_project.py**:
    * pytest file for testing
* **test.png**:
    * png file for testing
* **invalid_script.txt**:
    * malformed script file for testing
* **requirements.txt**:
    * programs that need to be pip installed prior using main
* **README.md**:
    * this file

### Dependencies

* Final Project Representer depends following external libraries:
    * Pillow    ```(pip install pillow)```
    * pyttsx3   ```(pip install pyttsx3)```
* and following internal libraries:
    * tkinter
    * time
    * ast
    * argparse

### Executing program

* Run project.py, see Help for command line options
    ```
    python project.py
    ```

## Help

* Run with -h to see command line arguments.
    ```
    python project.py -h
    ```

## Author

Samu Reinikainen
samu.reinikainen@gmail.com

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the APACHE LICENSE, VERSION 2.0 License