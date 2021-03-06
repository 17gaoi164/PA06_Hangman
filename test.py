"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
         'word_so_far':"-----------",
        'done':False}

@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')

@app.route('/start')
def play():
    global state
    state['word']=
    state['guesses'] = []
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
    """ plays hangman game """
    global state
    if request.method == 'GET':
        return play()
    elif request.method == 'POST':
        letter = request.form['guess']
        nLetters = state['word']
        nCorrect = 0
        win = False
        # check if letter has already been guessed
        if letter in state['guesses']:
            print('we')
        else:
            state['guesses'] += [letter]
    # and generate a response to guess again

    # else check if letter is in word
        if letter in state['word']:
            nCorrect+=1

    # then see if the word is complete
        if nCorrect == nLetters:
            win=True

    # if letter not in word, then tell them

    #state['guesses'] += [letter]
        return render_template('play.html',state=state)




        if __name__ == '__main__':
            app.run('0.0.0.0',port=3000)
