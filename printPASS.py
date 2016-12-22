from time import ctime

pass_string = '''

$$$$$$$$$      $     $$$$$$$$$ $$$$$$$$$
$       $     $ $    $         $
$$$$$$$$$    $ $ $   $$$$$$$$$ $$$$$$$$$
$           $     $          $         $
$          $       $ $$$$$$$$$ $$$$$$$$$

''' 

fail_string = '''

@@@@@@@@@      @     @@@@@@@@@ @
@             @ @        @     @
@@@@@@@@@    @ @ @       @     @
@           @     @      @     @
@          @       @ @@@@@@@@@ @@@@@@@@@

'''

def printPASS():
    print('\033[92m' + pass_string + '\033[0m')
    print(ctime())


def printFAIL():
    print(fail_string)
    print(ctime())
