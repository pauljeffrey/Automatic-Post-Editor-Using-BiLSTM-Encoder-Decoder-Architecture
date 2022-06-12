from .colourful_print import colourful_print


def handle_args(args, required_num):
    args_len = len(args) - 1

    if (args_len == required_num):
        return True
    elif (args_len < required_num):
        err_msg_former = ('ERROR: This program takes ' +
                          '{} positional arguments '.format(required_num))

        if (args_len <= 1):
            err_msg_latter = 'but {} was given.'.format(args_len)
        else:
            err_msg_latter = 'but {} were given.'.format(args_len)

        colourful_print('ERROR', err_msg_former + err_msg_latter)

        return False
