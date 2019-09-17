import random
factory_tweets = [
    'Good hotel not far from the city center & Kaliska railway station. Very good breakfast and friendly staff. The exterior could be better.',
    'The staff was good. Only instant coffee for breakfast no espresso.',
    'Location and kind staff. It was winter time, and the rooms weren\'t warm enough.',
    'Lovely Breakfast (buffet). Some staff were nice e.g. the twins, Central location (tram stop right in front of the hotel), Nearness to Piotrkowska street.'
    'Wifi was very poor, Accumulated dust, Poor quality toilet roll, some staff were not nice, smokey 8th floor.',
    'People made some noise during night that I could not sleep. However the location as well as the staff are great, value for money is more than fine.',
    'Location is perfect.Very dated needs a refurb, no flat screen tv, no coffee tea making facilities, breakfast was a joke,',
    'Location and cleanliness was a good side. Poor number of Tv programmes',
    'friendly staff, good price. Bad breakfast',
    'Very good location... ca. 200 meters from Piotrkowska street. Very good access to public transportation, namely trams. Good value for money...Breakfast could be much better, as well the wi-fi connection.',
    'Only the location is good. Completely to old hotel, expansive ( with the same price you can find other hotels of big groups). There was not hairdryer, poor products for the bathroom, comune rooms like a sauna'
]

factory_comments = 50 * [
    'Excellent bed and shower. Great location. Real jems within one block: restaurants, wine shop, jazz venue. Breakfast room gets crowded closer to 10:30 but is still friendly and social.',
    'Room was clean and staff was friendly and helpful. Breakfast could be bit more diverse.',
    'Near La Rambla so a good position kind Staff , nice room .generally Clean and the breakfast was quite various',
    'Great location. Bed sheets not changed for duration of stay. Didn’t like being told we only had five minutes to finish our breakfasts. Very cold and clinical feel to the place - I don’t think the floor that’s painted black vinyl helps.'
]

tweets = [*50 * factory_comments, *50 * factory_tweets]

def processed_tweets():
    return random.sample(tweets, random.randint(25, 100))