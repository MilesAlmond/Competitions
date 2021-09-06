class Solution:

    def get_check_digit(self, input):
        import re
        matched = re.match("[0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-x",input)
        is_match = bool(matched)
        if (not is_match):
            answer = -1
        else:
            input_new = input.replace('-','')[:-1]
            check = 0
            for i in range(len(input_new)):
                check = check + ((i+1)*int(input_new[i]))
            answer = check % 11
        return(answer)
