## [What is FooBar?](https://www.turing.com/kb/foobar-google-secret-hiring-technique)
Looking up the question names yields more results, such as lore-accurate question desccriptions and test cases

# Question 1 - Braille Translation
The task is to translate a given string of lowercase letters and spaces into Braille, where each character is represented by a 2x3 grid of 6 dots. Each dot is either a bump (`1`) or flat (`0`). The program must handle lowercase letters using predefined Braille patterns and represent spaces as `000000`. Additionally, capital letters should be encoded with a special capitalization mark (`000001`) followed by the Braille pattern for the letter. The function should return a concatenated string of 1s and 0s representing the Braille translation of the input text, which is no longer than 50 characters and consists only of lowercase letters and spaces.

# Question 2.a - Elevator Maintenance
The task is to sort a list of elevator version strings in ascending order based on major, minor, and revision numbers. Each version consists of at least a major number, and may optionally include a minor and revision number. Versions with fewer components should be considered smaller than those with more components (e.g., `1` < `1.0` < `1.0.0`). The sorting should handle cases where versions have missing minor or revision numbers by treating them as zeros when comparing (e.g., `1.0` is equivalent to `1.0.0`). The input is a list of version strings, and the output should be the list sorted according to the version numbers.

# Question 2.b - En Route Salute
The task is to count how many salutes are exchanged in a hallway based on a string representing employees walking in different directions. The string consists of three characters: > (employee walking to the right), < (employee walking to the left), and - (empty space). When two employees cross paths, they exchange a salute, and each salute takes 10 seconds. The goal is to count the total number of salutes exchanged as employees pass each other. Each time an employee moving to the right (>) crosses an employee moving to the left (<), they will exchange a salute. The function should return the total number of salutes based on the string input.

# Question 3.a - Bomb Baby!
The task is to determine how many replication cycles (generations) it will take to generate exactly the specified number of Mach bombs (`M`) and Facula bombs (`F`), starting with one of each. The bombs replicate according to two distinct rules: each Mach bomb creates a Facula bomb, and each Facula bomb creates a Mach bomb. The goal is to compute the minimum number of cycles required to reach the target number of bombs, or to determine if it's impossible to do so. The values for `M and `F can be as large as `10^50`, and the function should return the number of generations needed or `"impossible"` if it's not possible to reach the target values.

