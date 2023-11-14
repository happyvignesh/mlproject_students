import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] " \
                    f"error message[{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message_from_user, error_detail: sys):
        super().__init__(error_message_from_user)
        self.error_message = error_message_detail(error_message_from_user, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)