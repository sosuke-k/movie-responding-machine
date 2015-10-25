## Abstract

This module include some classes extending [storm](https://storm.canonical.com/) ORM for corpus data.

## Class List

* MovieTitlesMetadata
* Genre
* MovieGenreLine

## Usage

```
Company.accountants = ReferenceSet(Company.id,
  CompanyAccountant.company_id,
  CompanyAccountant.accountant_id,
  Accountant.id)
```

## NOTE

This is memo when I dealed with corpus problems.

## Problem

### movie_titles_metadata.txt

* I ignored an alphabet following year.
    * for example, line 34, `1989/I`
* I adjust title data for **Acute accent** manually.
    * line 115, `léon`
