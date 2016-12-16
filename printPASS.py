from time import ctime

def printPASS():
    pass_string = '''

    $$$$$$$$$      $     $$$$$$$$$ $$$$$$$$$
    $       $     $ $    $         $
    $$$$$$$$$    $ $ $   $$$$$$$$$ $$$$$$$$$
    $           $     $          $         $
    $          $       $ $$$$$$$$$ $$$$$$$$$

    ''' 
    print(pass_string, ctime())

def printFAIL():
    fail_string = '''

    @@@@@@@@@      @     @@@@@@@@@ @
    @             @ @        @     @
    @@@@@@@@@    @ @ @       @     @
    @           @     @      @     @
    @          @       @ @@@@@@@@@ @@@@@@@@@

    '''
    print(fail_string, ctime())
