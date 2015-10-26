## Abstract

This module include some classes extending [storm](https://storm.canonical.com/) ORM for [corpus](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html) data.

## Class List

* MovieTitlesMetadata
* Genre
* MovieGenreLine

## Usage

### Relationship setting

```
MovieTitlesMetadata.genres = ReferenceSet(MovieTitlesMetadata.id,
                                          MovieGenreLine.movie_id,
                                          MovieGenreLine.genre_id,
                                          Genre.id)
```

## Corpus Problem

This is memo when I dealt with corpus problems.

### movie_titles_metadata.txt

* I ignored an alphabet following year.
    * for example, line 34, `1989/I`
* I adjust title data for **Acute accent** manually.
    * line 115, `léon`
* I adjust genre data for **duplication**.
    * line 58, `['horror', 'mystery', 'mystery', 'sci-fi', 'sci-fi']`
