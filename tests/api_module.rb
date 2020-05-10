require 'nokogiri'
require 'sinatra'
require 'JSON'
require './entryClass'

g = Graph.new
g.load_graph_from_json('data.json')

get '/actors' do
  g.all_actors_json
end

get '/actors/:name' do
  g.get_actor(params[:name])
end

get '/movies' do
  print params['name']
  g.all_movies_json
end

get '/movies/:name' do
  g.get_movie(params[:name])
end

get '/stats/biggest_pair' do
  g.best_pair.to_json
end

get '/stats/biggest_hubs' do
  g.top_hub_val_actors.to_json
end