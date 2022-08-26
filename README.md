# COAX Bootcamp exercise

This is set of HWs for the COAX Bootcamp.

## Exercise 2

### Pagination

Pagination was set for both Products and Orders. It is available in api.

### Filtering, Ordering, Search

All the above mentioned functionality is set for both Products and Orders. It is available in views.py and uses standard embedded functionality.

### Permissions

Custom permision was set for both Products and Orders. It was placed in permissions.py and requires all users to be logged in for unsafe methods, still allows looking at the products. Also, only admins can delete Orders and Products.

### Validators

A custom valiadator was set for Products. It requires price to be multiple of .25. It was placed in serializer.

### Throttling

Throttling was set up for Unauthorized Users to defend against webscrapping.
