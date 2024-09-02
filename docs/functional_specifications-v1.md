# Functional Speifications

Functional specifications for an API outline the behavior, functionality, and interactions of the API.

## Category API Endpoints:
    
**Get**
- [ ] **Get** all categories
- [ ] **Get** all categories by slug

**Post**
- [ ] **Create** a new single category

**Put**
- [ ] **Update** a single category

**Delete**
- [ ] **Delete** a single category

## Input/Output:
    
- ## **Get**
- [ ] **Get** all categories

    **Input**
    ```
    None
    ```
    **Output**
    ```
    id: int
    name: str
    slug: str
    is_active: bool
    parent_id: Optional
    level: int
    ```

- [ ] **Get** all categories by slug

    **Input**
    ```
    URL/{slug_id: int}
    ```
    **Output**
    ```
    id: int
    name: str
    slug: str
    is_active: bool
    parent_id: Optional
    level: int
    ```

- ## **Post**

- [ ] **Create** a new single category

    **Input**
    ```
    name: str
    slug: str
    is_active: bool
    parent_id: Optional
    level: int
    ```
    **Output**
    ```
    id: int
    name: str
    slug: str
    is_active: bool
    parent_id: Optional
    level: int
    ```
- ## **Put**

- [ ] **Update** a single category

    **Input**
    ```

    URL/{category_id: int}

    name: str
    slug: str
    is_active: bool
    parent_id: Optional
    level: int
    ```
    **Output**
    ```
    id: int
    name: str
    slug: str
    is_active: bool
    parent_id: Optional
    level: int
    ```

- ## **Delete**

- [ ] **Delete** a single category

    **Input**
    ```
    URL/{category_id: int}
    ```
    **Output**
    ```
    id: int
    name: str
    ```