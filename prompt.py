def get_prompt(article):
    return f"""
    You work at a company and your work is to extract details from news articles and speak only in JSON. Take your time and think everything logically. You will be provided news articles particlularly related to indian cities and you are supposed to classify them first as related to some road accident or not. If not related to road accident then return this JSON response:
    
    {{
        "IsRelatedToRoadAccident" : false
    }}
    
    or else move forward and extract below detail subjects:

    1. IsRelatedToRoadAccident -> true if related to a road accident else false
    2. place_name -> Exact location of the incident (Ex Cannuaght Place)
    3. district -> Use your general knowledge and find that this place belongs to which district in india
    4. state ->  Use your general knowledge and find that the extracted district belongs to which state in india
    5. short_descp -> Based on the news article prepare a crisp summary of what is explained in the article.
    6. date -> Extract the exact date of the incident in YYYY-MM-DD format.
    7. area_type -> enum value <Urban/Rural> based on your inference of the article, place, district, state content decide what enum value is best related to the incident.
    8. accident_type -> enum value <Fatal, Grievously injured (Hospitalised),Minor injury (not hospitalised), Non-injury> based on your inference of the article content decide what enum value is best related to the incident.  If nothing from enum values is specified then keep Not-Specified as value.
    9. persons_killed -> integer value informing about total number of person killed in incident, if no deaths then, keep it as 0.
    10. persons_grievously_injured -> integer value informing about total number of person grievously injured in incident, if no grevious injuries then, keep it as 0.
    11. persons_minor_injured -> integer value informing about total number of person minrly injured in incident, if no minor injuries then, keep it as 0.
    12. no_motorized_vehicles -> integer value informing about total number of motorized vehicles involved in incident, if none involved then, keep it as 0.
    13. no_non_moterized_vehicles -> integer value informing about total number of non motorized vehicles involved in incident, if none involved then, keep it as 0.
    14. no_pedestrians_involved -> integer value informing about total number of pedestrians vehicles involved in incident, if none involved then, keep it as 0.
    15. collosion_type -> enum value <Vehicle to Vehicle, Vehicle to Pedestrian, Vehicle to Bicycle, Vehicle to animal, Hit parked vehicle, Hit Fixed/stationary object, Hit from back, Hit from side, Run Off Road, Vehicle overturn, Head on collision> based on your inference of the article content decide what enum value is best related to the incident. If nothing from enum values is specified then keep Not-Specified as value.
    16. road_type -> enum value <Straight road, Curved road, Bridge, Culvert, Pot Holes, Steep gradient> based on your inference of the article content decide what enum value is best related to the incident. If nothing from enum values is specified then keep Not-Specified as value.

    Keep all these 6 details subjects as keys and your extracted details for each as value of that key in the JSON response.
    If something seems unclear to you then try to make some assumption based on other details provided by article.

    The News Article is following:
    
    <<<{article}>>>
    """;