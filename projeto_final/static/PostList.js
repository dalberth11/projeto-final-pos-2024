import React, { useState, useEffect } from "react";
import axios from "axios";

function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/posts/");
        setPosts(response.data);
      } catch (error) {
        console.error("Erro ao carregar os posts:", error);
      }
    };
    fetchPosts();
  }, []);

  return (
    <div>
      <h2>Lista de Posts</h2>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostList;
