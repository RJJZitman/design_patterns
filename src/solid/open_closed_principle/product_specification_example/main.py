from filters import FilterSpec
from product import Product, Color, Size
from specifications import ColorSpecification, SizeSpecification


if __name__ == "__main__":
    pear = Product('Pear', Color.GREEN, Size.SMALL)
    ball = Product('Ball', Color.GREEN, Size.MEDIUM)
    palace = Product('Palace', Color.BLUE, Size.LARGE)
    products = [pear, ball, palace]

    green = ColorSpecification(Color.GREEN)
    small = SizeSpecification(Size.SMALL)
    small_blue = small & ColorSpecification(Color.BLUE)

    print('Green products (new):')
    for p in FilterSpec.filter(items=products, spec=green):
        print(f' - {p.name} is green')

    print('Small products:')
    for p in FilterSpec.filter(items=products, spec=small):
        print(f' - {p.name} is small')

    print('Small blue items:')
    for p in FilterSpec.filter(items=products, spec=small_blue):
        print(f' - {p.name} is small and blue')
