# __main__.py

import sys

from .step1.tournament import Tournament
from .step2.impostors import GetImpostors
from .step3.paths import Proofs
from .step4.tasks import Tasks

ARG = str(sys.argv[1])

if __name__ == '__main__':
    if ARG == "1":
        Tournament.run()
    elif ARG == "2":
        GetImpostors.run()
    elif ARG == "3":
        Proofs.run()
    else:
        Tasks.run()
