import urllib2

director = urllib2.OpenerDirector()
director.add_handler(handler)

req = urllib2.Request('http://localhost:3003/actors/BruceWillis', headers = {'Accept' : 'application/xml'})

result = director.open(req)

# To get say the content-length header
json = result.info()['Content']

assert json == '{"name":"Bruce Willis","age":61,"total_gross":562709189,"movies":["The First Deadly Sin","The Verdict","Blind Date","Sunset","Die Hard","In Country","Look Whos Talking","Thats Adequate","Die Hard 2","Look Who\'s Talking Too","The Bonfire of the Vanities","Mortal Thoughts","Hudson Hawk","Billy Bathgate","The Last Boy Scout","The Player","Death Becomes Her","Loaded Weapon 1","Striking Distance","Color of Night","North","Pulp Fiction","Nobody\'s Fool","Die Hard with a Vengeance","Four Rooms","12 Monkeys","Last Man Standing","Beavis and Butt-Head Do America","The Fifth Element","The Jackal","Mercury Rising","Armageddon","The Siege","Breakfast of Champions","The Sixth Sense","The Story of Us","The Whole Nine Yards","Disney\'s The Kid","Unbreakable","Bandits","Hart's War","True West","The Crocodile Hunter: Collision Course","Grand Champion","Tears of the Sun","Rugrats Go Wild","Charlie's Angels: Full Throttle","The Whole Ten Yards","Ocean's Twelve","Hostage","Sin City","Alpha Dog","16 Blocks","Fast Food Nation","Lucky Number Slevin","Over the Hedge","Hammy's Boomerang Adventure","The Astronaut Farmer","Perfect Stranger","Grindhouse","Planet Terror","Nancy Drew","Live Free or Die Hard","What Just Happened","Assassination of a High School President","Surrogates","Cop Out","The Expendables","Red","Set Up","Catch .44","Moonrise Kingdom","Lay the Favorite","The Expendables 2","The Cold Light of Day","Looper","Fire with Fire","A Good Day to Die Hard","G.I. Joe: Retaliation","Red 2","Sin City: A Dame to Kill For","The Prince","Vice","Rock the Kasbah","Extraction","Precious Cargo","Marauders","Split","The Bombing","Once Upon a Time in Venice","First Kill","Death Wish"]}'