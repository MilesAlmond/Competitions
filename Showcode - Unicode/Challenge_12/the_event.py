class Solution:

    def calculate_difference(self, input):
        smallest = sorted(input)
        largest = sorted(input,reverse=True)
        i = 1
        while smallest[0] == 0:
            smallest[0], smallest[i] = smallest[i], smallest[0]
            i = i + 1
        smallest_num = int(''.join(map(str,smallest)))
        largest_num = int(''.join(map(str,largest)))
        result = largest_num - smallest_num
        return(result)
