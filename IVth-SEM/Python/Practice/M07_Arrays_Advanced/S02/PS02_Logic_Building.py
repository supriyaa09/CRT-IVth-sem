class MoveZeroesSolution:
    def moveZeroes(self, nums):
        insert_position = 0

        for index in range(len(nums)):
            if nums[index] != 0:
                nums[insert_position], nums[index] = nums[index], nums[insert_position]
                insert_position += 1


class PascalTriangleSolution:
    def generate(self, numRows):
        triangle = []

        for row_index in range(numRows):
            row = [1] * (row_index + 1)
            for col_index in range(1, row_index):
                row[col_index] = triangle[row_index - 1][col_index - 1] + triangle[row_index - 1][col_index]
            triangle.append(row)

        return triangle


class MissingNumberSolution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)




