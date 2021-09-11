{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb7e6e20",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "\t# @param A : integer\n",
    "\t# @return an integer\n",
    "\tdef colorful(self, A):\n",
    "\t    digits=[]\n",
    "\t    while(A>0):\n",
    "\t        digits.insert(0,A%10)\n",
    "\t        A=A//10\n",
    "\t    hash_set=set()\n",
    "\t    start=0\n",
    "\t    while(start<len(digits)):\n",
    "\t        end=start\n",
    "\t        while(end<len(digits)):\n",
    "\t            if start==end:\n",
    "\t                product=digits[start]\n",
    "\t            else:\n",
    "\t                product*=digits[end]\n",
    "\t            if product not in hash_set:\n",
    "\t                hash_set.add(product)\n",
    "\t            else:\n",
    "\t                return 0\n",
    "\t            end+=1\n",
    "\t        start+=1\n",
    "\t    return 1\n",
    "\n",
    "       \n",
    "          \n",
    "if __name__ == '__main__':\n",
    "    A=int(input())\n",
    "    #B=int(input())\n",
    "    s=Solution()\n",
    "    n=s.colorful(A)\n",
    "    print(n)\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be444e97",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22d9aa76",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cb58ae7",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
