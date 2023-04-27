# Normalisation
## Benefits of normalisation
- Makes data bases better
- Reducing Redundancy(repetition) so that it is easier to understand, process, enter data. Also reducing redundancy reduces chances for errors/inconsistencies(anomalies)/erroneous data

## Normal Forms
 We can fix redundacy with normal forms

- **1NF** - First Normal Form: **Field/column names must be unique**, **Field data must be atomic**(one thing/ can't be seprated into differnt fields/ field data must be from the same domain/ **must be one data type**), we must have a primary key(a field (or set of fields) that uniquely identifies each record)

- **2NF** - Data dependant on the whole of the primary key (no partial dependancies)

- **3NF** - Data not dependant on a field that is not the primary key (no transitive dependancies)

### **Normalisaton**: data in fields must depend on:
1. The KEY
2. The whole KEY
3. And nothing but the KEY  
- *This pneumnoic is based on what a witness says in court **"tell the truth, the whole truth, and nothing but the truth, so help me God** (if you are religous you use the god bit)*

(So help me Codd - the guy that came up with these normalisation rules-)

## friday notes
- you cant have many-to-many relationships in a database  
- so you have to have multiple one-to-one or many-to-one (might be one-to-many not sure whixh is right) realtionships 