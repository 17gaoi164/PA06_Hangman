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
		 'word_so_far':"",
         'guess': "",
		 'win':False,
         'guessed': False,
         'nCorrect': 0,
         'tries': 5
         }

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
    global state
    state['word']=hangman_app.generate_random_word()
    state['guesses'] = []
    state['word_so_far'] = ''
    state['win'] = False
    state['nCorrect'] = False
    state['tries'] = 5
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])

def hangman():
    """ plays hangman game """
    global state
    if request.method == 'GET':
        return play()

    elif request.method == 'POST':
        guess = request.form['guess']
        word = state['word']
        guesses = state['guesses']
        print(state)

        if len(guesses) == 0:
            state['word_so_far'] = hangman_app.hide_word(state['word'])


        # check if letter has already been guessed
        # and generate a response to guess again
        if guess in state['guesses']:
            state['guessed'] = True
            state['tries'] -= 1
        else:
            state['guesses'] += guess
            state['guessed'] = False


    # else check if letter is in word
        if guess in state['word'] and state['tries'] > 0 and state['win'] == False:
            state['word_so_far'] = hangman_app.reveal_letter(state['word']
            ,state['word_so_far']
            ,state['guesses'])

            state['nCorrect'] += 1
        else:
            state['tries'] -= 1

    # then see if the word is complete
        if state['nCorrect'] == len(word):
            state['win']=True

        return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run(port=3000)
