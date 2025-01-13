import React from "react";
import UserList from "./components/UserList";
import CreateUserForm from "./components/CreateUserForm";
import PostList from "./components/PostList";
import "./index.css";

function App() {
  return (
    <div className="app-container">
      <h1>Cliente da API</h1>
      <CreateUserForm />
      <UserList />
      <PostList />
    </div>
  );
}

export default App;
