def foo():
    """
    This is a description inside python function.
    """
    pass

def int_to_char(input_int=65):
    """
    Turn an integer to a character.
    """
    return chr(input_int)

def send_message(sender: str="janan0", recipient="janan1", message_body="hello, another me", priority=1) -> int:
    """
    Send a message to a recipient.

    :param str sender: The person sending the message
    :param str recipient: The body of the message
    :param str message_body: The body of the message
    :param priority: The priority of the message, can be a number 1-5
    :type priority: integer or None
    :return: the message id
    :rtype: int
    :raises ValueError: if the message_body exceeds 160 characters
    :raises TypeError: if the message_body is not a basestring
    """

print("below is the description of foo(): ")
print("-------------------------------------")
help(foo)
print("-------------------------------------")
help(send_message)
print("-------------------------------------")
print(int_to_char())
print(int_to_char(8))
print(int_to_char(65))