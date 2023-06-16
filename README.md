Blog Site Readme
This is a blog site that allows users to create, edit, and delete blog posts. It also provides an API with filtering capabilities for accessing the blog posts. This readme will provide an overview of the blog site and its features.

Features
1) Create Blog Post: Authenticated users can create new blog posts by providing a title, content, and optionally, tags or categories for better organization.

2) Edit Blog Post: Users can edit their own blog posts, updating the title, content, and tags/categories associated with the post.

3) Delete Blog Post: Users can delete their own blog posts if they no longer wish to keep them.

4) Blog Post Listing: The blog site provides a listing of all the blog posts, displaying their titles, authors, and creation dates. Users can click on a blog post to view its full descriptiopn.

5) Filtering API: The site offers an API that allows users to filter blog posts based on different criteria such as author, tags, categories, or date. This API can be used by external applications or services to retrieve specific subsets of blog posts.
 
 
Technology Stack
Front-end: HTML, CSS
Backend: Flask
API


API Documentation
POST /api/article: Creates a new blog post.
PUT /api/article/<article_id>: Updates an existing blog post.
DELETE /api/article/<article_id>: Deletes a blog post.
