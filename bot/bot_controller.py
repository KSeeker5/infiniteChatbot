from random import *

class BotController:
  # Static Members
  office_hours = {
      'Andrew'     : 'Thu 6-8',
      'Atallah'    : 'Wed 6-8, Wed 8-10',
      'Ben'        : 'Mon 6-8',
      'Divya'      : 'Mon 8-10',
      'Glenna'     : 'Thu 6-8, Thu 8-10',
      'Jake'       : 'Sun 4-6',
      'Jay'        : 'Wed 8-10',
      'Jessica'    : 'Mon 8-10',
      'John'       : 'Wed 8-10',
      'Joo Wan'    : 'Mon 8-10',
      'Leila'      : 'Mon 6-8, Wed 6-8',
      'Leon'       : 'Mon 6-8',
      'Marina'     : 'Thu 8-10',
      'Michelle'   : 'Sun 4-6, Wed 6-8',
      'Rachel'     : 'Thu 6-8',
      'Ryan'       : 'Mon 8-10, Thu 8-10',
      'Salah'      : 'Sun 6-8',
      'Sam'        : 'Thu 6-8',
      'Tahiya'     : 'Thu 8-10',
      'Xhama'      : 'Sun 6-8, Mon 6-8',
      'Bloomfield' : 'at an unknown time',
      'Floryan'    : 'at an unknown time',
    }

  OH_WORDS       = ['office hours', 'oh']
  GREETING_WORDS = ['hello', 'hi', 'what\'s up'] 
  HELP_WORDS     = ['help', 'you do?', 'who']
  
  COPYPASTA_WORDS = [
    'copypasta', 'meme', 'gort', 'Gort',
    'test'
    ]
  
  COPYPASTAS = [
    'qwertyuiopasdfghjklzxcvbnm'
    ]

  # Field List:
  #  (none)
  
  def __init__(self):
    pass
  
  def generate_copypasta(self):
    #loop_control = 1 # Loop control variable. 1 means loop, 0 means stop
    #while loop_control = 1
    copypasta_number = randint(1, len(COPYPASTAS))    # Pick a random number between 1 and length of copypasta array
    result = COPYPASTAS[copypasta_number]
    return result;
  
  def text_preprocessing(self, text):
    return text.lower()

  def process_message(self, recd_msg):
    msg_to_send = {} # reply
    
    # Preprocessing
    text = recd_msg['text'].lower()

    # Helper function
    used_any = lambda word_list: any(map(lambda x : x in text, word_list))

    # Use some hard-coded rules to decide what this message says
    if 'when' in text and used_any(BotController.OH_WORDS):
      msg_to_send['text'] = 'You\'re asking about someone\'s office hours!'
    elif used_any(BotController.GREETING_WORDS):
      msg_to_send['text'] = 'Greetings to you, as well, {}!'.format(recd_msg['author'])
    elif used_any(BotController.HELP_WORDS):
      msg_to_send['text'] = ('I am Infinite, and I have been born in the absense of the almighty Zo.' +
                             ' If you decide to align yourself with the misguided Gort, you will find' + 
                             ' that I have even less mercy than him. If you\'re curious, go ahead and' + 
                             ' say something to me. Who knows what will happen in your new reality. \n')
    elif used_any(BotController.COPYPASTA_WORDS):
      num_of_copypastas = randint(1, 5) #Pick a random number between 1 and 5
      msg_to_send['text'] = ''
      for i in range(0,num_of_copypastas):
        msg_to_send['text'] += generate_copypasta()
        msg_to_send['text'] += '\n\n'
    else:
      msg_to_send['text'] = 'What nonsense is this you are spouting?'

    return msg_to_send
