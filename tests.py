from assistant import *

def test_file_cmd():
    assert file_cmd('file all-words.dat') == 'Loaded all-words.dat'
    assert file_cmd('file uknown_file.txt') == 'Error because file not found'
    assert file_cmd('file') == 'You haven\'t entered the file name'

def test_info_cmd():
    file_cmd('file all-words.dat')
    assert info_cmd('info') == '113004 lines\n1330218'

def test_words_cmd():
    file_cmd('file all-words.dat')
    assert words_cmd('words') == 'Read file as list of words'

def test_search_cmd():
    file_cmd('file all-words.dat')
    info_cmd('words')
    assert search_cmd('search joker') == 'joker is in the list of words'
    # assert 'number' in search_cmd('search joker1')

def test_sum_cmd():
    assert float(sum_cmd('sum 2 3 4 0.3 0.2').split(' ')[-1]) == sum([2,3,4,0.3,0.2])

    assert sum_cmd('sum') == 'You haven\'t entered the numbers'
    assert 'Error' in sum_cmd('sum 0,3 0,2')
    assert 'Error' in sum_cmd('sum abc vac')

def test_avg_cmd():
    numbers = [2,3,4,0.3,0.2]
    assert float(avg_cmd('avg 2 3 4 0.3 0.2').split(' ')[-1]) == sum(numbers)/len(numbers)

    assert avg_cmd('avg') == 'You haven\'t entered the numbers'
    assert 'Error' in avg_cmd('avg 0,3 0,2')
    assert 'Error' in avg_cmd('avg abc vac')

def test():
    cmd = None
    try:
        for cmd in [test_file_cmd, test_info_cmd, test_words_cmd, test_sum_cmd, test_avg_cmd]:
            cmd()

        print('All tests are passed without any exception.')

    except AssertionError as e:
        print(f'The problem with output at {cmd}')

    except Exception as e:
        print('The problem that\'s not handled')
        print(e)


if __name__ == '__main__':
    test()
