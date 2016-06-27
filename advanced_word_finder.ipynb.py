{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any word of phrase you'd like:test\n",
      "Enter a random string of text:aedtaetgaesdftgaweodptgiaerdpgoiadopgawserutyhuerwtoiaqwejtioghjsajdfhgqoawerdtgoiaherwoighapoirdhetuaqedhrgipqhwerg\n",
      "3 0 t\n",
      "5 1 e\n",
      "10 2 s\n",
      "13 3 t\n",
      "test found\n"
     ]
    }
   ],
   "source": [
    "def word_finder(word, string):\n",
    "    \n",
    "    str_i = 0\n",
    "    wrd_i = 0\n",
    "    \n",
    "    for letter in string:\n",
    "        \n",
    "        if wrd_i < len(word):\n",
    "        \n",
    "            if letter == word[wrd_i]:\n",
    "                print str_i, wrd_i, word[wrd_i]\n",
    "                wrd_i += 1\n",
    "            str_i += 1\n",
    "        \n",
    "        else:\n",
    "            break\n",
    "        \n",
    "    if wrd_i == len(word):\n",
    "        return word + \" found\" \n",
    "    else:\n",
    "        return word + \" not found\"\n",
    "\n",
    "\n",
    "\n",
    "print word_finder(raw_input(\"Enter any word of phrase you'd like:\"), raw_input(\"Enter a random string of text:\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def word_finder(word, string):\n",
    "    \n",
    "    str_i = 0\n",
    "    wrd_i = 0\n",
    "    \n",
    "    for letter in string:\n",
    "        \n",
    "        if wrd_i < len(word):\n",
    "        \n",
    "            if letter == word[wrd_i]:\n",
    "                print str_i, wrd_i, word[wrd_i]\n",
    "                wrd_i += 1\n",
    "            str_i += 1\n",
    "        \n",
    "        else:\n",
    "            break\n",
    "        \n",
    "    if wrd_i == len(word):\n",
    "        return word + \" found\" \n",
    "    else:\n",
    "        return word + \" not found\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any word or phrase you'd like: test\n",
      "Enter a random string of text: testkkk\n",
      "0 0 t\n",
      "1 1 e\n",
      "2 2 s\n",
      "3 3 t\n",
      "test found\n",
      "Do you want to play again, Y or N?NO\n"
     ]
    }
   ],
   "source": [
    "want_to_play = True\n",
    "while want_to_play:\n",
    "    secret_word = raw_input(\"Enter any word or phrase you'd like: \")\n",
    "    user_answer = raw_input(\"Enter a random string of text: \")\n",
    "    print word_finder(secret_word, user_answer)\n",
    "    user_response = raw_input(\"Do you want to play again, Y or N?\").lower()\n",
    "    when_to_stop = ['n', 'no']\n",
    "    if user_response in when_to_stop:\n",
    "        want_to_play = False\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "0\n",
      "BLAST OFF!!!\n"
     ]
    }
   ],
   "source": [
    "\n",
    "count = 10\n",
    "for number in range(11):\n",
    "    print count\n",
    "    count -= 1\n",
    "print \"BLAST OFF!!!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "0\n",
      "BLAST OFF!!\n"
     ]
    }
   ],
   "source": [
    "count = 10\n",
    "while count >= 0:\n",
    "    print count\n",
    "    count -= 1\n",
    "print \"BLAST OFF!!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
