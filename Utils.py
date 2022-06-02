from typing import List


def get_cls_name(elem) -> str:
    """Get the element's class name as a string

    Parameters
    ----------
    elem
        The element whose class name is to be obtained as a string

    Returns
    -------
    str
        Element class name as a string
    """
    full_cls_name = str(type(elem))
    cls_name = ''
    # We separate last two symbols "'>" from type(elem)
    for char in full_cls_name[-3::-1]:
        if char != '.':
            cls_name = char + cls_name
        else:
            break
    return cls_name


def get_clear_attr_names(elem) -> List[str]:
    """Get element attributes list without '_', '__', and class name

    Parameters
    ----------
    elem
        The element whose attributes are retrieved as a list

    Returns
    -------
    list
        List of element attributes without class name
    """
    clear_attr_names = []
    for attr in elem.__dict__.keys():
        clear_attr_name = attr.replace(get_cls_name(elem), '')
        clear_attr_names.append(clear_attr_name.lstrip('_'))
    return clear_attr_names
