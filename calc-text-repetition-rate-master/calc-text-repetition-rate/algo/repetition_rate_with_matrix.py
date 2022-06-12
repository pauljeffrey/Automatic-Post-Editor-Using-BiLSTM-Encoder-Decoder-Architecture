from .repeated_str_with_matrix import RepeatedStrWithMatrix


class RepetitionRateWithMatrix(object):
    def __init__(self, org_sentences, cmp_sentences):
        self._org_sentences = org_sentences
        self._cmp_sentences = cmp_sentences

    def calc(self):
        if (len(self._org_sentences) and len(self._cmp_sentences)):
            repeated_len = 0
            cmp_word_len = 0
            min_paras_len = min(len(self._org_sentences),
                                len(self._cmp_sentences))

            for i in range(min_paras_len):
                min_sentences_len = min(len(self._org_sentences[i]),
                                        len(self._cmp_sentences[i]))

                for j in range(min_sentences_len):
                    if (self._org_sentences[i][j] == self._cmp_sentences[i][j]
                        ):  # noqa
                        repeated_len += len(self._cmp_sentences[i][j])
                        cmp_word_len += len(self._cmp_sentences[i][j])
                    else:
                        inst = RepeatedStrWithMatrix(self._org_sentences[i][j],
                                                     self._cmp_sentences[i][j])
                        res = inst.get_res()

                        repeated_len += res['repeated_str_len']
                        cmp_word_len += res['cmp_str_len']

            rate = repeated_len / cmp_word_len

            return {'success': True, 'rate': rate}
        else:
            return {'success': False, 'err_msg': ''}
