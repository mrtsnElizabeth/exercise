class CombinationsList:
    @staticmethod
    def get_combinations(my_list):
        """
        :param self:
        :param my_list: list
        :return: list[list]
        """
        result = []
        def fun_combination(current_number):
            if current_number >= len(my_list):
                result.append(my_list)
                return result
            if current_number == 0:
                result.append([])
                return fun_combination(current_number+1)

            for ind, element in enumerate(my_list):
                combination = [element]
                if current_number == 1:
                    result.append(combination)
                    continue
                for ind2, element2 in enumerate(my_list):
                    if ind2 < ind + 1:
                        continue
                    combination.append(element2)
                    if current_number == len(combination):
                        result.append(combination)
                        combination = [element]
            return fun_combination(current_number+1)
        return fun_combination(0)


print('Combinations:', CombinationsList().get_combinations([1, 2, 'a']))