from slider_app.models import Carousel, CarouselItem
from sidebar_app.models import Sidebar, SidebarItem


def first_of_n(n, filter_item, p_style):
    """
    returns the first n number of filter_items with the post_style pf p_style

    return: list of carousel items
    """
    first_n = []

    x = filter_item.objects.filter(post_style=p_style, draft=True)

    for obj in x:
        first_n.append(obj)
        if len(first_n) == n:
            break

    return first_n


def first_of_lectures(n, filter_item, l_type):
    """
    returns the first n number of filter_items with the lecture_type pf l_style

    return: list of carousel items
    """
    first_of_l = []

    x = filter_item.objects.filter(lecture_type=l_type, draft=True)

    for obj in x:
        first_of_l.append(obj)
        if len(first_of_l) == n:
            break

    return first_of_l


def retrieve_carousel():
    """
    returns all the carousel items belonging to the first active active carousel

    return: list of carousel items
    """
    carousel_items = []

    c = Carousel.objects.all().filter(is_active=True).first()

    for ci in CarouselItem.objects.all().filter(item_carousel=c):
        carousel_items.append(ci)

    return carousel_items


def first_sidebar():
    pass