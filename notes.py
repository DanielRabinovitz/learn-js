#JS code is called using the <script> tag

#syntax:
#   <script src={filepath to JS file}> calls from file </script>
#   <script src={URL to JS file}> calls from file </script>

#Common issue with URL version:
#   hacker can catch script execution from file
#   by utilizing the URL. Must at least use https there.

#var let and const:
#Any browser from 2015 or before uses var as keyword
#Any browser from 2015 and after uses let, const
#Use let and const unless legacy browser support is super important

#variables are a thing, are dynamically typed.
#meaning, var type is specified at run time for flexibility.
#   Pro: Flexibility for developer
#   Con: Debugging is a pain in the ass

#You can do silly things with arithmetic:
#e.g. 
#   let x = "5" + 2 + 3 creates "523"
#   let x = 2 + 3 + "5" creates "55"
# + sign is used for string concat.

#let variables are locally scoped inside curly braces {}
#var variables are NOT locally scoped inside curly braces.
#In terms of function definitions and the like, let/var both stay local.
#blocks are weird.
#for some reason you can declare var variables
#before actually using the var keyword,
#because you can redeclare var variables multiple times (for some reason)

#const cannot be changed: it's read only.
#BUT you can change the values of the thing that
#const refers to. Because why the fuck not.
#Use const as your default variable keyword.


