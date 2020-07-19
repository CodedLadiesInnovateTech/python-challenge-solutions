{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original List [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]\n",
      "New List [[10, 20], [30, 56, 25], [33], [40]]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Write a Python program to remove duplicates from a list of lists\n",
    "\"\"\"\n",
    "import itertools\n",
    "num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]\n",
    "print(\"Original List\", num)\n",
    "num.sort()\n",
    "new_num = list(num for num,_ in itertools.groupby(num))\n",
    "print(\"New List\", new_num)\n",
    "\n",
    "#reference: w3resources"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
