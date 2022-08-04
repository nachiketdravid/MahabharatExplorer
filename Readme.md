### Install the jaal library:

pip install jaal

### Running File:
> python plot.py

You can change the data in the files and then press Ctrl+C to soft-reload the app. Then refresh the page to see the changes.
You can stop the act by Ctrl+Z.

### File Structure:

Nodes File:

>Id(Name), Gender

Edges File:

>From(X), To(Y), Relation(Who is Y of X?)

### Example Edge Queries
> relation == "Son"
> relation == "Son" or relation == "Daughter"


### Relationship Types:
- Son
- Daughter
- Father
- Mother
- Husband
- Wife
