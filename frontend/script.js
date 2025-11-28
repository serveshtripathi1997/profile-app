fetch("/profile")
    .then(res => res.json())
    .then(profile => {
        document.getElementById("name").textContent = profile.name;
        document.getElementById("role").textContent = profile.role;

        renderList("primary", profile.primary);
        renderList("secondary", profile.secondary);
        renderList("tertiary", profile.tertiary);
    })
    .catch(err => console.error("API ERROR:", err));

function renderList(id, items) {
    const ul = document.getElementById(id);
    ul.innerHTML = ""; // clear existing
    items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        ul.appendChild(li);
    });
}

