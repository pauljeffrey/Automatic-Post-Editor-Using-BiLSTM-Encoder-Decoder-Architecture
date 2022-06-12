class RepeatedStrWithMatrix(object):
    """ Using matrix to get all common parts between two strings

    Calculate all common parts between the original string and
    another string to compared with.
    Implemented by using matrix.
    """
    def __init__(self, _org_str, _cmp_str):
        self._org_str = _org_str
        self._org_str_len = len(_org_str)
        self._cmp_str = _cmp_str
        self._cmp_str_len = len(_cmp_str)
        self._res_lst = []

        self._init_matrix()
        self._calc_res_lst()

    def _init_matrix(self):
        """Init matrix"""
        self._matrix = [[0] * self._org_str_len
                        for _ in range(self._cmp_str_len)]

    def _calc_res_lst(self):
        """Calculate common parts"""
        for i, str2_val in enumerate(self._cmp_str):
            for j, str1_val in enumerate(self._org_str):
                if str1_val == str2_val:
                    val = self._matrix[i - 1][j - 1] + 1 if i and j else 1
                    self._matrix[i][j] = val
                if i and j:
                    if self._matrix[i - 1][j - 1] and not self._matrix[i][j]:
                        self._push_res(i, j)
                if i == self._cmp_str_len - 1 or j == self._org_str_len - 1:
                    if self._matrix[i][j] != 0:
                        self._push_res(i + 1, j + 1)

    def _push_res(self, i, j):
        length = self._matrix[i - 1][j - 1]

        if length > 1:
            self._res_lst.append(self._org_str[j - length:j])

    def get_res(self):
        repeated_str_len = len(''.join(self._res_lst))

        return {
            'org_str': self._org_str,
            'cmp_str': self._cmp_str,
            'cmp_str_len': self._cmp_str_len,
            'res_lst': self._res_lst,
            'repeated_str_len': repeated_str_len
        }
