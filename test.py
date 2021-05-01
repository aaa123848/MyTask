import unittest
import task1
import task2

class TestTaskOne(unittest.TestCase):

    def test_num_2_money(self):
        self.assertEqual(task1.num_2_money(9527), "9,527")
        self.assertEqual(task1.num_2_money(3345678), "3,345,678")
        self.assertEqual(task1.num_2_money(-1234.45), "-1,234.45")
        self.assertEqual(task1.num_2_money(0), "0")


class TestTaskTwo(unittest.TestCase):

    def test_pipe_num_incre(self):
        def incre(num):
            return num + 1
        self.assertEqual(task2.pipe(5, incre), 6)
        self.assertEqual(task2.pipe(5, incre, incre, incre), 8)
    def test_pipe_str_append(self):
        def str_append(word):
            return word + 'a'
        self.assertEqual(task2.pipe('', str_append), 'a')
        self.assertEqual(task2.pipe('', str_append, str_append, str_append), 'aaa')

if __name__ == '__main__':
    unittest.main()