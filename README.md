# weatherDiagrams

A server that analyzes data which it gets from several stations (probably Raspberry Pi's) and
creates diagrams. I think this is a cool project idea because it requires a lot of different
skillsets like Hardware, Web Dev and Data Analyzation. For the stations I am using Python
because it's pretty easy to work with hardware on a RPi with Python; for the Api the stations
use I am using Nodejs, just because I know it the best. And for the Data Analyzation I am
using Python because there are so many usful libraries and I do not know any other good
programming languages for this stuff very well.

## What data the RPi's will send to be analyzed and visualized

Each station obviously has its own directory where the Api will store the data which it gets.
In these directories that belong to the several stations, there are subdirectories for every
single year. In those, there are subdirectories for the months which contain json files
for each day. (I'm sorry for this horrible explanation)

## How to create diagrams

I'm planning to create a simple command line interface which can be used to create diagrams.
This means that you have to execute a command yourself whenever you want a diagram. Maybe later
I'll also add some Api endpoints for creating and downloading diagrams.
