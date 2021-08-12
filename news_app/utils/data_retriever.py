from faculty_app.models import Departmant
from professor_app.models import *
from slider_app.models import Carousel, CarouselItem


def get_pp() -> list:
    all_pp = ProfessorPost.objects.all()

    first_four_pp = []
    deps = []

    for pp in all_pp:
        first_four_pp.append(pp)
        dep = Departmant.objects.get(head=pp.professor.id)
        deps.append(dep)
        if len(first_four_pp) == 4:
            break

    return first_four_pp, deps


def first_of_n(n: int, filter_item: object) -> list:
    """
    returns the first n number of filter_items with the post_style pf p_style

    return: list of carousel items
    """
    first_n = []

    x = filter_item.objects.filter(draft=True)

    for obj in x:
        first_n.append(obj)
        if len(first_n) == n:
            break

    return first_n



def retrieve_carousel() -> list:
    """
    returns all the carousel items belonging to the first active active carousel

    return: list of carousel items
    """
    carousel_items = []

    c = Carousel.objects.all().filter(is_active=True).first()

    for ci in CarouselItem.objects.all().filter(item_carousel=c):
        carousel_items.append(ci)

    return carousel_items

