{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "e5717cb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.1: 8\n",
      "1.2: [19, 45, 7, 27, 36, 18, 17, 20, 29, 14, 22, 8, 45, 36, 63, 25, 11, 10, 90, 4, 18, 72, 54, 63, 28, 22, 13, 19, 4, 23]\n",
      "1.3: ['a', 20, 23, 29, 10, 'a', 30, 13, 2, 11, 'a', 9, 2, 30, 27, 'a', 11, 20, 19, 1, 'a', 10, 8, 6, 16, 'a', 25, 5, 10, 24]\n",
      "1.4: [21, 26, 25, 1, 24, 10, 27, 8, 23, 4, 10, 22, 1, 3, 7, 16, 18, 29, 11, 4, 1, 29, 10, 16, 10, 10, 2, 26, 26, 7, 10, 10, 6, 25, 4, 7, 12, 24, 5, 8, 23, 16, 8, 3, 16, 1, 9, 4, 27, 26, 9, 25, 7, 14, 27, 21, 27, 28, 2, 2, 27, 22, 3, 23, 14, 16, 10, 12, 14, 8, 10, 5, 16, 12, 24, 3, 28, 9, 21, 7, 25, 9, 5, 3, 27, 7, 29, 25, 13, 11, 25, 21, 2, 14, 8, 17, 18, 23, 22, 12, 8]\n"
     ]
    }
   ],
   "source": [
    "# Logical Processing Homework\n",
    "\n",
    "# Problem 1 Stacking logical operators\n",
    "\n",
    "influenza_genome = [19, 15, 7, 9, 12, 6, 17, 20, 29, 14, 22, 8, 15, 12, 21, 25, 11, 10, 30, 4, 6, 24, 18, 21, 28, 22, 13, 19, 4, 23, 16, 25, 13, 28, 16, 29, 4, 3, 25, 13, 10, 26, 26, 18, 25, 28, 24, 18, 3, 9, 11, 29, 30, 16, 24, 5, 5, 25, 14, 7, 1, 15, 6, 6, 19, 19, 15, 2, 14, 7, 21, 5, 26, 25, 18, 18, 9, 7, 27, 4, 1, 23, 30, 25, 24, 29, 11, 16, 20, 15, 2, 9, 8, 13, 1, 13, 5, 17, 29, 25, 16, 13, 3, 30, 10, 21, 9, 18, 20, 14, 20, 19, 6, 4, 20, 5, 14, 5, 12, 27, 18, 28, 13, 30, 6, 9, 12, 9, 29, 4, 14, 22, 7, 25, 11, 12, 5, 24, 6, 3, 8, 3, 20, 24, 8, 23, 22, 11, 22, 10, 13, 14, 2, 6, 22, 22, 7, 6, 18, 28, 25, 4, 6, 24, 10, 24, 15, 18, 12, 24, 10, 16, 24, 21, 19, 24, 8, 8, 8, 10, 8, 15, 26, 14, 21, 18, 6, 10, 23, 2, 20, 15, 1, 4, 20, 8, 6, 1, 4, 15, 21, 26, 25, 1, 24, 15, 27, 8, 23, 4, 30, 22, 1, 3, 7, 16, 18, 29, 11, 4, 1, 29, 30, 16, 30, 10, 2, 26, 26, 7, 10, 15, 6, 25, 4, 7, 12, 24, 5, 8, 23, 16, 8, 3, 16, 1, 9, 4, 27, 26, 9, 25, 7, 14, 27, 21, 27, 28, 2, 2, 27, 22, 3, 23, 14, 16, 30, 12, 14, 8, 10, 5, 16, 12, 24, 3, 28, 9, 21, 7, 25, 9, 5, 3, 27, 7, 29, 25, 13, 11, 25, 21, 2, 14, 8, 17, 18, 23, 22, 12, 7, 26, 11, 25, 1, 23, 9, 12, 2, 4, 17, 27, 9, 13, 19, 15, 10, 12, 21, 25, 5, 1, 16, 17, 28, 23, 18, 10, 15, 18, 1, 11, 14, 10, 18, 12, 1, 23, 23, 25, 13, 27, 27, 6, 9, 11, 23, 6, 23, 14, 9, 15, 11, 24, 11, 29, 18, 6, 19, 16, 14, 26, 2, 14, 15, 25, 6, 21, 23, 25, 27, 5, 1, 17, 4, 7, 18, 8, 9, 10, 5, 21, 29, 9, 6, 2, 22, 12, 1, 13, 19, 6, 17, 21, 22, 26, 21, 10, 29, 8, 13, 10, 29, 6, 29, 16, 30, 5, 25, 14, 15, 15, 9, 24, 13, 5, 28, 18, 11, 21, 15, 12, 5, 16, 5, 29, 29, 29, 3, 10, 24, 16, 16, 12, 14, 6, 22, 21, 10, 10, 2, 14, 9, 29, 29, 2, 26, 11, 6, 7, 28, 10, 3, 24, 30, 2, 23, 9, 29, 27, 19, 1, 15, 11, 5, 7, 9, 26, 28, 27, 10, 20, 23, 29, 10, 15, 30, 13, 2, 11, 5, 9, 2, 30, 27, 14, 11, 20, 19, 1, 12, 10, 8, 6, 16, 3, 25, 5, 10, 24]\n",
    "\n",
    "# Given the array influenza_genome, write code that uses for loops and if statements to do the following and print the results(see below for instructions):\n",
    "\n",
    "# 1.1 add 1 to the value at the index 300.\n",
    "influenza_genome[300] += 1\n",
    "print(\"1.1:\", influenza_genome[300])\n",
    "\n",
    "# 1.2 for the first 30 elements, if the value of the element is divisable by 3, multiply the value by 3.\n",
    "     \n",
    "for i in range(len(influenza_genome[0:30])):\n",
    "    if influenza_genome[i] % 3 == 0:\n",
    "        influenza_genome[i] *= 3\n",
    "        \n",
    "print(\"1.2:\", influenza_genome[0:30])       \n",
    "\n",
    "# 1.3 for the last 30 elements, if the index value at that point is divisable by 5, replace the value with \"a\".\n",
    "\n",
    "for i in range(-30,0):\n",
    "    if i % 5 == 0:\n",
    "        influenza_genome[i] = \"a\"\n",
    "\n",
    "print(\"1.3:\", influenza_genome[-30:])\n",
    "\n",
    "# 1.4 for all elements between index 200 and 300, if the value of the element is divisable by BOTH 3 AND 5, replace the value with the 10.\n",
    "\n",
    "for i in range(200,300):\n",
    "    if (influenza_genome[i] % 3 ==0) and (influenza_genome[i] % 5 == 0):\n",
    "        influenza_genome[i] = 10\n",
    "        \n",
    "print(\"1.4:\", influenza_genome[200:301])\n",
    "\n",
    "# Only print the section of the array that is modified after completing each operation. i.e only print index 300 of the array after 1.1 and only the first 30 elements after 1.2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "526232d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.1:\n",
      "4\n",
      "7\n",
      "12\n",
      "24\n",
      "2.2:\n",
      "4\n",
      "7\n",
      "12\n",
      "24\n",
      "2.3:\n",
      "12 12 12 12 12 12 12 \n"
     ]
    }
   ],
   "source": [
    "# Problem 2 Loops within loops\n",
    "# Given the array influenza_genome, write code using both for and while loops that:\n",
    "\n",
    "# 2.1 Create a for loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)\n",
    "\n",
    "print(\"2.1:\")\n",
    "for i in range(len(influenza_genome)):\n",
    "    if i > 233 and i < 238:\n",
    "        print(influenza_genome[i])\n",
    "\n",
    "# 2.2 Create a while loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)\n",
    "\n",
    "index = 234\n",
    "print(\"2.2:\")\n",
    "while index > 233 and index < 238:\n",
    "    print(influenza_genome[index])\n",
    "    index += 1    \n",
    "    \n",
    "# 2.3 Create a for loop that iterates over items index 234 through 237 and if the index is 236 print the item 7 times.\n",
    "print(\"2.3:\")\n",
    "for i in range(234,238):\n",
    "    if i == 236:\n",
    "        print((str(influenza_genome[i]) + \" \") * 7)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "cfb10a8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.1:\n",
      "[19, 22, 11, 18, 16, 9, 13, 24, 21, 10]\n",
      "3.2:\n",
      "[19, 18, 22, 25, 18, 22, 16, 29, 10, 28, 11, 5, 1, 19, 21, 18, 1, 29, 2, 13]\n",
      "3.3:\n",
      "[19, 22, 18, 16, 10, 11, 1, 21, 1, 2]\n"
     ]
    }
   ],
   "source": [
    "# Problem 3 Functions\n",
    "# You are going to implement 3 funtions that will process the influenza_genome list in various ways.\n",
    "\n",
    "# 3.1 write a function, that takes in the array as an argument, and outputs 10 values from the dataset, spaced out by indexes that are 25 apart (ie 0, 25, 50, etc)\n",
    "\n",
    "output_by_five = []\n",
    "def values_by_five(dataset):\n",
    "    for i in range(len(dataset)):\n",
    "        if i >= (25 * 10):\n",
    "            break\n",
    "        elif i % 25 == 0:\n",
    "            output_by_five.append(dataset[i])\n",
    "    print(output_by_five)\n",
    "\n",
    "print(\"3.1:\")\n",
    "values_by_five(influenza_genome)\n",
    "\n",
    "# 3.2 write a function that takes in the dataset as an argument and outputs 20 values from the dataset, spaced out by indexes that are y apart (ie you can decide how far apart they should be iterated as long as they dont exceed the length of the dataset)\n",
    "\n",
    "output_by_y = []\n",
    "def values_by_y(dataset, y):\n",
    "    for i in range(len(dataset)):\n",
    "        if i >= (y * 20):\n",
    "            break\n",
    "        elif i % y == 0:\n",
    "            output_by_y.append(dataset[i])\n",
    "    print(output_by_y)\n",
    "\n",
    "print(\"3.2:\")\n",
    "values_by_y(influenza_genome, 5)\n",
    "\n",
    "# 3.3 write a function that takes the output from the function from 3.2 as an argument, then only prints out every other item (ie there should only be 10 outputs)\n",
    "\n",
    "others = []\n",
    "def every_other(inputdata):\n",
    "    for i in range(len(inputdata)):\n",
    "        if i % 2 == 0:\n",
    "            others.append(inputdata[i])\n",
    "    print(others)\n",
    "\n",
    "    \n",
    "print(\"3.3:\")    \n",
    "every_other(output_by_y)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "a09ee755",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0:\n",
      "12 12 12 12 12 12 12 \n"
     ]
    }
   ],
   "source": [
    "# Problem 4 Putting it all together\n",
    "# Write a function that implements the code from problem 1.4, then implements the code from problem 2.3.\n",
    "\n",
    "# The function should create a modified version of the influenza_genome list as per 1.4, then print the section described in problem 2.3. \n",
    "\n",
    "def its_all_coming_together(putlisthere):\n",
    "    for i in range(200,300):\n",
    "        if (influenza_genome[i] % 3 ==0) and (influenza_genome[i] % 5 == 0):\n",
    "            influenza_genome[i] = 10\n",
    "        if i == 236:\n",
    "            print((str(influenza_genome[i]) + \" \") * 7)\n",
    "\n",
    "\n",
    "        \n",
    "print(\"4.0:\")\n",
    "its_all_coming_together(influenza_genome)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edb49f16",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
