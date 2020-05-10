

def base_gross_test()
  g = new Graph
  g.addNode('a')
  g.addNode('b')
  g.addNode('c')

  g.addEdge('a', 'b')

  m = Movie.new('Avatar', 2012, 40000000)
  m2 = Movie.new('Amadeus', 1984, 2300000)
  a = Actor.new('Sam Worthington', 1976)
  g.add_actor_node(a)
  g.add_movie_node(m)
  g.add_movie_node(m2)
  puts g.all_gross
end

def scrape_keanu_test
  g = new Graph
  scrape_actor(g, 'keanu_reeves.html', 1, 10)
  puts '-------------'
  puts g.num_actor
  puts g.num_movie
end

#base_gross_test
#scrape_keanu_test

{1,2,3}.first(1)