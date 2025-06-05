from database_ops import *
from dotenv import load_dotenv


# ----------------------------------------------------------------------------------------------
# Initializations Section:
# ----------------------------------------------------------------------------------------------

load_dotenv()
DB_MODE = os.environ.get("DB_MODE")

if DB_MODE == 'local':
    print('Using Local MySQL Database')

elif DB_MODE == 'remote':
    print('Using Remote MySQL Database')

else:
    print('DB_MODE not set correctly in .env file.')
    exit(1)
print()

# Clear entire database:
print("Clearing database...")
clear_db()

# Create tables:
print("Creating tables...")
create_locations()
print(f"\t - Created Locations table")
create_location_details()
print(f"\t - Created Location Details table")
create_maps()
print(f"\t - Created Maps table")
create_languages()
print(f"\t - Created Languages table")
create_countries()
print(f"\t - Created Countries table")


# ----------------------------------------------------------------------------------------------
# Fill the countries table:
# ----------------------------------------------------------------------------------------------

print("\n\n Inserting countries...")
insert_country(name="India", code="IN", flag='🇮🇳')
insert_country(name="France", code="FR", flag='🇫🇷')
insert_country(name="Germany", code="DE", flag='🇩🇪')
insert_country(name="All Locations", code="ALL", flag='🌍')
print(f'\t - Inserted 4 countries: India, France, Germany, All Locations')


# ----------------------------------------------------------------------------------------------
# Fill the languages table:
# ----------------------------------------------------------------------------------------------

print("\n\n Inserting languages...")
insert_language(name="English", code="en")
insert_language(name="Hindi", code="hi")
insert_language(name="French", code="fr")
insert_language(name="German", code="de")
insert_language(name="Marathi", code="mr")
insert_language(name="Tamil", code="ta")
print(f'\t - Inserted 6 languages: English, Hindi, French, German, Marathi, Tamil')


# ----------------------------------------------------------------------------------------------
# Fill Locations Table:
# ----------------------------------------------------------------------------------------------

print("\n\n Inserting locations...")

# India:
print('\t India')

# Taj Mahal:
insert_location(
    id=1, name="Taj Mahal",
    location="Agra, Uttar Pradesh", country_code="IN",
    image="taj_mahal.jpg", image2="taj_mahal_2.jpg",
    image3="taj_mahal_3.jpg", image4="taj_mahal_4.jpg"
)
print(f'\t - Inserted Location-{1:02} : Taj Mahal')

# Jaipur City Palace:
insert_location(
    id=2, name="Jaipur City Palace",
    location="Jaipur, Rajasthan", country_code="IN",
    image="jaipur_palace.jpg", image2="jaipur_palace_2.jpg",
    image3="jaipur_palace_3.jpg", image4="jaipur_palace_4.jpg"
)
print(f'\t - Inserted Location-{2:02} : Jaipur City Palace')

# Mysore Palace:
insert_location(
    id=3, name="Mysore Palace",
    location="Mysore, Karnataka", country_code="IN",
    image="mysore_palace.jpg", image2="mysore_palace_2.jpg",
    image3="mysore_palace_3.jpg", image4="mysore_palace_4.jpg"
)
print(f'\t - Inserted Location-{3:02} : Mysore Palace')

# Ellora Caves:
insert_location(
    id=4, name="Ellora Caves",
    location="Aurangabad, Maharashtra", country_code="IN",
    image="ellora_caves_3.jpg", image2="ellora_caves_2.jpg",
    image3="ellora_caves.jpg", image4="ellora_caves_4.jpg"
)
print(f'\t - Inserted Location-{4:02} : Ellora Caves')

# Gateway of India:
insert_location(
    id=5, name="Gateway of India",
    location="Mumbai, Maharashtra", country_code="IN",
    image="gateway_of_india.jpg", image2="gateway_of_india_2.jpg",
    image3="gateway_of_india_3.jpg", image4="gateway_of_india_4.jpg"
)
print(f'\t - Inserted Location-{5:02} : Gateway of India')

# Kaziranga National Park:
insert_location(
    id=6, name="Kaziranga National Park",
    location="Assam, Northeast India", country_code="IN",
    image="kaziranga.jpg", image2="kaziranga_2.jpg",
    image3="kaziranga_3.jpg", image4="kaziranga_4.jpg"
)
print(f'\t - Inserted Location-{6:02} : Kaziranga National Park')

# ----------------------------------------------------------------------------------------------

# France : 
print('\t France')

# Bordeaux Place:
insert_location(
    id=7, name="Bordeaux Place",
    location="Bordeaux, Nouvelle-Aquitaine", country_code="FR",
    image="bordeaux_place.jpg", image2="bordeaux_place_2.jpg",
    image3="bordeaux_place_3.jpg", image4="bordeaux_place_4.jpg"
)
print(f'\t - Inserted Location-{7:02} : Bordeaux Place')

# Eiffel Tower:
insert_location(
    id=8, name="Eiffel Tower",
    location="Paris, Île-de-France", country_code="FR",
    image="eiffel_tower.jpg", image2="eiffel_tower_2.jpg",
    image3="eiffel_tower_3.jpg", image4="eiffel_tower_4.jpg"
)
print(f'\t - Inserted Location-{8:02} : Eiffel Tower')

# French Riviera:
insert_location(
    id=9, name="French Riviera",
    location="Côte d'Azur, Provence-Alpes-Côte d'Azur", country_code="FR",
    image="french_riviera.jpg", image2="french_riviera_2.jpg",
    image3="french_riviera_3.jpg", image4="french_riviera_4.jpg"
)
print(f'\t - Inserted Location-{9:02} : French Riviera')

# Loire Valley:
insert_location(
    id=10, name="Loire Valley",
    location="Loire Valley, Centre-Val de Loire", country_code="FR",
    image="loire_valley.jpg", image2="loire_valley_2.jpg",
    image3="loire_valley_3.jpg", image4="loire_valley_4.jpg"
)
print(f'\t - Inserted Location-{10:02} : Loire Valley')

# Palace of Versailles
insert_location(
    id=11, name="Palace of Versailles",
    location="Versailles, Île-de-France", country_code="FR",
    image="palace_of_versailles.jpg", image2="palace_of_versailles_2.jpg",
    image3="palace_of_versailles_3.jpg", image4="palace_of_versailles_4.jpg"
)
print(f'\t - Inserted Location-{10:02} : Loire Valley')

# Mont Saint Michel
insert_location(
    id=12, name="Mont Saint Michel",
    location="Normandy, Manche", country_code="FR",
    image="mont_saint_michel.jpg", image2="mont_saint_michel_2.jpg",
    image3="mont_saint_michel_3.jpg", image4="mont_saint_michel_4.jpg"
)
print(f'\t - Inserted Location-{11:02} : Palace of Versailles')

# ----------------------------------------------------------------------------------------------

# Germany: 
print('\t Germany')

# Allgäu Valley
insert_location(
    id=13, name="Allgäu Valley",
    location="Bavaria, Germany", country_code="DE",
    image="allgau_valley.jpg", image2="allgau_valley_2.jpg",
    image3="allgau_valley_3.jpg", image4="allgau_valley_4.jpg"
)
print(f'\t - Inserted Location-{12:02} : Mont Saint Michel')

# Brandenburg Gate
insert_location(
    id=14, name="Brandenburg Gate",
    location="Berlin, Germany", country_code="DE",
    image="brandenburg_gate.jpg", image2="brandenburg_gate_2.jpg",
    image3="brandenburg_gate_3.jpg", image4="brandenburg_gate_4.jpg"
)
print(f'\t - Inserted Location-{13:02} : Allgäu Valley')

# Cologne Cathedral
insert_location(
    id=15, name="Cologne Cathedral",
    location="Cologne, North Rhine-Westphalia, Germany", country_code="DE",
    image="cologne_cathedral.jpg", image2="cologne_cathedral_2.jpg",
    image3="cologne_cathedral_3.jpg", image4="cologne_cathedral_4.jpg"
)
print(f'\t - Inserted Location-{14:02} : Brandenburg Gate')

# Lake Königssee
insert_location(
    id=16, name="Lake Königssee",
    location="Berchtesgaden, Bavaria, Germany", country_code="DE",
    image="lake_koenigssee.jpg", image2="lake_koenigssee_2.jpg",
    image3="lake_koenigssee_3.jpg", image4="lake_koenigssee_4.jpg"
)
print(f'\t - Inserted Location-{15:02} : Cologne Cathedral')

# Neuschwanstein Castle
insert_location(
    id=17, name="Neuschwanstein Castle",
    location="Schwangau, Bavaria, Germany", country_code="DE",
    image="neuschwanstein_castle.jpg", image2="neuschwanstein_castle_2.jpg",
    image3="neuschwanstein_castle_3.jpg", image4="neuschwanstein_castle_4.jpg"
)
print(f'\t - Inserted Location-{16:02} : Lake Königssee')

# Reichstag Dome
insert_location(
    id=18, name="Reichstag Dome",
    location="Berlin, Germany", country_code="DE",
    image="reichstag_dome.jpg", image2="reichstag_dome_2.jpg",
    image3="reichstag_dome_3.jpg", image4="reichstag_dome_4.jpg"
)
print(f'\t - Inserted Location-{17:02} : Neuschwanstein Castle')


# ----------------------------------------------------------------------------------------------
# Fill location details:
# ----------------------------------------------------------------------------------------------

print("\n\n Inserting location details...")

print("\t India")

# Taj Mahal
insert_location_details(
    location_id=1,
    description_intro="The Taj Mahal, located in Agra, India, is one of the most iconic monuments in the world and a symbol of love. Built in the 17th century by Mughal Emperor Shah Jahan, this stunning white marble mausoleum was dedicated to his beloved wife, Mumtaz Mahal. Its architectural beauty and intricate details draw millions of visitors each year, making it a UNESCO World Heritage site and one of the New Seven Wonders of the World.",
    description_history="The history of the Taj Mahal dates back to 1632 when Emperor Shah Jahan commissioned the construction in memory of his wife, Mumtaz Mahal, who passed away during childbirth. The mausoleum took about 22 years to complete, involving thousands of artisans, craftsmen, and architects. It is said that Shah Jahan spared no expense, importing the finest materials from across India and Asia, including white marble, precious stones, and intricate carvings. After Shah Jahan’s death, he was laid to rest beside Mumtaz Mahal in the tomb, fulfilling his vision of an eternal resting place for the two lovers.",
    description_highlights="Highlights of the Taj Mahal include the beautiful gardens with fountains leading up to the monument, the intricate marble inlay work featuring semi-precious stones, and the central dome that towers over the tomb. The building’s symmetry, combined with its reflection in the pool, is truly mesmerizing. The Taj Mahal also boasts four minarets and impressive calligraphy of Quranic verses along its walls. Visiting during sunrise or sunset can enhance the experience, as the monument's marble surface reflects different hues in varying lights.",
    description_tips="Visit early in the morning to avoid crowds and enjoy the best lighting. Be mindful of restricted areas, and avoid bringing large bags or food items, as these are not allowed inside. Hiring a local guide can enhance your visit by providing insight into the monument’s history and architecture."
)
print(f'\t - Added details for Location-{1:02} : Taj Mahal')

# Jaipur City Palace
insert_location_details(
    location_id=2,
    description_intro="The Jaipur City Palace is a grand complex of palaces, courtyards, and museums in Jaipur, Rajasthan. It showcases a unique blend of Mughal and Rajput architectural styles, offering visitors a glimpse into the royal heritage and cultural richness of the region. Constructed in the early 18th century, this palace still serves as a residence for Jaipur’s royal family and remains a must-visit attraction in the 'Pink City'.",
    description_history="Jaipur City Palace was established by Maharaja Sawai Jai Singh II, the founder of Jaipur, as a part of his vision for the new city in 1727. This elaborate complex was designed with a combination of Rajput, Mughal, and European architectural influences. The palace served as the royal residence and administrative center, hosting events, ceremonies, and royal gatherings. Successive rulers continued to add to its grandeur, creating an intricate network of courtyards, temples, and gardens, each showcasing unique artistic styles and historical significance.",
    description_highlights="Key highlights of the Jaipur City Palace include the Mubarak Mahal, with its collection of textiles and royal garments, and the Chandra Mahal, which houses royal artifacts and stunning frescoes. The Pritam Niwas Chowk courtyard is known for its intricately painted doorways, representing the four seasons. The museum within the complex offers insight into the rich cultural heritage of Jaipur, displaying royal artifacts, manuscripts, and artwork.",
    description_tips="Plan your visit in the morning to enjoy a quieter experience. Guided tours are available, providing historical insights. Be sure to dress respectfully, as some areas require traditional attire."
)
print(f'\t - Added details for Location-{2:02} : Jaipur City Palace')

# Mysore Palace
insert_location_details(
    location_id=3,
    description_intro="Mysore Palace, located in Karnataka, India, is one of the most visited palaces in the country. Known for its Indo-Saracenic architecture and intricate interiors, this royal residence once belonged to the Wodeyar dynasty. With its impressive façade, grand halls, and vibrant festivals, Mysore Palace captures the essence of Karnataka's rich cultural heritage.",
    description_history="The original Mysore Palace was constructed in the 14th century but has been rebuilt several times due to damage from invasions and fires. The current palace was designed by British architect Henry Irwin in 1912, blending Hindu, Muslim, Rajput, and Gothic architectural elements to create a unique Indo-Saracenic style. The palace served as the seat of the Wodeyar Maharajas, who ruled Mysore for over five centuries, and was a focal point for cultural and political activities in the region.",
    description_highlights="Visitors to Mysore Palace can explore the Durbar Hall with its intricately carved pillars, the Kalyana Mantapa with beautiful stained glass ceilings, and the Ambavilasa hall, known for its impressive gold doors. During the annual Dussehra festival, the palace is illuminated with thousands of lights, creating a stunning spectacle. The palace grounds also host a museum displaying artifacts from the royal family.",
    description_tips="Plan to visit in the late afternoon to experience the palace’s illumination at night. Photography is allowed outside, but it is restricted within the interiors. Consider visiting during Dussehra for a special experience."
)
print(f'\t - Added details for Location-{3:02} : Mysore Palace')

# Ellora Caves
insert_location_details(
    location_id=4,
    description_intro="The Ellora Caves in Maharashtra are a remarkable complex of rock-cut temples and monasteries, reflecting the harmonious coexistence of Hinduism, Buddhism, and Jainism in ancient India. Dating back to 600-1000 AD, Ellora is a UNESCO World Heritage site, known for its impressive architecture, artistry, and historical significance.",
    description_history="The Ellora Caves were carved over several centuries by skilled artisans and represent three major religious traditions of ancient India: Hinduism, Buddhism, and Jainism. The Kailasa Temple, one of the largest rock-cut temples in the world, is a masterpiece dedicated to Lord Shiva. Built in the 8th century under the patronage of the Rashtrakuta dynasty, it is known for its scale and architectural detail. The complex also includes Buddhist monasteries and Jain temples, each adorned with intricate carvings, statues, and pillars that showcase the spiritual and cultural synthesis of the time.",
    description_highlights="Highlights of the Ellora Caves include the Kailasa Temple, with its massive monolithic structure, the Buddhist viharas with their beautiful sculptures of Buddha, and the Jain caves showcasing intricate depictions of the Tirthankaras. The carvings in each cave are highly detailed, and exploring them offers a glimpse into ancient art and religious practices.",
    description_tips="Wear comfortable shoes, as the cave complex is extensive. A flashlight can be useful for viewing intricate details in dimly lit areas. Consider hiring a guide to fully appreciate the history and significance of each cave.",
)
print(f'\t - Added details for Location-{4:02} : Ellora Caves')

# Gateway of India
insert_location_details(
    location_id=5,
    description_intro="The Gateway of India, located in Mumbai, Maharashtra, is an iconic monument overlooking the Arabian Sea. Built to commemorate the visit of King George V and Queen Mary in 1911, this grand archway has become a symbol of Mumbai's rich history and resilience. It serves as a popular tourist attraction and a place for cultural gatherings.",
    description_history="Constructed in 1924, the Gateway of India was designed by architect George Wittet in the Indo-Saracenic style, combining Hindu, Muslim, and European architectural elements. It was originally intended as a ceremonial entrance for British Viceroys and other dignitaries arriving by sea. Over time, it became a symbol of India's colonial history, witnessing significant events, including the departure of the last British troops in 1948, marking India's independence.",
    description_highlights="The Gateway of India is known for its grand design, with an impressive central dome and intricate carvings on its basalt structure. It offers stunning views of the Arabian Sea and is situated near the iconic Taj Mahal Palace hotel. The site is especially beautiful in the evening when it is illuminated, and it provides a bustling atmosphere filled with street vendors and local artists.",
    description_tips="Visit early in the morning or late in the evening to avoid crowds. The area around the Gateway is bustling, so plan to spend some time exploring the nearby attractions, including ferry rides to Elephanta Caves."
)
print(f'\t - Added details for Location-{5:02} : Gateway of India')

# Kaziranga National Park
insert_location_details(
    location_id=6,
    description_intro="Kaziranga National Park is a UNESCO World Heritage Site located in the state of Assam, India. It is home to the largest population of one-horned rhinoceroses in the world. Spanning over 1,000 square miles, the park is rich in biodiversity, including tigers, elephants, wild buffalo, and various species of birds. It is a crucial part of the Assam Valley's ecosystem and offers a unique glimpse into India's wildlife conservation efforts.",
    description_history="The park was established in 1905, initially as a forest reserve, and later declared a national park in 1974. Kaziranga has been a pioneer in rhino conservation, with the population of the one-horned rhino significantly increasing over the years. The park has faced many challenges, including poaching and floods, but continues to thrive due to its rigorous conservation practices.",
    description_highlights="Kaziranga is known for its vast grasslands, dense forests, and wetland areas. The park's most famous inhabitants are the one-horned rhinoceros, but it is also home to tigers, elephants, wild buffaloes, and hundreds of bird species. Visitors can enjoy jeep and elephant safaris to explore the diverse wildlife, and the park’s annual census of rhinos is a major event.",
    description_tips="When visiting Kaziranga, it's best to go between November and April, as the weather is more favorable for safaris. Be prepared for an early start for safaris, as the animals are most active in the morning. If you are traveling by road, ensure to check the conditions, as floods can sometimes affect the area. Also, carry binoculars for birdwatching and a good camera to capture the stunning landscapes and wildlife."
)
print(f'\t - Added details for Location-{6:02} : Kaziranga National Park')

# ----------------------------------------------------------------------------------------------

# France:
print("\t France")
# Bordeaux Place
insert_location_details(
    location_id=7,
    description_intro="Bordeaux is a port city in southwestern France, renowned for its exceptional wine production and stunning 18th-century architecture. The city is situated along the Garonne River and is often referred to as the 'wine capital of the world.' Bordeaux offers a mix of historical landmarks and modern attractions, making it a cultural and culinary hub in France.",
    description_history="Bordeaux has a rich history dating back to Roman times when it was known as Burdigala. Over centuries, the city flourished as a major trade hub, especially for wine. Its historic center, the Port of the Moon, is a UNESCO World Heritage Site and showcases impressive architecture from the Age of Enlightenment.",
    description_highlights="Bordeaux is famous for its vineyards and wine tours, with some of the best wineries located in nearby regions like Médoc and Saint-Émilion. Key attractions include Place de la Bourse, the Bordeaux Cathedral, and the stunning waterfront along the Garonne River. The city also hosts vibrant wine festivals and culinary events throughout the year.",
    description_tips="Visit Bordeaux during the spring or autumn months for pleasant weather and fewer crowds. Don't miss a stroll along the Miroir d'eau, a unique water mirror reflecting the city's architecture. If you're a wine enthusiast, book a guided tour of the vineyards and châteaux. Comfortable walking shoes are essential, as Bordeaux is best explored on foot."
)
print(f'\t - Added details for Location-{7:02} : Bordeaux Place')

# Eiffel Tower
insert_location_details(
    location_id=8,
    description_intro="The Eiffel Tower is an iconic symbol of France, located in the heart of Paris. Standing at 330 meters tall, this iron lattice tower was built for the 1889 World's Fair and has since become one of the most visited landmarks in the world. It offers breathtaking views of Paris from its observation decks.",
    description_history="Constructed by Gustave Eiffel's engineering company, the Eiffel Tower was initially criticized by Parisians but later gained worldwide acclaim. It was the tallest man-made structure in the world until 1930 and played a crucial role in technological advancements, including early radio transmission.",
    description_highlights="The tower features three levels accessible by elevator or stairs. Visitors can dine at the restaurants on the first and second levels or enjoy panoramic views from the top observation deck. At night, the Eiffel Tower sparkles with lights, offering a magical experience.",
    description_tips="Buy tickets online in advance to skip long queues, especially during peak tourist seasons. Visit in the early morning or late evening for fewer crowds and stunning views. Wear comfortable shoes, as climbing the stairs is a popular option for adventurous visitors."
)
print(f'\t - Added details for Location-{8:02} : Eiffel Tower')

# French Riviera
insert_location_details(
    location_id=9,
    description_intro="The French Riviera, or Côte d'Azur, is a glamorous stretch of Mediterranean coastline in southeastern France. Known for its luxury resorts, pristine beaches, and vibrant cultural scene, the Riviera attracts celebrities, artists, and tourists from around the world.",
    description_history="The French Riviera gained prominence in the late 19th century as a winter retreat for European aristocracy. Over time, it evolved into a year-round destination, with cities like Nice, Cannes, and Monaco becoming synonymous with luxury and sophistication.",
    description_highlights="The Riviera boasts stunning beaches, scenic coastal drives, and world-famous events like the Cannes Film Festival. Visitors can explore charming towns like Saint-Tropez and Èze or enjoy the vibrant nightlife and casinos in Monte Carlo.",
    description_tips="Visit during spring or early autumn to avoid the summer crowds while still enjoying warm weather. Pack swimwear and sunscreen for beach outings and comfortable attire for exploring picturesque villages. Public transport, including trains and buses, is a convenient way to travel between towns."
)
print(f'\t - Added details for Location-{9:02} : French Riviera')

# Loire Valley
insert_location_details(
    location_id=10,
    description_intro="The Loire Valley, often called the 'Garden of France,' is a region known for its magnificent châteaux, lush vineyards, and picturesque landscapes. Located in central France, the valley is a UNESCO World Heritage Site and a popular destination for history and wine enthusiasts.",
    description_history="The Loire Valley has been a center of French culture and royalty since the Renaissance. Many of its iconic châteaux, such as Château de Chambord and Château de Chenonceau, were built during this era as symbols of power and artistic achievement.",
    description_highlights="Highlights of the Loire Valley include visits to its historic castles, wine tasting tours, and exploring charming villages. The region is also home to stunning gardens and offers outdoor activities like cycling along the Loire River.",
    description_tips="Spring and summer are the best times to visit for vibrant scenery and outdoor events. Plan your itinerary to include guided tours of the major châteaux. Renting a bike is a great way to explore the region at your own pace."
)
print(f'\t - Added details for Location-{10:02} : Loire Valley')

# Palace of Versailles
insert_location_details(
    location_id=11,
    description_intro="The Palace of Versailles is a masterpiece of French Baroque architecture and a symbol of absolute monarchy. Located near Paris, it was the royal residence of Louis XIV, the Sun King, and remains one of France's most visited historical landmarks.",
    description_history="Originally a hunting lodge, Versailles was transformed by Louis XIV into a grand palace in the late 17th century. It became the seat of political power and a center of art and culture during his reign. The Treaty of Versailles, ending World War I, was signed here.",
    description_highlights="Visitors can explore the Hall of Mirrors, the King's and Queen's apartments, and the sprawling gardens designed by André Le Nôtre. The Musical Fountain Shows and the Grand Trianon are must-see attractions within the estate.",
    description_tips="Purchase tickets online to avoid long lines and consider booking a guided tour for in-depth historical insights. Arrive early to beat the crowds, and set aside ample time to explore both the palace and its gardens. Wear comfortable shoes for walking."
)
print(f'\t - Added details for Location-{11:02} : Palace of Versailles')

# Mont Saint Michel
insert_location_details(
    location_id=12,
    description_intro="Mont Saint Michel is a medieval abbey perched on a rocky island in Normandy, France. Surrounded by tidal waters, it offers breathtaking views and a unique blend of history and natural beauty. The island is connected to the mainland by a causeway, making it an iconic destination.",
    description_history="The abbey was founded in the 8th century and became a major pilgrimage site during the Middle Ages. Over the centuries, it has served as a fortress, a religious center, and a symbol of French resilience. Mont Saint Michel is now a UNESCO World Heritage Site.",
    description_highlights="Highlights include the stunning Gothic abbey, the quaint village streets, and panoramic views of the bay. Visitors can also witness the dramatic tidal changes that surround the island, creating an otherworldly atmosphere.",
    description_tips="Visit during low tide for easier access and explore the abbey early in the day to avoid crowds. Wear sturdy shoes for walking on uneven paths, and check tide schedules to plan your visit. Guided tours offer fascinating insights into the site's history."
)
print(f'\t - Added details for Location-{12:02} : Mont Saint Michel')

# ----------------------------------------------------------------------------------------------

# Germany:
print("\t Germany")

# Allgäu Valley
insert_location_details(
    location_id=13,
    description_intro="The Allgäu Valley is a picturesque region in Bavaria, Germany, known for its breathtaking alpine landscapes, rolling meadows, and charming villages. It's a popular destination for hiking, skiing, and experiencing authentic Bavarian culture.",
    description_history="The Allgäu Valley has a rich cultural heritage, with its origins tracing back to ancient settlements. Over the centuries, it has been a hub for agriculture, particularly dairy farming. The region's distinct architecture and traditions reflect its deep Bavarian roots.",
    description_highlights="The valley is famous for its hiking trails, especially around the Nebelhorn and Fellhorn mountains. Visitors can also explore the traditional alpine huts, enjoy locally made cheese, and take in the stunning views of the Bavarian Alps.",
    description_tips="Visit during the summer for hiking or winter for skiing. Pack comfortable shoes for exploring the trails, and don't miss the chance to try Allgäuer Bergkäse, the region’s renowned cheese. Carry a camera to capture the stunning landscapes."
)
print(f'\t - Added details for Location-{13:02} : Allgäu Valley')

# Brandenburg Gate
insert_location_details(
    location_id=14,
    description_intro="The Brandenburg Gate is an iconic neoclassical monument located in Berlin, Germany. Once a symbol of division during the Cold War, it now represents German reunification and peace.",
    description_history="Constructed between 1788 and 1791 by Carl Gotthard Langhans, the gate was commissioned by King Frederick William II of Prussia. It has witnessed significant historical events, including Napoleon's occupation and the fall of the Berlin Wall.",
    description_highlights="The gate is a must-see landmark, beautifully illuminated at night. It's located near other attractions like the Reichstag Building and the Holocaust Memorial. The gate's Quadriga, a chariot drawn by four horses, is a masterpiece of sculpture.",
    description_tips="Visit early in the morning or late in the evening to avoid crowds. The area around the gate is pedestrian-friendly, making it easy to explore. Wear comfortable shoes and consider joining a guided tour for historical insights."
)
print(f'\t - Added details for Location-{14:02} : Brandenburg Gate')

# Cologne Cathedral
insert_location_details(
    location_id=15,
    description_intro="Cologne Cathedral is a Gothic masterpiece and one of Germany’s most visited landmarks. Located in Cologne, it boasts stunning architecture and is a UNESCO World Heritage Site.",
    description_history="Construction of the cathedral began in 1248 and spanned over 600 years. It served as a pilgrimage site and remains an important symbol of faith and resilience, having survived WWII bombings.",
    description_highlights="The twin spires of the cathedral dominate Cologne's skyline. Visitors can climb to the top for panoramic views of the city. The cathedral houses impressive stained glass windows and the Shrine of the Three Kings.",
    description_tips="Arrive early to avoid crowds, especially during the summer. Dress modestly, as it's a place of worship. Climbing the spires requires good physical fitness. Don’t forget to explore the surrounding old town of Cologne."
)
print(f'\t - Added details for Location-{15:02} : Cologne Cathedral')

# Lake Königssee
insert_location_details(
    location_id=16,
    description_intro="Lake Königssee is a pristine alpine lake located in Berchtesgaden, Bavaria. Surrounded by steep mountains, it is renowned for its crystal-clear waters and serene atmosphere.",
    description_history="The lake has been a retreat for nature lovers for centuries. Historically, it was used for fishing and transportation. Today, it is protected as part of the Berchtesgaden National Park.",
    description_highlights="Take a boat ride to St. Bartholomew's Church, explore the hiking trails, and enjoy the echo demonstration on the lake. The area's untouched beauty makes it a favorite among photographers and adventurers.",
    description_tips="Visit early in the day to avoid crowds. Wear sturdy shoes if you plan to hike. Bring snacks, as food options near the lake can be limited. Check the weather forecast before planning a boat trip."
)
print(f'\t - Added details for Location-{16:02} : Lake Königssee')

# Neuschwanstein Castle
insert_location_details(
    location_id=17,
    description_intro="Neuschwanstein Castle is a fairy-tale castle located in Schwangau, Bavaria. Built by King Ludwig II, it is one of the most famous castles in the world and a major tourist attraction.",
    description_history="Construction began in 1869, intended as a retreat for the king. The castle's design was inspired by romanticized medieval architecture and Wagnerian operas. It was never completed, as Ludwig II died mysteriously in 1886.",
    description_highlights="The castle’s stunning interiors, including the Throne Room and Singer's Hall, are must-see. The Marienbrücke Bridge offers breathtaking views of the castle against the alpine backdrop.",
    description_tips="Book tickets in advance to avoid long lines. Wear comfortable shoes, as the walk to the castle involves a steep climb. Guided tours provide fascinating insights into its history. Visit during off-peak seasons for a quieter experience."
)
print(f'\t - Added details for Location-{17:02} : Neuschwanstein Castle')

# Reichstag Dome
insert_location_details(
    location_id=18,
    description_intro="The Reichstag Dome is a modern architectural marvel atop the German Parliament building in Berlin. The dome symbolizes transparency and offers panoramic views of the city.",
    description_history="The Reichstag building was completed in 1894 and has undergone several transformations, including severe damage during WWII. The dome was added in the 1990s, designed by architect Norman Foster.",
    description_highlights="Visitors can walk along the spiral ramp inside the dome to enjoy views of Berlin. The building also houses exhibits on German history and the Bundestag's functioning.",
    description_tips="Entry to the dome is free, but advance registration is required. Visit at sunset for spectacular views. Dress warmly if visiting during winter, as the dome can be chilly. Combine your visit with a tour of nearby attractions like the Brandenburg Gate."
)
print(f'\t - Added details for Location-{18:02} : Reichstag Dome')


# ----------------------------------------------------------------------------------------------
# Fill the maps:
# ----------------------------------------------------------------------------------------------

print("\n\n Inserting maps...")

# India:
print("\t India")

# Taj Mahal:
insert_map(
    location_id=1,
    latitude=27.1751, longitude=78.0421,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3549.400402283387!2d78.0395672755463!3d27.17514954876302!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39747121d702ff6d%3A0xdd2ae4803f767dde!2sTaj%20Mahal!5e0!3m2!1sen!2sin!4v1731096906266!5m2!1sen!2sin')
)
print(f'\t - Added map for Location-{1:02} : Taj Mahal')

# Jaipur City Palace:
insert_map(
    location_id=2,
    latitude=26.9124, longitude=75.7873,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3557.2969486586367!2d75.82109647553895!3d26.925799059527854!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db40b8620b0c1%3A0x44801531017d7b60!2sThe%20City%20Palace!5e0!3m2!1sen!2sin!4v1731099652719!5m2!1sen!2sin')
)
print(f'\t - Added map for Location-{2:02} : Jaipur City Palace')

# Mysore Palace:
insert_map(
    location_id=3,
    latitude=12.3051, longitude=76.6551,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3898.157648891582!2d76.65259997524211!3d12.305168229138431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3baf701103f9a1f9%3A0xc37fbae2a124da0d!2sMysore%20Palace!5e0!3m2!1sen!2sin!4v1731099719717!5m2!1sen!2sin')
)
print(f'\t - Added map for Location-{3:02} : Mysore Palace')

# Ellora Caves:
insert_map(
    location_id=4,
    latitude=20.0264, longitude=75.1822,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14994.081656486365!2d75.15761048715821!3d20.02863330000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdb92609201a9eb%3A0xe0639ba6286a474!2sEllora%20Cave%20No.%2029%20The%20Dhumar%20Lena!5e0!3m2!1sen!2sin!4v1731098951522!5m2!1sen!2sin')
)
print(f'\t - Added map for Location-{4:02} : Ellora Caves')

# Gateway of India:
insert_map(
    location_id=5,
    latitude=18.9220, longitude=72.8347,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3774.2124287744723!2d72.83207937534421!3d18.92198915678915!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7d1c73a0d5cad%3A0xc70a25a7209c733c!2sGateway%20Of%20India%20Mumbai!5e0!3m2!1sen!2sin!4v1731099772759!5m2!1sen!2sin')
)
print(f'\t - Added map for Location-{5:02} : Gateway of India')

# Kaziranga National Park:
insert_map(
    location_id=6,
    latitude=26.6574, longitude=93.1968,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14279.453420942631!2d92.98384525627273!3d26.524518829310978!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3744fbb424af3d57%3A0x4d16514f2d701362!2sKaziranga%20National%20Park%2C%20Assam!5e0!3m2!1sen!2sin!4v1731100048295!5m2!1sen!2sin')
)
print(f'\t - Added map for Location-{6:02} : Kaziranga National Park')

# ----------------------------------------------------------------------------------------------

# France:
print("\t France")

# Bordeaux Place
insert_map(
    location_id=7,
    latitude=44.8378, longitude=-0.5792,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d90493.80973923237!2d-0.6684125996549064!3d44.863688174012964!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd5527e8f751ca81%3A0x796386037b397a89!2sBordeaux%2C%20France!5e0!3m2!1sen!2sin!4v1732047436727!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{7:02} : Bordeaux Place')

# Eiffel Tower
insert_map(
    location_id=8,
    latitude=48.8584, longitude=2.2945,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2624.991626110945!2d2.2919063765339804!3d48.858370071332196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e66e2964e34e2d%3A0x8ddca9ee380ef7e0!2sEiffel%20Tower!5e0!3m2!1sen!2sin!4v1732047511318!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{8:02} : Eiffel Tower')

# French Riviera
insert_map(
    location_id=9,
    latitude=43.7034, longitude=7.2663,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d742269.6317850997!2d5.861370156481297!3d43.38767112940292!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12cebc738732d97f%3A0x594966412c5651c0!2sFrench%20Riviera%2C%20France!5e0!3m2!1sen!2sin!4v1732047580000!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{9:02} : French Riviera')

# Loire Valley
insert_map(
    location_id=10,
    latitude=47.3667, longitude=0.7500,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1378484.4027711952!2d-0.6241136383180284!3d47.560932506478764!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47fd31c40ddaa889%3A0xd49789bfb849e842!2sLoire%20Valley%2C%20France!5e0!3m2!1sen!2sin!4v1732047633991!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{10:02} : Loire Valley')

# Palace of Versailles
insert_map(
    location_id=11,
    latitude=48.8049, longitude=2.1204,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2627.7963721453993!2d2.11778047653095!3d48.804864871324966!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e67d94d7b14c75%3A0x538fcc15f59ce8f!2sPalace%20of%20Versailles!5e0!3m2!1sen!2sin!4v1732047662419!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{11:02} : Palace of Versailles')

# Mont Saint Michel
insert_map(
    location_id=12,
    latitude=48.6361, longitude=-1.5115,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d21097.885092720426!2d-1.5492976957613078!3d48.62447276326066!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x480ea8d67c9ceeb3%3A0xc5834ce47e0dc3fe!2s50170%20Mont%20Saint-Michel%2C%20France!5e0!3m2!1sen!2sin!4v1732047694783!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{12:02} : Mont Saint Michel')

# ----------------------------------------------------------------------------------------------

# Germany:
print("\t Germany")

# Allgäu Valley
insert_map(
    location_id=13,
    latitude=47.5807, longitude=10.2743,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d687639.2500243224!2d10.08489537793109!3d47.6826561513961!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x479c7ca4ffebd9c3%3A0xcfbb905589e36007!2zQWxsZ8OkdQ!5e0!3m2!1sen!2sin!4v1732047733617!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{13:02} : Allgäu Valley')

# Brandenburg Gate
insert_map(
    location_id=14,
    latitude=52.5163, longitude=13.3777,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2427.948306852939!2d13.37512917674518!3d52.51627457206017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47a851c655f20989%3A0x26bbfb4e84674c63!2sBrandenburg%20Gate!5e0!3m2!1sen!2sin!4v1732047766950!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{14:02} : Brandenburg Gate')

# Cologne Cathedral
insert_map(
    location_id=15,
    latitude=50.9413, longitude=6.9583,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2514.0505400622606!2d6.955706476652937!3d50.94127837169009!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47bf25a5369c3d2f%3A0x29ec913896e3a9c6!2sCologne%20Cathedral!5e0!3m2!1sen!2sin!4v1732047791789!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{15:02} : Cologne Cathedral')

# Lake Königssee
insert_map(
    location_id=16,
    latitude=47.5935, longitude=12.9901,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d43082.50107807436!2d12.93804228323545!3d47.55501737314839!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4776eecee3fd13a1%3A0x2ffeda19ea35cd8!2sK%C3%B6nigssee!5e0!3m2!1sen!2sin!4v1732047814674!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{16:02} : Lake Königssee')

# Neuschwanstein Castle
insert_map(
    location_id=17,
    latitude=47.5576, longitude=10.7498,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2692.524941859384!2d10.747225476461539!3d47.55757397118532!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x479cf7cac44ea35d%3A0xc8a6866bd39dbba3!2sNeuschwanstein%20Castle!5e0!3m2!1sen!2sin!4v1732047836079!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{17:02} : Neuschwanstein Castle')

# Reichstag Dome
insert_map(
    location_id=18,
    latitude=52.5186, longitude=13.3762,
    map_iframe=get_iframe_code("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2427.818692665521!2d13.373612276745318!3d52.5186201720608!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47a851c741ee506d%3A0x641b52d3abf17de5!2sReichstag%20Building!5e0!3m2!1sen!2sin!4v1732047859124!5m2!1sen!2sin")
)
print(f'\t - Added map for Location-{18:02} : Reichstag Dome')


# ----------------------------------------------------------------------------------------------
# Testing Section:
# ----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Test the database operations:
    print("Done")