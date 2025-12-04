import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        board_arr = np.array(board)
        for i in board:        #For Rows
            arr = np.array(i)
            nums = arr[arr != "."]
            if(nums.size != np.unique(nums).size):
                return False
        columns = [board_arr[:, i].tolist() for i in range(board_arr.shape[1])]
        for j in columns:      #For Columns
            arr = np.array(j)
            nums = arr[arr != "."]
            if(nums.size != np.unique(nums).size):
                return False

        one = board_arr[0:3 ,0:3]
        one_flat = one.flatten()
        nums = one_flat[one_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        two = board_arr[0:3 ,3:6]
        two_flat = two.flatten()
        nums = two_flat[two_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        three = board_arr[0:3 ,6:9]
        three_flat = three.flatten()
        nums = three_flat[three_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        four = board_arr[3:6 ,0:3]
        four_flat = four.flatten()
        nums = four_flat[four_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        five = board_arr[3:6 ,3:6]
        five_flat = five.flatten()
        nums = five_flat[five_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        six = board_arr[3:6 ,6:9]
        six_flat = six.flatten()
        nums = six_flat[six_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        seven = board_arr[6:9 ,0:3]
        seven_flat = seven.flatten()
        nums = seven_flat[seven_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        eight = board_arr[6:9 ,3:6]
        eight_flat = eight.flatten()
        nums = eight_flat[eight_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        nine = board_arr[6:9 ,6:9]
        nine_flat = nine.flatten()
        nums = nine_flat[nine_flat != "."]
        if(nums.size != np.unique(nums).size):
            return False

        return True
        
