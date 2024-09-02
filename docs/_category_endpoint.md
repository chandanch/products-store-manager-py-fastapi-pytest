# Unit Test Planning

Unit test planning for the Category API Endpoints

## Category API Endpoints:
    
**Get**
- [ ] **Get** all categories

    - [ ] Retrieve all category data from database
        - [ ] Test sucessful database operation
        - [ ] Test no data returned from database 
        - [ ] Test unsuccessful database operation

- [ ] **Get** all categories by slug

    - [ ] Retrieve all category data from database
        - [ ] Test sucessful database operation
        - [ ] Test no data returned from database 
        - [ ] Test unsuccessful database operation


**Post**
- [ ] **Post** Create new category record

    - [ ] Check to make sure that the data sent via the request is validated
        - [ ] Test category schema data validation
            - [ ] Valid data
            - [ ] Invalid data
        - [ ] Test serialization (Is this needed?)
        - [ ] Test deserialization (Is this needed?)
        
  - [ ] Check name and level together is unique
        - [ ] Test POST new category when category exists with name and level 
     
    - [ ] Check slug is unique
        - [ ] Test POST new category when category exists with slug
       
    - [ ] Save a new category to the database
        - [ ] Test POST new category
            - [ ] Test sucessful database operation
            - [ ] Test unsuccessful database operation
    
**Put**
- [ ] **Update** a single category

    - [ ] Update single category 
        - [ ] Test sucessful database operation
        - [ ] Test category match found | no data returned
        - [ ] Test unsuccessful database operation

**Delele**

- [ ] **Delete** a single category

    - [ ] Delete a single category 
        - [ ] Test sucessful database operation
        - [ ] Test category match found | no data returned
        - [ ] Test unsuccessful database operation