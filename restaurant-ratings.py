def restaurant_ratings(input_filename):
    file = open(input_filename)
    restaurant_ratings = {}
    for line in file:
        line = line.strip()
        place_score = line.split(":")
        place = place_score[0]
        score = place_score[1]
        restaurant_ratings[place] = score

    # for place, score in restaurant_ratings.items():
    #     print "%s: %s" %(place, score)

    sorted_places = sorted(restaurant_ratings)
    
    for restaurant in sorted_places:
        print "%s is rated at %s" %(restaurant, restaurant_ratings[restaurant])

restaurant_ratings('scores.txt')