# MovieMagic

#### There is two level of access:
###### User: view movies
###### admin: create, delete and edit movies 
####### username: admin password: admin

#### To create a new movie object - /movies/create/

##### e.g.
curl -H "Content-type:application/json" -u admin:admin -d '{"name":"Star Wars", "top99popularity":88.0, "director":"George Lucas", "imdb_score":8.8, "genres":["Adventure", "Action", "Fantasy", "Sci-Fi"]}' -X POST https://moviesapp1.herokuapp.com/movies/create/

##### To edit or delete movie object - /movie/<id>/
##### Note: This can only be accessed by admin

##### To view all the movies present in the database, do a GET call - /movies/view/

##### e.g. curl -H "Content-type:application/json" https://moviesapp1.herokuapp.com/movies/view/

##### Sample result: 
[{"name":"The Wizard of Oz","top99popularity":83.0,"director":"Victor Fleming","imdb_score":8.3,"id":1},
{"name":"Star Wars","top99popularity":88.0,"director":"George Lucas","imdb_score":8.8,"id":3}]

##### To view a movie with a particular id, do a GET call to /movies/view/<id>/

##### To search a movie, pass search parameter as q to /search/

##### e.g. 
curl -H "Content-type:application/json" https://moviesapp1.herokuapp.com/search/\?q\=Wiz
