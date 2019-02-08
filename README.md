# ValuefyChallenge1

Designed with passion to complete the Valuefy coding challenge. 
(https://github.com/valuefy-solutions/coding-challenges/blob/master/python/scraper.md)

Setup Instructions:
1. Install Python 3.5.3 (from here : https://www.python.org/downloads/release/python-350/)
2. In cmd, powershell or bash, type "python scraper.py" and press enter

Project Structure:
1. scraper_lib.py contains essential functions scraper.py uses
2. tests\test.py is another version of linearly solving this challenge (without recursion or multithreading)
3. scraper.py is the main file from which the code runs, and does not require an argument

Features:
1. Multiprocessing is implemented
2. Recursive url discovery of medium.com is implemented (note: the tree implementation of the url structure has given way to the list implementation because there is no need for a parent-child relationship in the urls once visited)
3. The program randomly sleeps to mimic human requests - this is untested and based off previous experience coding a google-dork finding bot
4. 


Inspirations for writing this code:
1. http://eikke.com/how-not-to-write-python-code/
2. https://medium.com/the-andela-way/idiomatic-python-coding-the-smart-way-cc560fa5f1d6
3. https://github.com/springload/site-url-scraper (served only as a general idea of how to go from an empty page to the current code)
4. https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing
5. https://medium.com/python-pandemonium/how-to-speed-up-your-python-web-scraper-by-using-multiprocessing-f2f4ef838686


