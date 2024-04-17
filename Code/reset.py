# RESET

# Running this program will erase the high-score and reset it to 0
# And the tutorial will also be shown when the game in runned.

import pickle
with open('Data/data.dat', 'wb') as f:
    pickle.dump(0, f)      # high_score
    pickle.dump(True, f)   # new_player
