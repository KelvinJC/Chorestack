def get_page_indices(page, paginator):
    try:
        leftIndex = (int(page) - 3)
    except TypeError:
        leftIndex = 1

    if leftIndex < 1:
        leftIndex = 1
    
    try:
        rightIndex = (int(page) + 3)
    except TypeError:
        rightIndex = 9
    
    if leftIndex == 1:
        rightIndex = 6   

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    return leftIndex, rightIndex
