CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
   SELECT parents.child AS child FROM parents, dogs
      WHERE parents.parent = dogs.name
      ORDER by dogs.height desc;

-- The size of each dog
CREATE TABLE size_of_dogs AS
   SELECT dogs.name AS name, sizes.size AS size FROM dogs, sizes
      WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;
  


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS first, b.child AS second FROM parents AS a, parents AS b
      WHERE a.parent = b.parent AND a.child < b.child;
  

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT  SELECT "The two siblings, " || siblings.first || " and " || siblings.second || ", have the same size: " || a.size
      FROM siblings, size_of_dogs AS a, size_of_dogs AS b
      WHERE a.size = b.size AND a.name = siblings.first AND b.name = siblings.second;
;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

