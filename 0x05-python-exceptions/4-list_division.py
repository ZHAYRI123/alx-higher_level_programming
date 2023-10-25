#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    m_list = []
    a = 0
    while a < list_length:
        try:
            m_list[a] = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            m_list[a] = 0
        except IndexError:
            print("out of range")
            m_list[a] = 0
        except ZeroDivisionError:
            print("division by 0")
            m_list[a] = 0
        finally:
            a += 1
    return (m_list)
