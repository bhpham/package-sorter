# Package Sorter

## Objective

This project implements a function to sort packages into three categories: **STANDARD**, **SPECIAL**, and **REJECTED**, based on their size (volume) and weight (mass). 

### Rules:

- A package is **bulky** if its volume is greater than or equal to 1,000,000 cm³, or if one of its dimensions is greater than or equal to 150 cm.
- A package is **heavy** if its mass is greater than or equal to 20 kg.

The packages are dispatched into the following stacks:
- **STANDARD**: If the package is neither bulky nor heavy.
- **SPECIAL**: If the package is either bulky or heavy.
- **REJECTED**: If the package is both bulky and heavy.

## Requirements
- Python 3.x

## Running the Code

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/package-sorter.git
   cd package-sorter
