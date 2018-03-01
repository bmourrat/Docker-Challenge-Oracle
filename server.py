from flask import Flask, request, render_template #flask is the library that turns our code into a REST web service
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

def fibonacci(n):
    #returns a list containing the first n terms of the Fibonacci sequence, n natural entire
    #we first deal with the particular cases n=0 and n=1
    if n==0:
        return []
    if n==1:
        return [0]

    #for n>=2, we use an while loop that append to our list the sum of the last 2 terms of our list
    if n>=2:
        fibo=[0,1] #we initiate our list to [0,1]
        i=2
        while i<n:
            fibo.append(fibo[i-2]+fibo[i-1])
            i=i+1
        return fibo

    #we could also have used a for loop

def sort(list):
    #list : list of entires
    #returns the numbers of list sorted with even numbers first in descending order, and then odd numbers in descending order
    even=[] #list that will contain the even numbers
    odd=[] #list that will contain the odd numbers
    for number in list: #we run throught the entire list and put each number into his matching list thanks to the modulo operator
        if number%2==0:
            even.append(number)
        if number%2==1:
            odd.append(number)
    sorted=even[::-1]+odd[::-1] #we reverse the order of each of the two lists and then concatenate them
    return sorted

app = Flask(__name__)

#indicates to the server how to deal with the http request
@app.route('/fibonacci/<int:n>')
def fibo(n):
     l=fibonacci(n)
     return jsonify({"fibonacci":l,"sorted":sort(l)})

#to launch our server
if __name__ == '__main__':
     app.run(host='0.0.0.0',port=80)
