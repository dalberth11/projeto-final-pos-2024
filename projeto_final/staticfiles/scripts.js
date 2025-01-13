const apiUrl = "http://127.0.0.1:8000/api/users/";

// Função para buscar usuários
async function fetchUsers() {
    try {
        const response = await fetch(apiUrl);
        const users = await response.json();
        const contentDiv = document.getElementById('content');
        contentDiv.innerHTML = ''; // Limpa a lista antes de adicionar

        users.forEach(user => {
            const userDiv = document.createElement('div');
            userDiv.classList.add('user');
            userDiv.innerHTML = `
                <strong>${user.name}</strong> (${user.email})
                <button class="delete" onclick="deleteUser(${user.id})">Excluir</button>
            `;
            contentDiv.appendChild(userDiv);
        });
    } catch (error) {
        console.error("Erro ao buscar usuários:", error);
    }
}

// Função para criar um usuário
document.getElementById('create-user-form').addEventListener('submit', async (event) => {
    event.preventDefault(); // Impede o envio do formulário e o recarregamento da página

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email }),
        });

        if (response.ok) {
            alert('Usuário criado com sucesso!');
            fetchUsers(); // Atualiza a lista de usuários
        } else {
            alert('Erro ao criar usuário!');
        }
    } catch (error) {
        console.error("Erro ao criar usuário:", error);
    }
});

// Função para excluir um usuário
async function deleteUser(userId) {
    try {
        const response = await fetch(`${apiUrl}${userId}/`, {
            method: 'DELETE',
        });

        if (response.ok) {
            alert('Usuário excluído com sucesso!');
            fetchUsers(); // Atualiza a lista de usuários
        } else {
            alert('Erro ao excluir usuário!');
        }
    } catch (error) {
        console.error("Erro ao excluir usuário:", error);
    }
}

// Carregar a lista de usuários ao carregar a página
fetchUsers();
