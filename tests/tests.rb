###################################################################
#                                                                 #
#                                                                 #
#        Testing file                                             #
#                                                                 #
#                                                                 #
###################################################################
require_relative('entryClass.rb')

def base_gross_test()
  g = Graph.new

  m = Movie.new('Avatar', 2012, 40000000)
  m2 = Movie.new('Amadeus', 1984, 2300000)
  a = Actor.new('Sam Worthington', 1976, 0, [])
  g.add_actor_node(a)
  g.add_movie_node(m)
  g.add_movie_node(m2)
  if g.all_gross == 42300000
    puts 'Passed Gross test'
  else
    puts 'Failed gross test, got value ' + g.all_gross.to_s
  end
end

def scrape_keanu_test
  g = Graph.new
  scrape_actor(g, 'keanu_reeves.html', 1, 10)
  puts '-------------'
  if g.num_actor == 1
    if g.num_movie == 7
      puts 'Passed Keanu test'
    else
      puts 'Failed Keanu test: g.num_movie is ' + g.num_movie.to_s
    end
  else
    puts 'Failed Keanu test: g.num_actor is ' + g.num_actor.to_s
  end
end

def scrape_morgan_freeman_test
  g = Graph.new
  actor = scrape_actor(g, 'morgan_freeman.html', 0, 1)
  puts '-------------'
  if actor.name == 'Morgan Freeman'
    if actor.age == 80
      puts 'Passed Morgan Freeman test'
    else
      puts 'Failed Morgan Freeman test: age is is ' + g.num_movie.to_s
    end
  else
    puts 'Failed Morgan Freeman test: name is is ' + g.num_actor.to_s
  end
end



def save_as_json_test
  g = Graph.new

  m = Movie.new('Avatar', 2012, 40000000)
  m2 = Movie.new('Amadeus', 1984, 2300000)
  a = Actor.new('Sam Worthington', 1976, 0, [])
  g.add_actor_node(a)
  g.add_movie_node(m)
  g.add_movie_node(m2)
  g.save_graph_as_json
  if File.open('temp.json', 'r').read == '{"movie":[["Avatar","2012",40000000],["Amadeus","1984",2300000]],"actor":[["Sam Worthington","41"]],"edges":[]}'
    puts 'Passed save as json test'
  else
    puts 'Failed save as json test'
  end
end

def graph_library_tests
  g = Graph.new
  m = Movie.new('The Boxer', 1997, 16500000)
  a1 = Actor.new('Emma Watson', 31, 0, [])
  a2 = Actor.new('Daniel Day-Lewis', 45, 0, [])
  a3 = Actor.new('Humphrey Bogart', 105, 0, [])

  g.add_movie_node(m)
  g.add_actor_node(a1)
  g.add_actor_node(a2)
  g.add_actor_node(a3)
  g.addEdge(m, a1)
  g.addEdge(m, a2)
  puts g.all_actors_in_movie('The Boxer')
  puts '---------------'
  puts g.n_oldest_actors
  puts g.all_gross
end

# Test the loading function of the graph function
def load_json_test
  g = Graph.new
  g.load_graph_from_json('data.json')
  if g.num_actor == 3
    if g.num_movie == 1
      puts 'Passed load test!'
    else
      puts 'Failed load test, not enough movies'
    end
  else
    puts 'Failed load test, not enough actors'
  end
end

def full_125_250_test(base_url, is_actor)
  g = Graph.new
  if is_actor
    scrape_actor(g, base_url, 25, 50)
  else
    scrape_movie(g, base_url, 125, 250)
  end
end

def shared_movie_test
  g = Graph.new
  g.load_graph_from_json('data.json')
  print g.best_pair
end

def actor_hub_test
  g = Graph.new
  g.load_graph_from_json('data.json')
  print g.top_hub_val_actors
end

def djikstra
  g = Graph.new
  g.load_graph_from_json('data.json')
  g.update_matrix
  print g.run_djikstras_on_actors
end

# graph_library_tests
# base_gross_test
# scrape_keanu_test
# scrape_morgan_freeman_test
# full_125_250_test($domain + '/wiki/James_Mason', true)

# save_as_json_test
# load_json_test
# shared_movie_test
# actor_hub_test

# djikstra