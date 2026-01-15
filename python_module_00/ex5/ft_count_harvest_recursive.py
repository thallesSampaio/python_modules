def ft_count_harvest_recursive(i=None, n=None):
    if i is None and n is None:
        n = int(input('Days till harvest: '))
        i = 1
    if i > n:
        print('Harvest time!')
        return
    print("Day", i)
    ft_count_harvest_recursive(i + 1, n)
