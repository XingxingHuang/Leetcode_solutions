class Bank:
    def __init__(self):
        self.changes = {5: 0, 10: 0, 20: 0}

    def get_total(self):
        return sum([k*v for k,v in self.changes.items()])

    def change(self, bill):
        assert bill in [5,10,20], 'unaccepted bill amount {}'.format(bill)
        self.changes[bill] += 1
        bill -= 5
        while bill >= 10 and self.changes[10] > 0:
            bill -= 10
            self.changes[10] -= 1
        while bill >= 5 and self.changes[5] > 0:
            bill -= 5
            self.changes[5] -= 1
        return bill == 0

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        my_bank = Bank()

        for bill in bills:
            # print('bill {}, bank {}'.format(bill, my_bank.changes))
            can_change = my_bank.change(bill)
            # print('can change? {} updated bank {}'.format(can_change, my_bank.changes))
            if not can_change:
                return False
        return True


if __name__ == '__main__':
    cases = [
        [5,5,10],
        [10,10],
        [5,5,10,10,20],
        [5,5,5,5,20,20,5,5,20,5]
    ]
    answers = [True, False, False, False]
    for case, answer in zip(cases, answers):
        print('case {} returned {}, and the expected is {}'.format(case, Solution().lemonadeChange(case), answer))
