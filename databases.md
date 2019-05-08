## Database Partitioning
Each partition may be spread over multiple nodes, and users at the node can perform local transactions on the partition. This increases performance for sites that have regular transactions involving certain views of data, whilst maintaining availability and security.

### Partitioning methods
The partitioning can be done by either building separate smaller databases (each with its own tables, indices, and transaction logs), or by splitting selected elements, for example just one table.
1. Horizontal partitioning involves putting different rows into different tables.
2. Vertical partitioning involves creating tables with fewer columns and using additional tables to store the remaining columns.

### Partitioning criteria
Current high end relational database management systems provide for different criteria to split the database. They take a partitioning key and assign a partition based on certain criteria. Common criteria are:
1. Range partitioning - selects a partition by determining if the partitioning key is inside a certain range.
2. List partitioning - a partition is assigned a list of values. If the partitioning key has one of these values, the partition is chosen.
3. Composite partitioning - allows for certain combinations of the above partitioning schemes. Consistent hashing could be considered a composite of hash and list partitioning where the hash reduces the key space to a size that can be listed.
4. Round-robin partitioning - the simplest strategy, it ensures uniform data distribution. With n partitions, the ith tuple in insertion order is assigned to partition (i mod n). This strategy enables the sequential access to a relation to be done in parallel. However, the direct access to individual tuples, based on a predicate, requires accessing the entire relation.
5. Hash partitioning - applies a hash function to some attribute that yields the partition number. This strategy allows exact-match queries on the selection attribute to be processed by exactly one node and all other queries to be processed by all the nodes in parallel.

## Data Striping
A technique for dividing large data into data blocks and spreading data over multiple storage devices. Data striping can speed up operations that retrieve data from disk storage.

Data redundancy, Load balancing (scalability), High availability, Monitoring and automation

