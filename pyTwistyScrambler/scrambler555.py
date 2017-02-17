from . import SCRAMBLE_SRC, MEGA_SCRAMBLE_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + MEGA_SCRAMBLE_SRC)

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=60):
    """ Gets a WCA scramble of length N for a 5x5x5 cube. Defaults to csTimer's default length of 60. """
    return _scrambler.call("megaScrambler.get555WCAScramble", n)

@trim
def get_SiGN_scramble(n=60):
    """ Gets a SiGN-notation scramble of length N for a 5x5x5 cube. Defaults to csTimer's default length of 60. """
    return _scrambler.call("megaScrambler.get555SiGNScramble", n)