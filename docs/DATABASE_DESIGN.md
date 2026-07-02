# 📊 Database Design (Blog + CRM System)

## 🧠 What is ER Diagram?
ER Diagram (Entity Relationship Diagram) represents:
- Entities (tables)
- Attributes (fields)
- Relationships (connections)

---

# 🧩 Entities

## 👤 User
- id (PK)
- name
- email
- password
- role
- created_at

---

## 🏷 Category
- id (PK)
- name

---

## 📝 BlogPost
- id (PK)
- title
- content
- status (draft, published)
- image_url
- user_id (FK → User.id)
- category_id (FK → Category.id)
- created_at

---

## 💬 Comment
- id (PK)
- content
- user_id (FK → User.id)
- blogpost_id (FK → BlogPost.id)
- created_at

---

## 💼 Lead
- id (PK)
- name
- email
- status (new, contacted, converted, rejected, lost)
- document_url
- user_id (FK → User.id)
- created_at

---

## 🗒 Note
- id (PK)
- content
- lead_id (FK → Lead.id)
- user_id (FK → User.id)
- created_at

---

# 🔗 Relationships

- User (1) → (Many) BlogPost  
- User (1) → (Many) Comment  
- User (1) → (Many) Lead  
- User (1) → (Many) Note  

- Category (1) → (Many) BlogPost  

- BlogPost (1) → (Many) Comment  

- Lead (1) → (Many) Note  

---

# 📊 ER Diagram (Text Representation)


---

# 🚀 Summary

- This design supports:
  - Blog system (posts, comments, categories)
  - CRM system (leads, notes)
  - File handling (image_url, document_url)

- Follows:
  - Normalization
  - One-to-Many relationships
  - Scalable architecture

---