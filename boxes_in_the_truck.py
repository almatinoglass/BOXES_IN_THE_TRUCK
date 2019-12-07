import math
length_of_track = 13.4
width_of_track = 2.45
height_of_track = 2.4
#Вычисление объема фуры
volume_of_track = length_of_track * width_of_track * height_of_track

language = input('Выберите язык: Русский - 1, Английский - 2/ Choose language: Russian - 1, English - 2')

if language=='1':
    while True:
        length_of_the_box = input('Введите длину коробки в метрах ')
        width_of_the_box = input('Введите ширину коробки в метрах ')
        height_of_the_box = input('Введите высоту коробки в метрах ')
        if float(length_of_the_box) > length_of_track or float(width_of_the_box) > width_of_track \
            or float(height_of_the_box) > height_of_track :
            print ('Ваша коробка не влезет в фуру! Введите новое значение')
        else:
            break

    #вычисление геометрического объема коробки
    geom_volume_of_the_box = round(float(length_of_the_box) * float(width_of_the_box) * float(height_of_the_box), 4)

    print('Геометрический объем коробки = ' + str(geom_volume_of_the_box) + ' куб. м')

    #Вычисление количества коробок вдоль каждой стороны при условии, что длинная сторона коробки расположена вдоль
    # длинной стороны фуры
    quantity_along_Long_side = math.floor(length_of_track / float(length_of_the_box))
    quantity_along_short_side = math.floor(width_of_track / float(width_of_the_box))
    quantity_up = math.floor(height_of_track / float(height_of_the_box))

    quantity_in_the_track_al = quantity_along_Long_side * quantity_along_short_side * quantity_up
    print('Количество в фуре при расположении вдоль длинной стороны - ' + str(quantity_in_the_track_al) + ' штук')
    load_volume_along_length = round((volume_of_track / quantity_in_the_track_al), 4)
    print('Условный объем загрузки для коробки - ' + str(load_volume_along_length) + ' куб. м')

    # Вычисление количества коробок вдоль каждой стороны при условии, что длинная сторона коробки расположена вдоль
    # короткой стороны фуры
    try:
        quantity_w_along_Long_side = math.floor(length_of_track / float(width_of_the_box))
        quantity_l_along_short_side = math.floor(width_of_track / float(length_of_the_box))
        quantity_up = math.floor(height_of_track / float(height_of_the_box))

        quantity_in_the_track_aw = quantity_w_along_Long_side * quantity_l_along_short_side * quantity_up
        print('Количество в фуре при расположении вдоль короткой стороны - ' + str(quantity_in_the_track_aw) + ' шт.')
        load_volume_along_width = round((volume_of_track / quantity_in_the_track_aw), 4)
        print('Условный объем загрузки для коробки - ' + str(load_volume_along_width) + ' куб.м.')


    #Вычисляем разницу в процентах
        if (quantity_in_the_track_al > quantity_in_the_track_aw):
            quan = quantity_in_the_track_al - quantity_in_the_track_aw
            percentage = round((quan/quantity_in_the_track_aw) * 100, 2)
            print('При расположении вдоль длинной стороны в фуру войдет на ' + str(percentage) + ' процентов или на ' + str(quan) +
              ' больше коробок, чем при расположении вдоль короткой стороны фуры. ' )
        else:
            quan = quantity_in_the_track_aw - quantity_in_the_track_al
            percentage = round((quan/quantity_in_the_track_al) * 100, 2)
            print('При расположении вдоль короткой стороны в фуру войдет на ' + str(percentage) + ' процентов или на ' + str(quan) +
              ' больше коробок, чем при расположении вдоль длинной стороны фуры. ' )
    except:
        print('Расположение вдоль короткой стороны невозможно!')


elif language=='2':
    while True:
        length_of_the_box = input('Enter length of the box (m) ')
        width_of_the_box = input('Enter width of the box (m)')
        height_of_the_box = input('Enter height of the box (m)')
        if float(length_of_the_box) > length_of_track or float(width_of_the_box) > width_of_track \
                or float(height_of_the_box) > height_of_track:
            print('Your box did not fit in the truck! Please enter the correct dimensions!')
        else:
            break
    geom_volume_of_the_box = round(float(length_of_the_box) * float(width_of_the_box) * float(height_of_the_box), 4)

    print('Geometrical volume of the Box is = ' + str(geom_volume_of_the_box) + ' m**3')

    try:
        quantity_along_Long_side = math.floor(length_of_track / float(length_of_the_box))
        quantity_along_short_side = math.floor(width_of_track / float(width_of_the_box))
        quantity_up = math.floor(height_of_track / float(height_of_the_box))

        quantity_in_the_track_al = quantity_along_Long_side * quantity_along_short_side * quantity_up
        print('Amount in track when the Boxes placed along the long side - ' + str(quantity_in_the_track_al) + ' pcs.')
        load_volume_along_length = round((volume_of_track / quantity_in_the_track_al), 4)
        print('Conditional loading volume for a box - ' + str(load_volume_along_length) + ' m**3')

        quantity_w_along_Long_side = math.floor(length_of_track / float(width_of_the_box))
        quantity_l_along_short_side = math.floor(width_of_track / float(length_of_the_box))
        quantity_up = math.floor(height_of_track / float(height_of_the_box))


        quantity_in_the_track_aw = quantity_w_along_Long_side * quantity_l_along_short_side * quantity_up
        print('Amount in track when the Boxes placed along the short side - ' + str(quantity_in_the_track_aw) + ' pcs.')
        load_volume_along_width = round((volume_of_track / quantity_in_the_track_aw), 4)
        print('Conditional loading volume for a box - ' + str(load_volume_along_width) + ' m**3')
        if (quantity_in_the_track_al > quantity_in_the_track_aw):
            quan = quantity_in_the_track_al - quantity_in_the_track_aw
            percentage = round((quan/quantity_in_the_track_aw) * 100, 2)
            print('When the Boxes placed along the long side of truck, the Amount will be more on ' + str(percentage) +
              ' percents, or on ' + str(quan) + ' more boxes' )
        else:
            quan = quantity_in_the_track_aw - quantity_in_the_track_al
            percentage = round((quan/quantity_in_the_track_al) * 100, 2)
            print('When the Boxes placed along the short side of truck, the Amount will be more on ' + str(percentage) + ' percents, or on ' + str(quan) +
              ' more boxes' )
    except:
        print('Location along the short side is not possible!')
else:
    print('Попробуйте выбрать язык еще раз / Try to choose language one more time')



